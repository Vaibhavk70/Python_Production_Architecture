from docling.document_converter import DocumentConverter
from dotenv import load_dotenv
import os

load_dotenv()

class OCRService:
    def __init__(self):
        self.api_key = os.getenv("OCR_API_KEY")
        self.convertor = DocumentConverter()
        
    def extract_text(self, file_path):
        """Extract text from the given file using Docling OCR."""
        try:
            extracted_text = self.convertor.convert(file_path)
            markdown_text = extracted_text.document.export_to_markdown()
            return markdown_text
        except Exception as e:
            print(f"Error occurred while extracting text from {file_path}: {e}")
            return None

