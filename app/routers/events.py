from fastapi import APIRouter, Depends

from app.auth.jwt import get_current_user
from app.services.filters import filter_event
from app.services.nasa import fetch_nasa_events
from app.services.serializer import default_serializer

router = APIRouter()


@router.get("/recent")
async def recent_events(user=Depends(get_current_user)):
    event_list = await fetch_nasa_events()
    filtered_events = [filter_event(event) for event in event_list]
    return default_serializer(filtered_events)


@router.get("/critical")
async def get_critical_events(user=Depends(get_current_user)):
    events_list = await fetch_nasa_events()
    critical_events = []
    for event in events_list:
        cme_analyses = event.get("cmeAnalyses", [])
        for analysis in cme_analyses:
            if analysis.get("speed", 0) > 800:
                critical_events.append(filter_event(event))
                break
    return default_serializer(critical_events)
