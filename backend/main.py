from fastapi import FastAPI

app = FastAPI(
    title="ARES-SOC API",
    description="Backend API for the ARES-SOC AI Analyst project",
    version="1.0.0",
)

@app.get("/")
def home():
    return {"message": "ARES-SOC backend is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
