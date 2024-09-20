from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from app.shared.models import PyObjectId


# ======= Chat Collection ===============

class BaseMessage(BaseModel):
    message: str
    response: str
    quickOptions: List[str]
    createdAt: datetime
    context: str


class MessageModel(BaseModel):
    id: str
    createdAt: datetime
    edits: List[BaseMessage]


class ChatCollection(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    messages: List[MessageModel]
    createdAt: datetime

