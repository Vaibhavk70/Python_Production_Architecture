from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from services.LLM_service import generate_response
from services.ocr_service import OCRService
from services.pdf_service import PDFService

from dotenv import load_dotenv
import os

router = APIRouter()

load_dotenv()
UPLOAD_DIR = os.getenv("UPLOAD_DIR")
EXTRACTED_DIR = os.getenv("EXTRACTED_DIR")

@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    """Endpoint to handle file uploads and extract text using OCRService."""
    try:
        os.makedirs(UPLOAD_DIR, exist_ok=True)
        file_location = f"{UPLOAD_DIR}/{file.filename}"

        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())
            
        if file.filename.split(".")[-1].lower() == "zip":
            # Extract PDF files from the ZIP archive
            os.makedirs(EXTRACTED_DIR, exist_ok=True)

            extracted_path = PDFService.extract_file_from_zip(file_location, EXTRACTED_DIR)       # Extract files from the ZIP archive

            extracted_text = PDFService.process_pdf(extracted_path)      # Process the extracted PDF files and extract text

            llm_response = generate_response(extracted_text)      # Generate response using the extracted text

            return JSONResponse(
                content={
                    "status_code": 200,
                    "message": f"ZIP file processed successfully: {file.filename}",
                    "extracted_text": extracted_text,
                    "llm_response": llm_response
                }
            )
            
        else:

            OCRServiceInstance = OCRService()
            extracted_text = OCRServiceInstance.extract_text(file_location)

            llm_response = generate_response(extracted_text)

            # print(f"Extracted text from {file.filename}:\n{extracted_text}")        
            return JSONResponse(
                content={
                    "status_code": 200,
                    "message": f"File uploaded successfully: {file.filename}",
                    "extracted_text": extracted_text,
                    "llm_response": llm_response
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

