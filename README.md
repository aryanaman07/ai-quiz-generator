# 🎓 AI Quiz Generator using Gemini API

An interactive web application that generates multiple-choice quizzes for students (Classes 4 to 8) using Google’s Gemini AI. Built with Streamlit, this tool makes learning fun and dynamic by tailoring questions based on grade, subject, topic, and difficulty.

## 🌟 Features

- ✅ Generates 3 unique MCQs on every quiz generation
- 🧠 Smart difficulty selector: Easy, Medium, Hard
- 🎯 Covers subjects like Math, Science, English, Social Studies & Computer Science
- 🎒 Designed for students of Class 4 to Class 8 (age group 10–14)
- 🚀 Instant quiz interface with real-time evaluation
- 📊 Displays final score with detailed feedback

---

## 🛠️ Tech Stack

- **Frontend & UI:** Streamlit
- **Backend:** Google Gemini Flash 2.0 API
- **Language:** Python
- **Libraries:** `google-generativeai`, `streamlit`, `dotenv`, `json`, `re`

---

## 📁 Folder Structure

```
ai-quiz-generator/
├── app.py               # Main Streamlit application
├── .env                 # API key 
├── .gitignore           # Specifies files to ignore
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation (this file)
```


## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/aryanaman07/ai-quiz-generator.git
cd ai-quiz-generator
```

### 2. (Optional) Set Up Virtual Environment

```bash
python -m venv venv
# Activate:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API

Create a `.env` file in the root directory and add your API key:

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

## ▶️ Run the App

```bash
streamlit run app.py
```

The application will open in your default browser.

---

## 📸 Screenshots


![Screenshot 2025-04-15 103538](https://github.com/user-attachments/assets/15547588-d6d9-4c9e-a35b-5e332dfa403d)
![Screenshot 2025-04-15 103318](https://github.com/user-attachments/assets/e64a208d-329e-42b6-814c-a85abb0e9109)
![Screenshot 2025-04-15 103452](https://github.com/user-attachments/assets/a0e14243-354f-4833-86f0-5d650326729a)
![Screenshot 2025-04-15 103258](https://github.com/user-attachments/assets/1e1a268e-f5fc-491f-8eed-8d99cefd6d4f)


---

## 📦 Dependencies

List of key dependencies:

- `streamlit`
- `google-generativeai`
- `python-dotenv`

Install all via:

```bash
pip install -r requirements.txt
```

---

## 🧪 Sample Use

1. Select Grade: `Class 6`
2. Select Subject: `Mathematics`
3. Choose Topic: `Basic Algebra`
4. Choose Difficulty: `Medium`
5. Click on "🚀 Generate Quiz"
6. Answer all MCQs and click "✅ Submit Answers"
7. View your score and correct answers

---

## 💡 Future Enhancements

- 📚 Explanation for correct answers
- ⏳ Timed quizzes with leaderboards
- 📈 Progress tracking for students
- 🌍 Deploy on Streamlit Cloud / HuggingFace Spaces
- 🧑‍🤝‍🧑 Multiplayer modes: 1v1, classroom battles, etc.

---

## 🤝 Contributing

Contributions, feedback, and ideas are welcome!  
Fork this repository, create a branch, and submit a pull request.

---

## 📄 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute it with attribution.

---

## 🙋‍♂️ Author

**Aryan Aman**  
👨‍🎓 B.Tech CSE (Data Science), TMSL Kolkata
📫 Connect with me:  
- [LinkedIn](https://www.linkedin.com/in/aryan-aman-b3334b270/)  
- [GitHub](https://github.com/aryanaman07)

---

## 💬 Feedback

Have suggestions or improvements? Feel free to open an issue or message me directly. Let's make learning more engaging for students together!
```
