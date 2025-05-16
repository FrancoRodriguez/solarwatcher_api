from fastapi import APIRouter, Depends

from app.auth.jwt import get_current_user
from app.services.nasa import fetch_nasa_events
from app.services.serializer import summary_serializer

router = APIRouter()


@router.get("/summary")
async def get_stats_summary(user=Depends(get_current_user)):
    events = await fetch_nasa_events()

    speeds = []
    critical_count = 0

    for event in events:
        for analysis in event.get("cmeAnalyses", []):
            speed = analysis.get("speed")
            if speed:
                speeds.append(speed)
                if speed > 800:
                    critical_count += 1

    return summary_serializer(events, critical_count, speeds)
