from fastapi import FastAPI

from app.routers import auth, events, root, stats

app = FastAPI()

app.include_router(auth.router, tags=["Auth"])
app.include_router(root.router, tags=["Root"])
app.include_router(events.router, prefix="/events", tags=["Events"])
app.include_router(stats.router, prefix="/status", tags=["Stats"])
