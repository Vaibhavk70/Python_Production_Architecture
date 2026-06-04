from celery import Celery
from kombu import Exchange, Queue

celery_app = Celery(
    "documnt_processor",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)

celery_app.conf.task_queues = (
    Queue("ocr_queue"),
    Queue("llm_queue"),
    Queue("excel_queue"),
)

celery_app.conf.task_routes = {
    "services.ocr_service.*": {"queue": "ocr_queue"},
    "services.llm_service.*": {"queue": "llm_queue"},
    "services.excel_service.*": {"queue": "excel_queue"},
}


