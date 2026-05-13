# Task 19: Invalid / Irrelevant Answer Detection System (Guardrails Phase 2)

## 📌 Project Overview
This module is a core component of the **AI Interview Assessment System** Guardrails. It acts as a gatekeeper to detect and flag answers that are irrelevant, generic, nonsensical, or empty before they are processed by the evaluation engine.

### Objectives:
- **Filter Noise:** Prevent garbage data from reaching the scoring logic.
- **Cost Efficiency:** Bypass expensive LLM evaluations for invalid responses.
- **Enhanced Feedback:** Provide specific signals to the decision engine for follow-up triggers.

## 🛠️ Technical Architecture
The system is built using **FastAPI** for high-performance serving and **PyTorch/Sentence-Transformers** for deep semantic analysis.

### Detection Strategies:
1. **Length Heuristics:** Identifies empty strings or answers under the minimum character threshold.
2. **Nonsense Detection:** A unique character variety check to catch "keyboard smashing" (e.g., *asdfghjkl*).
3. **Pattern Matching:** Regex-based filtering for "memorized" or "evasive" responses (e.g., *"I don't know"*, *"Not sure"*).
4. **Semantic Similarity:** Uses the `all-MiniLM-L6-v2` transformer model to compare the mathematical vector of the question against the answer.

## ⚙️ API Specification

### Input Schema
```json
{
  "question": "string",
  "answer": "string"
}
