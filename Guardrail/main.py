import re
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from sentence_transformers import SentenceTransformer, util

# Initialize FastAPI
app = FastAPI(title="Uptoskill Guardrail")

# Load Model (MiniLM is perfect for Phase 2: low latency, medium-high accuracy)
model = SentenceTransformer('all-MiniLM-L6-v2')

# --- SCHEMAS ---
class GuardrailRequest(BaseModel):
    question: str
    answer: str

class GuardrailResponse(BaseModel):
    valid: bool
    issue_type: Optional[str] = None
    confidence: float

# --- DETECTION LOGIC ---
def get_validation(question: str, answer: str):
    q_clean = question.strip()
    a_clean = answer.strip()

    # 1. Empty/Short Check
    if len(a_clean) < 3:
        return False, "empty", 1.0

    # 2. Nonsense/Gibberish (Check for low variety in characters)
    if len(set(a_clean.lower())) < 4 and len(a_clean) > 10:
        return False, "nonsense", 0.95

    # 3. Generic/Memorized Detection
    generic_regex = r"(i don't know|i do not know|not sure|skip|test answer|asdf)"
    if re.search(generic_regex, a_clean.lower()):
        return False, "generic", 0.90

    # 4. Semantic Irrelevance (The AI part)
    q_emb = model.encode(q_clean, convert_to_tensor=True)
    a_emb = model.encode(a_clean, convert_to_tensor=True)
    cosine_sim = util.pytorch_cos_sim(q_emb, a_emb).item()

    # If similarity < 0.25, the answer is likely off-topic
    if cosine_sim < 0.25:
        return False, "irrelevant", round(1 - cosine_sim, 2)

    return True, None, round(cosine_sim, 2)

# --- ROUTES ---
@app.post("/validate", response_model=GuardrailResponse)
async def validate_answer(payload: GuardrailRequest):
    is_valid, issue, conf = get_validation(payload.question, payload.answer)
    return {
        "valid": is_valid,
        "issue_type": issue,
        "confidence": conf
    }