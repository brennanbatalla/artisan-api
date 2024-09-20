from pydantic import BaseModel


# ====== UpsertChatMessageModel =======

class UpsertChatMessageModel(BaseModel):
    message: str
    context: str