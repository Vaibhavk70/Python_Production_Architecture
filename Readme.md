
# Production Achitecture

Aim to developed this project is to understand production-ready document processing pipeline using FastAPI, Celery (For Worker Manage), and Redis(For Queues). In this we can see how the perticular task execute very smothly without getting down the project. We will see whole end-to-end project pipeline with industrialized folder structure.

The system processes uploaded PDF or ZIP files, extracts text using OCR, sends the extracted text to an LLM for structured data extraction, and generates Excel reports.


---

## Features
- PDF Upload
- ZIP Upload Support
- OCR Text Extraction
- LLM-Based Data Extraction
- Excel Generation
- Background Processing with Celery
- Redis Task Queue
- Job Tracking
- Scalable Worker Architecture

---

## Architecture

```text
                FastAPI
                    │
                    ▼
              Create Job ID
                    │
                    ▼
                Redis Queue
                    │
     ┌──────────────┼──────────────┐
     ▼              ▼              ▼

 OCR Queue      LLM Queue      Excel Queue
     │              │               │

 OCR Worker    LLM Worker    Excel Worker
     │              │               │
     └──────────────┼───────────────┘
                    │
                    ▼
                Final Excel
```

---

## Project Structure

```text
src/

├── app/
|    ├──routes/
|    |    └── file_upload.py
|    └── main.py
│
├── celery_app/
│   └── celery_config.py
|
├── config/
│   └── setting.py
|
├── llm/
|   ├── chain.py
│   ├── prompt.py
│   └── schema.py
│
├── services/
│   ├── ocr_service.py
│   ├── pdf_service.py
│   └── llm_service.py

│
├── repositories/
│   └── job_repository.py
│
├── models/
│   └── job.py
│
├── .gitignore
│
├── docker-compose.yml
│
├── Dockerfile
│
├── requirements.txt
│
└── README.md
```

---

## Workflow

### Step 1

Upload PDF or ZIP file.

### Step 2

Create a unique Job ID.

### Step 3

Store processing task in Redis Queue.

### Step 4

OCR Worker extracts text.

### Step 5

LLM Worker extracts structured information.

### Step 6

Excel Worker generates final report.

### Step 7

Update Job Status.

---

## Job Status Flow

```text
PENDING
    ↓
OCR_PROCESSING
    ↓
LLM_PROCESSING
    ↓
EXCEL_GENERATION
    ↓
COMPLETED
```

---

## Tech Stack

| Component    | Technology            |
| ------------ | --------------------- |
| API          | FastAPI               |
| Queue        | Redis                 |
| Worker       | Celery                |
| OCR          | PaddleOCR / Tesseract |
| LLM          | OpenAI / Ollama       |
| Database     | PostgreSQL            |
| File Storage | Local Storage         |
| Deployment   | Docker                |

---

## Installation

Clone repository:

```bash
git clone <repository-url>
```

Move into project:

```bash
cd src
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create `.env`

```env
groq_api_key=your_api_key

REDIS_HOST=localhost
REDIS_PORT=6379

```

---

## Start Redis

Using Docker:

```bash
docker run -p 6379:6379 redis
```

---

## Run FastAPI

```bash
uvicorn app.main:app --reload
```

---

## Run Celery Workers

OCR Worker:

```bash
celery -A celery_app worker -Q ocr_queue --concurrency=4
```

LLM Worker:

```bash
celery -A celery_app worker -Q llm_queue --concurrency=2
```

Excel Worker:

```bash
celery -A celery_app worker -Q excel_queue --concurrency=1
```

---

## API Endpoints

### Upload File

```http
POST /uploadfile
```

Request:

```text
multipart/form-data
```

Response:

```json
{
  "job_id": "abc123",
  "status": "PENDING"
}
```

---

### Get Job Status

```http
GET /jobs/{job_id}
```

Response:

```json
{
  "job_id": "abc123",
  "status": "LLM_PROCESSING"
}
```

---

## Future Improvements

* Kubernetes Deployment
* Worker Autoscaling
* RabbitMQ Support
* S3 File Storage
* Multi-Tenant Processing
* Monitoring Dashboard
* Retry Mechanism
* Distributed Processing

---

## Author

Vaibhav Kharat

Python Developer | AI Engineer | FastAPI | LLM | RAG | OCR | Distributed Systems
