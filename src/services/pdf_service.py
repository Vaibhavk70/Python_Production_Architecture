from pathlib import Path
import zipfile
from services.ocr_service import OCRService


class PDFService:
    @staticmethod
    def extract_file_from_zip(zip_file_path: str, output_dir: str) -> Path:
        """Extracts files from a ZIP archive and saves them to the specified output directory.

        Args:
            zip_file_path (str): The path to the ZIP file containing the files.
            output_dir (str): The directory where the extracted files will be saved.

        Returns:
            Path: The path to the directory where the extracted files are saved.
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            zip_ref.extractall(output_path)

        return output_path
    
    @staticmethod
    def process_pdf(extract_dir: Path) -> str:
        """Processes a PDF file and extracts text from it.

        Args:
            extract_dir (Path): The directory containing the PDF files to be processed.

        Returns:
            str: The extracted text from the PDF files.
        """
        # Placeholder for PDF text extraction logic
        # You can use libraries like PyPDF2, pdfminer.six, or any OCR library to extract text from the PDF
        
        OCRServiceInstance = OCRService()
        extracted_text = ""

        for pdf_file in extract_dir.glob("*"):
            extracted_text += OCRServiceInstance.extract_text(str(pdf_file)) + "\n"

        return extracted_text