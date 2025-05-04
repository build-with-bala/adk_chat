# 🧠 Gemini Multi-Agent Research Assistant (Google ADK + LLMs)

This project implements a **multi-agent system using Google ADK** (Agent Development Kit) with a clean agent pipeline:  
**Commander → Discusser → Validator**, powered by Gemini models.

Built for:
- 🧪 Multi-step reasoning
- 🧵 Collaboration between agents
- ⚡️ Command-line access via tools
- 👤 Human-in-the-loop approval

---

## 🔧 Agent Roles

| Agent        | Model              | Description                                               |
|--------------|-------------------|-----------------------------------------------------------|
| **Commander** | `gemini-1.5-pro`   | Thinks deeply, generates solutions, and executes code (with permission) |
| **Discusser** | `gemini-2.0-flash` | Quickly critiques or expands Commander’s outputs          |
| **Validator** | `gemini-1.5-pro`   | Validates final reasoning and gives guidance              |

> ⚠️ Note: `gemini-2.0-flash` is used **without tools** due to function call limitations.

---

## 🗂 Project Structure

