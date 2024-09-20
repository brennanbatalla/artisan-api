import time
import uuid
from typing import List

from bson import ObjectId
from fastapi import APIRouter, Request, HTTPException

from app.chats.chat_model import ChatCollection, MessageModel, BaseMessage
from app.chats.schemas import PostChatMessageModel
from app.services.openai_service import get_chat_response

router = APIRouter()


@router.get("/chats", response_model=List[ChatCollection])
async def get_chats(request: Request):
    return await request.app.mongodb.chats.find().to_list()


@router.post("/chats", response_model=ChatCollection)
async def get_chats(request: Request):
    res = await request.app.mongodb.chats.insert_one({
        "messages": [],
        "createdAt": time.time()
    })
    print(res)
    if res.inserted_id:
        return await request.app.mongodb.chats.find_one({"_id": res.inserted_id})
    raise HTTPException(status_code=500, detail="Failed to create item")


@router.post("/chats/{chat_id}/messages")
async def post_chat_message(request: Request, chat_id: str, message: PostChatMessageModel):
    message_dict = message.model_dump()
    message_dict["createdAt"] = time.time()  # Automatically set the creation date

    ai_response = await get_chat_response(message.message, message.context)
    print(ai_response)
    message_dict["response"] = ai_response['response']
    message_dict["quickOptions"] = ai_response['quickOptions']

    new_message = MessageModel(
        id=str(uuid.uuid4()),
        createdAt=time.time(),
        edits=[BaseMessage(**message_dict)]
    ).model_dump(by_alias=True)

    # Update the chat document by pushing the new message to the messages array
    result = await request.app.mongodb.chats.update_one(
        {"_id": ObjectId(chat_id)},
        {"$push": {"messages": new_message}}
    )

    print(result)

    return new_message


@router.patch("/chats/{chat_id}/message/{message_id}")
async def get_chats():
    return {"chats": "chats"}
