from pydantic import BaseModel


# ====== PostChatMessageModel =======

class PostChatMessageModel(BaseModel):
    message: str
    context: str
    chatId: str