from auth import auth_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
import logging
import time

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)


app.include_router(auth_router)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# we should add it to track the logging of http requests 
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    logger.info(f"📥 Received request: {request.method} {request.url}")

    response = await call_next(request)

    process_time = time.time() - start_time
    logger.info(f"✅ Response sent: {response.status_code} {request.url} (Time: {process_time:.2f}s)")

    return response

@app.get("/")
def read_root():
    return {"message": "Ethereum Auth API is Running"}
