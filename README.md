README.md (TravelAI)
AI-Powered Multi-Agent Travel Planning System

Track: Concierge Agents – Google × Kaggle 5-Day AI Agents Intensive Capstone
Author: Darshan
Project Name: TravelAI

🚀 Overview

TravelAI is an automated AI travel concierge built using multi-agent architecture, OpenAI LLMs, Google Search tools, long-term memory, and custom tools.
It generates complete personalized travel itineraries, budgets, hotel plans, activity summaries, and safety notes — all automatically orchestrated through coordinated agents.

This project demonstrates:

Multi-agent orchestration

Sequential + parallel agents

Tool calling

LLM-powered reasoning

Memory-based session handling

Observability & structured logging

A2A-style design patterns

Gemini/OpenAI usage (OpenAI is default here)

🎯 Problem Statement

Planning a trip takes hours — researching flights, hotels, activities, safety, budgeting, and transportation manually.

Most people check 10–15 websites, copy-paste information into notes, compare prices themselves, and struggle to make optimized choices.

💡 Solution

TravelAI automates the entire process using coordinated AI agents:

A Planner Agent creates the high-level itinerary

A Budget Agent estimates costs

A Search Agent uses Google Search tools

A Safety Agent checks advisories

A Refinement Agent polishes and formats results

A Memory Manager stores traveler preferences

Everything runs under a Travel Orchestrator, which manages agent order, parallelism, and context sharing.

✨ Core Features
✔ Multi-Agent System

Sequential planning → parallel research → sequential refinement.

Each agent has its own task, tools, and memory scope.

✔ Tooling

Google Search

Custom tools (date parsing, score ranking)

OpenAI LLM calls for generation

✔ Memory & State

InMemory session state

User preference memory (food, budget level, travel style)

✔ Observability

Structured logging

Step-level tracing (which agent called which tool)

✔ Long-running operations

Automatic pause/resume for long searches

🧠 Architecture
                            ┌──────────────────────┐
                            │   User Request       │
                            └──────────┬───────────┘
                                       │
                             ┌─────────▼────────┐
                             │ Travel Orchestrator │
                             └───────┬───────────┘
         ┌──────────────┬──────────┼───────────┬──────────────┐
         ▼              ▼           ▼           ▼               ▼
 Planner Agent   Budget Agent   Search Agent   Safety Agent   Memory Agent
 (LLM)            (LLM)          (Google)       (LLM)          (Storage)
         └──────────────┴──────────┼───────────┴──────────────┘
                                    ▼
                           Refinement Agent (LLM)
                                    ▼
                           Final Travel Plan Output

📦 Project Structure
travelai/
│
├── agents/
│   ├── planner_agent.py
│   ├── budget_agent.py
│   ├── search_agent.py
│   ├── safety_agent.py
│   ├── refine_agent.py
│
├── tools/
│   ├── search_tool.py
│   ├── date_parser.py
│   ├── price_ranker.py
│
├── memory/
│   ├── session_state.py
│   ├── preference_store.py
│
├── orchestrator/
│   ├── travel_orchestrator.py
│
├── main.py
├── requirements.txt
├── LICENSE
└── README.md

🛠️ Installation
1. Clone Repo
git clone https://github.com/DarshanAI/TravelAI.git
cd TravelAI

2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

🔐 Environment Variables

Create .env:

OPENAI_API_KEY=your_key
GOOGLE_API_KEY=optional

▶ Run the agent
python main.py


Example request inside the app:

plan = orchestrator.run({
    "destination": "Germany",
    "days": 5,
    "budget": "medium",
    "preferences": ["architecture", "cafes", "night tours"]
})
print(plan)

📑 Kaggle Capstone Requirements Check
Requirement	Status
Multi-agent system	✔
LLM-powered reasoning	✔
Parallel & sequential agents	✔
Tools (custom + search)	✔
Memory	✔
Observability/logging	✔
Documentation	✔
OpenAI/Gemini usage	✔ (OpenAI default)
📝 Short GitHub Description (for repo sidebar)

TravelAI – Multi-Agent AI Travel Planner using OpenAI + tools. Automates itinerary creation, budgeting, research, and safety checks using orchestrated LLM agents. Kaggle Agents Intensive Capstone Project (Concierge Track).

📄 Should your repo be licensed?

Yes — MIT (already provided).
This allows people to use your project and protects you legally
MIT License
