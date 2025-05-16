import os
from datetime import date, timedelta

import httpx

NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")
BASE_URL = "https://api.nasa.gov/DONKI/"


async def fetch_nasa_events():
    today = date.today()
    start_date = today - timedelta(days=7)

    url = f"{BASE_URL}CME?startDate={start_date}&endDate={today}&api_key={NASA_API_KEY}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()
