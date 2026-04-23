from fastapi import FastAPI
from routes.task import router as task_router

app = FastAPI(title="Task API", version="1.0.0")
app.include_router(task_router)