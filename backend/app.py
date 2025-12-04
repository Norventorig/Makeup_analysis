from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from model.core import model_handler
from pathlib import Path
from PIL import Image
import io

PROJECT_ROOT = Path(__file__).resolve().parents[1]


app = FastAPI(title="Image Classifier API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=PROJECT_ROOT / "frontend"), name="static")


@app.post("/api/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    prediction = model_handler.predict(image)
    return {"success": True, "result": {"prediction": prediction}}


@app.get("/")
async def index():
    return FileResponse(PROJECT_ROOT / "frontend" / "index.html")
