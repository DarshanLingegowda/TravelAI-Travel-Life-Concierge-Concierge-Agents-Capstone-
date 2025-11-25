import httpx

class WeatherTool:
    async def get_weather(self, city: str) -> str:
        return f"Weather data unavailable in demo mode for: {city}"

