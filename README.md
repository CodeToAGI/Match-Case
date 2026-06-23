# CodeToAGI — Episode 44: Match / Case (Structural Pattern Matching)

**Python 3.10+ Feature**

---

## 🎯 What You Learned

- Structural Pattern Matching (`match` / `case`)
- 6 Pattern Types: **Literal**, **Capture**, **Sequence**, **Mapping**, **Class**, **OR**
- **Guards** (`if` conditions)
- Real-world use cases (CLI routers, API responses, AI tool calling)

---

## 🚀 Challenge: Build a Command Dispatcher

**Goal**: Replace messy `if/elif` chains with clean, readable `match/case`.

### Requirements

1. Handle string commands like:
   - `help`
   - `quit`
   - `go north` / `go south` etc.

2. Use a **guard** to validate directions.

3. Support variable-length commands (`pick sword dungeon`).

4. **Bonus**: Support dictionary-based commands.

---

### Solution

See `challenge_command_dispatcher.py`

---

## How to Run

```bash
python challange_code.py
