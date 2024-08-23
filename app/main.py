# app/main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import base64

from services.text_processing import extract_text_from_pdf, generate_prompts_from_text
from services.image_generation import query

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello World"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        text_chunks = extract_text_from_pdf(file)
        filtered_chunks = await generate_prompts_from_text(text_chunks)  

        images = []
        for prompt in filtered_chunks:
            image_data = query(prompt) 
            image_base64 = base64.b64encode(image_data).decode('utf-8')
            images.append(f"data:image/png;base64,{image_base64}")

        return {
            "message": "File processed successfully",
            "text_chunks": text_chunks,
            "new_prompts": filtered_chunks,
            "images": images
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
