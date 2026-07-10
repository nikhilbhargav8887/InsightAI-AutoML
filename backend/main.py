from fastapi import FastAPI
from backend.api.upload import router as upload_router
from backend.api.datasets import router as datasets_router
from backend.api.clean import router as clean_router
from backend.api.analyze import router as analyze_router
from backend.api.train import router as train_router




app = FastAPI(
    title="Insight AutoML",
    
)

app.include_router(analyze_router)
app.include_router(upload_router)
app.include_router(datasets_router)
app.include_router(clean_router)
app.include_router(train_router)




@app.get("/")
def home():
    return {
        "message": "Welcome to the Insight AutoML API. Use the available endpoints to upload datasets, clean data, analyze features, train models"
    }