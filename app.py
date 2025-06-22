import streamlit as st
import json
import os
import re
import random
import time
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("AIzaSyDU-6KInbvEYJddNdfYk4rm5p3MVwgJbG0"))

# Initialize Gemini Flash model
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")

TOPICS = {
    "Class 4": {
        "Mathematics": ["Addition and Subtraction", "Shapes and Patterns", "Time", "Measurement"],
        "Science": ["Plants and Their Functions", "Our Body", "Air and Water", "Animals and Their Habitats"],
        "English": ["Nouns and Pronouns", "Verbs", "Story Comprehension"],
        "Social Studies": ["Our Country", "Maps and Globes", "Community Helpers"],
        "Computer Science": ["Parts of Computer", "Input and Output Devices"]
    },
    "Class 5": {
        "Mathematics": ["Decimals", "Fractions", "Volume", "Area"],
        "Science": ["Force and Energy", "Water Cycle", "Safety and First Aid"],
        "English": ["Tenses", "Synonyms and Antonyms", "Comprehension"],
        "Social Studies": ["India's Natural Resources", "Great Leaders"],
        "Computer Science": ["Internet", "Computer Storage Devices"]
    },
    "Class 6": {
        "Mathematics": ["Integers", "Basic Algebra", "Geometry"],
        "Science": ["Separation of Substances", "The Living World", "Electricity"],
        "English": ["Sentence Types", "Paragraph Writing", "Reading Skills"],
        "Social Studies": ["Early Humans", "Indian Government Structure"],
        "Computer Science": ["Spreadsheet Basics", "Email and Internet Safety"]
    },
    "Class 7": {
        "Mathematics": ["Linear Equations", "Ratios and Proportion", "Data Handling"],
        "Science": ["Heat and Temperature", "Respiration in Organisms", "Motion and Time"],
        "English": ["Active & Passive Voice", "Formal Letters", "Idioms"],
        "Social Studies": ["Medieval India", "Environment and Society"],
        "Computer Science": ["Scratch Programming", "MS Excel"]
    },
    "Class 8": {
        "Mathematics": ["Quadrilaterals", "Exponents and Powers", "Mensuration"],
        "Science": ["Combustion and Flame", "Cell Structure", "Friction"],
        "English": ["Direct & Indirect Speech", "Essay Writing"],
        "Social Studies": ["Indian Constitution", "Colonialism"],
        "Computer Science": ["HTML Basics", "Algorithms and Flowcharts"]
    }
}

#@st.cache_data
def fetch_questions(grade, subject, topic, quiz_level):
    RESPONSE_JSON = {
        "mcqs": [
            {
                "mcq": "multiple choice question1",
                "options": {
                    "a": "choice here1",
                    "b": "choice here2",
                    "c": "choice here3",
                    "d": "choice here4",
                },
                "correct": "a",
            }
        ]
    }

    seed = random.randint(1000, 9999) 
    prompt = f"""
You are an educational content generator AI specialized in creating quizzes for school students.

Generate a quiz for:
- Grade: {grade}
- Subject: {subject}
- Topic: {topic}
- Difficulty Level: {quiz_level}

Generate exactly 3 unique multiple-choice questions (MCQs). Avoid repeating questions from earlier generations.

Use this seed to ensure variety: {seed}

Return the result ONLY in the following JSON format (no explanation):

Example:
{json.dumps(RESPONSE_JSON, indent=2)}
"""

    try:
        response = model.generate_content(prompt,generation_config={"temperature":0.9})
        raw_text = response.text.strip()

        match = re.search(r'\{[\s\S]*\}', raw_text)
        if not match:
            st.error("❌ Couldn't find valid JSON in Gemini's response.")
            return []

        cleaned_json = match.group(0)
        parsed = json.loads(cleaned_json)

        if "mcqs" not in parsed or not isinstance(parsed["mcqs"], list):
            st.error("❌ Unexpected JSON format.")
            return []

        return parsed["mcqs"]
    except json.JSONDecodeError:
        st.error("❌ Failed to parse JSON. Please regenerate.")
        return []
    except Exception as e:
        st.error(f"❌ Gemini API Error: {str(e)}")
        return []

def main():
    st.title("🎓 AI Quiz Generator (Grade & Subject Smart Mode)")

    grade = st.selectbox("🎒 Select Grade:", list(TOPICS.keys()))
    subject = st.selectbox("📘 Select Subject:", list(TOPICS[grade].keys()))
    topic = st.selectbox("📚 Select Topic:", TOPICS[grade][subject])
    quiz_level = st.selectbox("🧠 Select Difficulty:", ["Easy", "Medium", "Hard"]).lower()

    if 'questions' not in st.session_state:
        st.session_state.questions = []
    if 'selected_options' not in st.session_state:
        st.session_state.selected_options = [None] * 3
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False

    if st.button("🚀 Generate Quiz"):
        st.session_state.questions = fetch_questions(grade, subject, topic, quiz_level)
        st.session_state.selected_options = [None] * len(st.session_state.questions)
        st.session_state.submitted = False

    if st.session_state.questions:
        st.header("📝 Quiz Questions")

        for idx, question in enumerate(st.session_state.questions):
            options = question["options"]
            labels = [f"{k.upper()}: {v}" for k, v in options.items()]
            key_list = list(options.keys())
            value_list = list(options.values())

            selected_value = st.session_state.selected_options[idx]
            if selected_value in key_list:
                default_index = key_list.index(selected_value)
            else:
                default_index = None

            placeholder = "Select an option"
            display_labels = [placeholder] + labels
            selected_label = st.radio(
                f"Q{idx+1}: {question['mcq']}",
                display_labels,
                index=key_list.index(selected_value) + 1 if selected_value in key_list else 0,
                key=f"q{idx}"
            )
            if selected_label != placeholder:
                selected_key = selected_label.split(":")[0].strip().lower()
                st.session_state.selected_options[idx] = selected_key
            else:
                st.session_state.selected_options[idx] = None

        if st.button("✅ Submit Answers"):
            if None in st.session_state.selected_options:
                st.warning("⚠️ Please answer all questions before submitting.")
            else:
                st.session_state.submitted = True

    if st.session_state.submitted:
        st.header("📊 Quiz Result")
        marks = 0
        for i, question in enumerate(st.session_state.questions):
            selected_key = st.session_state.selected_options[i]
            correct_key = question["correct"]
            correct_answer = question["options"][correct_key]
            selected_answer = question["options"].get(selected_key, "Not Selected")

            st.subheader(f"Q{i+1}: {question['mcq']}")
            st.write(f"Your Answer: {selected_answer}")
            st.write(f"Correct Answer: {correct_answer}")

            if selected_key == correct_key:
                marks += 1

        st.success(f"🎉 You scored {marks} out of {len(st.session_state.questions)}")

if __name__ == "__main__":
    main()
