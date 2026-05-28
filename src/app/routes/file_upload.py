from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from services.ocr_service import OCRService
from dotenv import load_dotenv
import os

router = APIRouter()

load_dotenv()
UPLOAD_DIR = os.getenv("UPLOAD_DIR")

@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    """Endpoint to handle file uploads and extract text using OCRService."""
    try:
        os.makedirs(UPLOAD_DIR, exist_ok=True)
        file_location = f"{UPLOAD_DIR}/{file.filename}"

        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())

        OCRServiceInstance = OCRService()
        extracted_text = OCRServiceInstance.extract_text(file_location)

        # print(f"Extracted text from {file.filename}:\n{extracted_text}")        
        return JSONResponse(
            content={
                "status_code": 200,
                "message": f"File uploaded successfully: {file.filename}",
                "extracted_text": extracted_text
            }
        )
    
    except Exception as e:
        print(f"Error occurred while processing the file {file.filename}: {e}")
        return JSONResponse(
            status_code=500,
            content={
                "status_code": 500,
                "message": f"An error occurred while processing the file: {e}"
            }
        )

