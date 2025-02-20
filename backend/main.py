from typing import Union
from fastapi import FastAPI
import httpx
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("videos/{video_id}")
def get_video(video_id: int):

    video_url = f"https://www.youtube.com/watch?v={video_id}"    
    if not video_id:
        return {"error": "video_id is required"}
    
    async def video_stream():
        async with httpx.AsyncClient() as client:
            r = await client.get(video_url)
            yield r.content
    return 