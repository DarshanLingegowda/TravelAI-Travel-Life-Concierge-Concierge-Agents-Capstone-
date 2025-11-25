from fastapi import FastAPI
from travelai.services.planning_service import PlanningService

app = FastAPI()
planner = PlanningService()

@app.get("/")
async def home():
    return {"message": "TravelAI is running!"}

@app.post("/plan")
async def plan_trip(query: str):
    result = await planner.generate_plan(query)
    return {"response": result}

