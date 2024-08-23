# app/services/text_processing.py
import pymupdf
from fastapi import UploadFile, HTTPException
from .config import configure_model

model = configure_model()

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
                f"Transform the following text: {input_string} into a concise, evocative art prompt focusing on environmental scenes. Emphasize natural landscapes, abstract forms, and symbolic elements. You can include animals and structures like houses, but avoid any human characters. Suggest a color palette and composition style that reflects the mood and setting described in the text."
            )
            filtered_text = model.generate_content(prompt)
            filtered_strings.append(filtered_text.candidates[0].content.parts[0].text)
        
        return filtered_strings
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing text: {str(e)}")
