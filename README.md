# TravelAI

A production‑grade, modular AI agent system specializing in travel planning, trip optimization, bookings, and real‑time information retrieval using OpenAI LLMs. The project follows clean architecture principles and is structured for scalability, observability, and deployment.

## Features

* Multi‑agent orchestration (Planner, Booking, Knowledge)
* OpenAI LLM‑powered reasoning
* Tool integrations (weather, flights, search)
* Memory and session management
* Modular service layer (LLM client, evaluation, observability)
* Config-driven environment
* Fully typed Python codebase

## Repository Structure

```
travelai/
│── README.md
│── pyproject.toml
│── .gitignore
│── travelai/
│   ├── __init__.py
│   ├── config/
│   │   └── settings.py
│   ├── agents/
│   │   ├── planner.py
│   │   ├── booking.py
│   │   └── knowledge.py
│   ├── tools/
│   │   ├── weather.py
│   │   ├── flights.py
│   │   └── mcp_google_search.py
│   ├── memory/
│   │   ├── session_manager.py
│   │   └── memory_bank.py
│   ├── services/
│   │   ├── observability.py
│   │   ├── llm_client.py
│   │   └── evaluation.py
│   └── app.py
│── tests/
│   └── test_basic.py
│── diagrams/
│   └── architecture.png
```

## Installation

```bash
pip install -e .
```

## Run

```bash
python -m travelai.app
```

## License

MIT License
