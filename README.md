# 🛡️ Guardrail: Invalid & Irrelevant Answer Detection System

This repository contains **Task 19** (Phase 2 Guardrails) for the AI Interview Assessment System. It acts as a gatekeeper to ensure only high-quality, relevant responses are passed to the evaluation engine.

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
