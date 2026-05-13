# 🛡️ Guardrail: Invalid & Irrelevant Answer Detection System

This repository contains  Guardrails for the AI Interview Assessment System. It acts as a gatekeeper to ensure only high-quality, relevant responses are passed to the evaluation engine.

---

## 🎯 Objective
To detect and flag invalid responses to optimize the evaluation pipeline and provide signals to the decision engine for corrective follow-ups.

### Target Detection Categories:
- **Irrelevant:** Answers that do not align with the question's topic.
- **Generic:** Memorized or evasive answers (e.g., "I don't know").
- **Nonsense:** Keyboard smashing or gibberish.
- **Empty:** Null or extremely short inputs.

---

## 🛠️ Detection Strategies
The system uses a multi-layered logic approach to ensure high precision:

| Strategy | Implementation | Purpose |
| :--- | :--- | :--- |
| **Semantic Similarity** | `Sentence-Transformers` | Measures vector distance between Question and Answer. |
| **Pattern Detection** | Regex & Phrase Mapping | Identifies "I don't know" and other evasive templates. |
| **Length Heuristics** | Character/Word Count | Flags empty or too-short responses. |
| **Entropy Check** | Unique Character Variety | Detects gibberish/nonsense (e.g., "asdfasdf"). |

---

## ⚙️ Technical Specifications

### Input Schema
```json
{
  "question": "string",
  "answer": "string"
}
```
### Output Schema
```json
{
  "valid": "boolean",
  "issue_type": "irrelevant | generic | empty | nonsense | null",
  "confidence": "float (0-1)"
}
```
---
## 🚀 Installation & Setup

1. **Install Dependencies:**
   Using the provided requirements file ensures all AI models and server components are version-synced:
   ```bash
   pip install -r requirements.txt

2. **Run the service:**
   ```bash
   uvicorn Guardrail.main:app --reload

### Pipeline Behavior
This guardrail is integrated **before** deep evaluation. 
- **If `valid: false`:** The system overrides the evaluation score to **0**.
- **Confidence Scores:** Used by the decision engine to determine flag strength.

---

## ✅ Deliverables Summary
- **Detection Logic:** Multi-layered approach combining heuristic filters with AI-driven semantic validation.
- **Rule Definitions:** Transparent logic thresholds defined for Empty, Nonsense, Generic, and Irrelevant categories.
- **High Precision:** Calibration optimized to handle short but correct responses while flagging verbose irrelevance.
- **Integration Ready:** Fully compatible with the existing evaluation pipeline for automated scoring overrides.


