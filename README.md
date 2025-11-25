# TravelAI — Travel & Life Concierge (Concierge Agents Capstone)


**Track:** Concierge Agents


## Overview
TravelAI is a multi-agent personal concierge that helps users plan short trips and daily itineraries, combining web research, cost estimation, and personalized recommendations. It demonstrates multiple agent patterns from the Agents Intensive course: planner, researcher, scheduler, writer, and evaluator.


## Project Pitch
**Problem:** Planning short trips and daily itineraries is time-consuming and error-prone.


**Solution:** A multi-agent personal concierge that: (1) researches destinations and activities, (2) builds an itinerary and cost estimate, (3) outputs a user-ready itinerary and packing checklist, and (4) self-evaluates and iterates.


**Value:** Automates repetitive planning steps, saves hours of research, and generates consistently structured itineraries.


## Features Demonstrated
- Multi-agent system (Planner, Researcher, Scheduler, Writer, Evaluator)
- Agent tools (web search mock, calculator, file writer)
- Memory (simple vector store or Pinecone optional)
- Sessions & state (simple session id for continuity)
- Observability (JSON logs of agent steps)
- Agent evaluation (LLM-based rubric)
- Kaggle submission generator (CSV with `id,response`)


## Quickstart
1. Copy `.env.example` to `.env` and set `OPENAI_API_KEY`. Optionally enable Pinecone.
2. Create virtual environment and install:
```bash
pip install -r requirements.txt
