from fastapi import FastAPI, APIRouter

from app.routes import file_upload

app = FastAPI(
    title="OCR Service API",
    description="API for uploading files and extracting text using OCRService.",
)

api_router = APIRouter(prefix="/Python_architechture")


api_router.include_router(file_upload.router, tags=["Docling OCR"])

app.include_router(api_router)
