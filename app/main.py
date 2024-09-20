from dotenv import load_dotenv
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from app.modules.mongodb import lifespan

load_dotenv()

# import routers
from app.chats.chats_router import router as chat_router

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# imports routes
router = APIRouter(lifespan=lifespan)
router.include_router(router=chat_router, tags=["Chats"])

app.include_router(router=router)