import os
import joblib
from sklearn.pipeline import make_pipeline, Pipeline

# model path
model_file = os.path.join(os.path.dirname(__file__), "./models/newsgroup_model.joblib")
# loaded model
loaded_model: tuple[Pipeline, list[str]] = joblib.load(model_file)

# unpack the loaded pack
model, targets = loaded_model

# Run a prediction
prediction = model.predict(["computer cpu memory ram gpu"])
print(targets[prediction[0]])
