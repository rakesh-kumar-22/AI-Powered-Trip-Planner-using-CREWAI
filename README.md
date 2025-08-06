# 🗺️ AI-Powered Trip Planner with CrewAI

> **Plan your perfect trip in seconds** — powered by multi-agent collaboration, GPT‑4o‑mini intelligence, and real-time web search.

## 🚀 Overview
This project uses **CrewAI** to orchestrate three specialized AI agents that work together to design a fully personalized travel itinerary.  
It integrates **real-time web search** (via DuckDuckGo) and **OpenAI GPT‑4o‑mini** for fast, context-aware reasoning to deliver **up-to-date travel recommendations**, then presents them in a ready-to-download trip plan.

Whether you’re planning a **cultural getaway**, an **adventure trip**, a **shopping spree**, or a **sightseeing journey** — the AI team handles the research, curation, and planning for you.

---

## 🧠 How It Works

### **1. Multi-Agent Setup**
Three dedicated CrewAI agents, each with a unique role:

| Agent | Role | Description |
|-------|------|-------------|
| **Location Expert** | Research | Finds updated details about the destination (climate, attractions, travel tips). |
| **Guide Expert** | Curation | Suggests the best activities, spots, and local experiences based on user interest. |
| **Planner Expert** | Itinerary Building | Designs a day-by-day trip plan integrating travel dates, activities, and recommendations. |

---

### **2. Real-Time Web Search**
Instead of static data, the system uses **DuckDuckGo Search Tool** to pull **fresh, relevant travel info** — perfect for checking current events, latest attractions, or seasonal changes.

---

### **3. User-Driven Planning**
The user provides:
- **From City**
- **Destination City**
- **From Date**
- **Return Date**
- **Interest**: `Adventure` | `Shopping` | `Culture` | `Sightseeing`

The CrewAI agents then **collaboratively** generate the final travel plan using **OpenAI GPT‑4o‑mini** for reasoning and content generation.

---

### **4. Streamlit Web App**
A clean, interactive UI built in **Streamlit** allows:
- Easy input of trip details
- Instant itinerary generation
- One-click **download** of the plan as `.txt`

---

## 📦 Tech Stack

- **[CrewAI](https://www.crewai.io/)** – Multi-agent orchestration
- **[OpenAI GPT‑4o‑mini](https://platform.openai.com/)** – Fast, efficient LLM reasoning
- **DuckDuckGo Search Tool** – Live web search integration
- **Streamlit** – Web app interface
- **Python** – Core scripting & logic

---
