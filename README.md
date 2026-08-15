# AI Registration Assistant 🤖

An intelligent conversational AI chatbot designed to guide students through the registration process for an AI & Data Science Internship.

The project uses Natural Language Processing (NLP), Machine Learning, and Flask to understand user queries, manage the registration conversation, validate user information, and store completed registrations.

## 🚀 Features

- 🤖 AI-powered chatbot
- 🧠 Machine Learning-based intent classification
- 📝 Internship registration workflow
- 👤 Name validation
- 📧 Email extraction and validation
- 🎓 Field of study collection
- 💻 Programming experience collection
- ✅ Registration confirmation
- 💾 JSON-based registration storage
- 🌐 Flask web interface
- 📊 Admin dashboard to view registrations
- ❓ FAQ and help handling

## 🛠️ Technologies Used

- Python
- Flask
- NLTK
- Scikit-learn
- TF-IDF Vectorizer
- Multinomial Naive Bayes
- HTML
- CSS
- JSON

## 📂 Project Structure

```text
AI-Registration-Assistant/
│
├── app.py
├── chatbot.py
├── intent_model.py
├── intents.json
├── requirements.txt
├── .gitignore
│
├── static/
│   └── style.css
│
└── templates/
    ├── index.html
    └── admin.html
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Soumyasatham/AI-Registration-Assistant.git
```

### 2. Navigate to the project folder

```bash
cd AI-Registration-Assistant
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

## 🌐 Usage

After running the application, open your browser and visit:

```text
http://127.0.0.1:5000
```

You can:

1. Ask questions about the internship.
2. Type `register` to begin registration.
3. Enter your name.
4. Enter a valid email address.
5. Enter your field of study.
6. Enter your programming experience.
7. Confirm registration using `YES`.

Completed registrations are stored locally in a JSON file.

## 🧠 AI and NLP Implementation

The chatbot uses a hybrid conversational AI approach:

- **Rule-based logic** for the structured registration flow.
- **NLTK** for text preprocessing, tokenization, stop-word removal, and lemmatization.
- **TF-IDF Vectorization** for converting text into numerical features.
- **Multinomial Naive Bayes** for intent classification.
- **Confidence-based handling** for unknown or unsupported queries.

## 📊 Supported Intents

The chatbot can recognize:

- Greeting
- Registration
- Internship Information
- Help
- Thank You
- Goodbye
- Unknown Queries

## 🔮 Future Improvements

- Multi-language support
- Sentiment analysis
- Database integration
- User authentication
- Improved intent classification using Transformers or BERT
- Analytics dashboard
- Cloud deployment

## 👩‍💻 Author

**Soumyaa Satham**

Final Year Electronics and Telecommunication Engineering Student

---

This project was developed as part of an **AI & Data Science Internship**.
