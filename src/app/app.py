from fastapi import FastAPI, HTTPException
from src.pred.torch_pred import torch_run_classifier
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class Img(BaseModel):
    img_url: str


app = FastAPI(title="Image Classifier API")


origins = [
    "http://localhost:3000",
    "localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def read_main():
    return {"msg": "Hello cox.it !"}

print("HERE WE GO 5")

@app.post("/predict/torch_model/", status_code=200)
async def predict_torch(request: Img):
    prediction = torch_run_classifier(request.img_url)
    if not prediction:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail="Image could not be downloaded"
        )

    return {"status_code": 200,
            "predicted_label": prediction[0],
            "probability": prediction[1]}

