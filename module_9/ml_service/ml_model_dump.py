import joblib
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Сформируем 4 класса для того, чтобы не использовать все 20 лейблов для ускорения тренировки модели
categories = ['comp.sys.mac.hardware', 'sci.crypt', 'soc.religion.christian','talk.religion.misc']

# Сформируем тестовый и тренировочный наборы данных
newsgroup_training = fetch_20newsgroups(subset="train", categories=categories, random_state=42)
newsgroup_testing = fetch_20newsgroups(subset="test", categories=categories, random_state=42)

# Pipeline
model = make_pipeline(
    TfidfVectorizer(),
    MultinomialNB()
)

# Training step
model.fit(newsgroup_training.data, newsgroup_training.target)

# Serialize model and target names
model_file = "./models/newsgroup_model.joblib"
model_targets_tuple = (model, newsgroup_training.target_names)

# dump the model and the target labels with provided model's name
joblib.dump(model_targets_tuple, model_file)
