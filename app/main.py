from fastapi import FastAPI, UploadFile, File, HTTPException
import pymupdf
from pathlib import Path
import tempfile

app = FastAPI()

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


@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/upload")
async def upload_file():
    tester_path = Path(__file__).parent / "tester.pdf"  

    with open(tester_path, "rb") as f:
        contents = f.read()

        with tempfile.SpooledTemporaryFile() as temp_file:
            temp_file.write(contents)
            temp_file.seek(0) 

            file = UploadFile(temp_file, filename="tester.pdf")
            text_chunks = extract_text_from_pdf(file)

    return {"text_chunks": text_chunks}
