from travelai.agents.travel_agent import TravelAgent

class PlanningService:
    def __init__(self):
        self.agent = TravelAgent()

    async def generate_plan(self, query: str):
        return await self.agent.run(query)

