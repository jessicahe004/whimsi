from fastapi import FastAPI, UploadFile, File, HTTPException
import pymupdf
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def extract_text_from_pdf(file: UploadFile):
    try:
        contents = file.file.read()  
        document = pymupdf.open(stream=contents, filetype='pdf')
        all_text = ""
        
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            all_text += page.get_text()

        words = all_text.split()
        chunk_size = 100
        chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

        return chunks
   
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error extracting text from PDF: {str(e)}")

async def generate_prompts_from_text(text_chunks):
    try:
        filtered_strings = []
        for input_string in text_chunks:
            prompt = (
                f"Transform the following text into a concise, evocative art prompt: {input_string}. Emphasize characters, setting, mood, and key actions. Suggest a color palette and composition style. For example, if the text describes a tense scene, the prompt might be 'Paint a dramatic, high-contrast portrait of a troubled character in a dimly lit room.' Keep it short and impactful."
            )
            filtered_text = model.generate_content(prompt)
            filtered_strings.append(filtered_text.candidates[0].content.parts[0].text)
        
        return filtered_strings
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing text: {str(e)}")

@app.get("/")
def read_root():
    return {"Hello World"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        text_chunks = extract_text_from_pdf(file)
        filtered_chunks = await generate_prompts_from_text(text_chunks)  
        return {
            "message": "File processed successfully", 
            "text_chunks": text_chunks,
            "new_prompts": filtered_chunks  
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
