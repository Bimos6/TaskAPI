from fastapi import FastAPI

app = FastAPI(
    title="Task API",
    description="Мини API для списка задач",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Task API работает", "status": "ok"}