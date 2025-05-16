from fastapi import APIRouter, Depends

from app.auth.jwt import get_current_user

router = APIRouter()


@router.get("/")
def secure_endpoint(user: str = Depends(get_current_user)):
    return {"message": f"Hello, {user}"}
