from fastapi import FastAPI

app = FastAPI(title="Data Quality Automation Toolkit")

@app.get("/")
def root():
    return {"message": "DQAT backend is running 🎯"}
