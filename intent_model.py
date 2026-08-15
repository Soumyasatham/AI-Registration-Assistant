import json
import nltk
import re

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Download NLTK resources
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")


class IntentClassifier:

    def __init__(self):

        self.lemmatizer = WordNetLemmatizer()

        self.stop_words = set(
            stopwords.words("english")
        )

        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), analyzer="word", sublinear_tf=True)

        self.model = LogisticRegression(max_iter=1000)

        self.train_model()


    # -------------------------
    # TEXT PREPROCESSING
    # -------------------------

    def preprocess(self, text):

        text = text.lower()

        # Keep only letters and spaces
        text = re.sub(r"[^a-zA-Z\s]", "", text)

        tokens = nltk.word_tokenize(text)

        # Lemmatize but DO NOT remove stopwords
        tokens = [
            self.lemmatizer.lemmatize(word)
            for word in tokens
        ]

        return " ".join(tokens)


    # -------------------------
    # LOAD TRAINING DATA
    # -------------------------

    def load_data(self):

        with open(
            "intents.json",
            "r"
        ) as file:

            intents = json.load(file)

        texts = []

        labels = []

        for intent, patterns in intents.items():

            for pattern in patterns:

                processed_text = self.preprocess(
                    pattern
                )

                texts.append(
                    processed_text
                )

                labels.append(
                    intent
                )

        return texts, labels


    # -------------------------
    # TRAIN MODEL
    # -------------------------

    def train_model(self):

        texts, labels = self.load_data()

        X = self.vectorizer.fit_transform(
            texts
        )

        self.model.fit(
            X,
            labels
        )

        print("Intent model trained successfully!")


    # -------------------------
    # PREDICT INTENT
    # -------------------------

    def predict_intent(self, text):

        processed_text = self.preprocess(text)

        X = self.vectorizer.transform([processed_text])

        if X.nnz == 0:
            return "unknown", 0.0

        prediction = self.model.predict(X)

        probabilities = self.model.predict_proba(X)

        confidence = max(probabilities[0])

        if confidence < 0.30:
            return "unknown", confidence

        return prediction[0], confidence

if __name__ == "__main__":

    classifier = IntentClassifier()

    while True:

        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit"]:

            print("Exiting...")
            break

        intent, confidence = classifier.predict_intent(user_input)

        print("Predicted Intent:", intent)

        print("Confidence:",round(confidence * 100, 2),"%")