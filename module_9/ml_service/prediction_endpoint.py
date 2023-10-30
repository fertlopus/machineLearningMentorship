from fastapi import FastAPI, Depends
import joblib
from sklearn.pipeline import Pipeline
from fastapi import HTTPException
from pydantic import BaseModel
import contextlib


class PredictionInput(BaseModel):
    text: str

class PredictionOutput(BaseModel):
    category: str

class NewsGroupModel:
    def __init__(self):
        self.model = None
        self.targets = None

    def load_model(self):
        model_file = "./models/newsgroup_model.joblib"  # Adjust the path to your model file
        loaded_model = joblib.load(model_file)
        model, targets = loaded_model
        self.model = model
        self.targets = targets

    def predict(self, input: PredictionInput) -> PredictionOutput:
        if not self.model or not self.targets:
            raise RuntimeError("Model files are not found!")
        prediction = self.model.predict([input.text])
        category = self.targets[prediction[0]]
        return PredictionOutput(category=category)


newsgroup_model = NewsGroupModel()


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    newsgroup_model.load_model()
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/prediction", response_model=PredictionOutput)
async def get_prediction(input: PredictionInput):
    output = newsgroup_model.predict(input)
    return output