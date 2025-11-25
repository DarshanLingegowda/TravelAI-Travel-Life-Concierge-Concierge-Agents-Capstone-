from openai import OpenAI
from travelai.settings import OPENAI_API_KEY, MODEL
from travelai.agents.base_agent import BaseAgent

client = OpenAI(api_key=OPENAI_API_KEY)

class TravelAgent(BaseAgent):
    async def run(self, query: str) -> str:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are TravelAI, an expert travel planning assistant."},
                {"role": "user", "content": query}
            ]
        )
        return response.choices[0].message["content"]

