from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from utils import verify_signature

auth_router = APIRouter()

class AuthRequest(BaseModel):
    wallet_address: str
    signed_message: str

@auth_router.post("/verify")
def verify_wallet_auth(data: AuthRequest):
    if not verify_signature(data.wallet_address, data.signed_message):
        raise HTTPException(status_code=401, detail="Invalid signature")
    return {"message": "Authentication successful", "wallet_address": data.wallet_address}
