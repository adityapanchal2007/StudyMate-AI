import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

MODEL = os.getenv("OPENAI_MODEL")

# AI Response Function
def get_ai_response(prompt):
    try:
        response = client.responses.create(
            model=MODEL,
            input=prompt
        )

        return response.output_text

    except Exception as e:
        return f"AI Error: {str(e)}"


# Configure application
st.set_page_config(
    page_title="StudyMate AI",
    page_icon="🧠",
    layout="centered"
)

# Application heading
st.title("📚 StudyMate AI")
st.write("Your personal AI-powered study assistant.")


st.divider()

# Feature selection
st.subheader("Choose your study tool")

feature = st.selectbox(
    "What would you like to do today?",
    [
        "Summarize Notes",
        "Generate Quiz",
        "Explain a Concept"
    ]
)

# Student input
st.subheader("Enter your study material")

user_input = st.text_area(
    "Paste your notes or enter a topic:",
    placeholder="Enter your notes or question here...",
    height=150
)


def generate_ai_response(feature, user_input):

    text = user_input.strip()
    words = text.split()

    if feature == "Summarize Notes":

        preview = " ".join(words[:35])

        if len(words) > 35:
            preview += "..."

        return f"""
### 📝 Demo Summary

**Your notes contain:** {len(words)} words.

**Key content preview:**

{preview}

**Main takeaway:** Review the key ideas and concepts
contained in your study material.
"""

    
    elif feature == "Generate Quiz":

        return f"""
## 🧠 Practice Quiz

**Topic:** Based on your study material

**Instructions:** Answer the following questions
using the notes provided.

---

### Question 1
What is the main idea of this study material?

### Question 2
Explain one important concept from your notes.

### Question 3
Give an example related to the topic.

### Question 4
Why is this topic important?

---

### Your Turn!
Write your answers in your notebook and
compare them with your study material.
"""


    
    elif feature == "Explain a Concept":

        return f"""
## 📚 Concept Explanation

**Selected Topic:** {text}

---

### 1. Introduction

{ text } is the topic you have selected
for learning and understanding.

### 2. Understanding the Concept

Start by identifying the main idea.
Break the topic into smaller parts and
understand how each part connects.

### 3. Key Points to Remember

- Understand the basic definition.
- Learn the important concepts.
- Study practical examples.
- Revise the topic regularly.

### 4. Quick Revision

Try explaining this topic in your own words
without looking at your notes.

---

### 💡 Study Tip

Use examples and practice questions to
strengthen your understanding.
"""


# Generate button

# Generate button
if st.button("Generate", use_container_width=True):

    # Check for empty input
    if not user_input or not user_input.strip():
        st.warning("Please enter some text before continuing.")

    # Check input length
    elif len(user_input) > 10000:
        st.warning(
            "Your input is too long! Please keep it "
            "within 10000 characters."
        )

    else:
        try:
            st.success("Your input has been received!")

            st.info(f"Selected feature: {feature}")

            st.subheader("Your Input")
            st.write(user_input)

            st.subheader("StudyMate AI Response")

            response = generate_ai_response(feature, user_input)

            if response and response.strip():
                with st.container(border=True):
                    st.markdown(response)
            else:
                st.warning(
                    "No response was generated. Please try again."
                )

        except Exception:
            st.error(
                "Something went wrong while processing "
                "your request. Please try again."
            )

# if st.button("Generate", use_container_width=True):

#     if not user_input.strip():
#         st.warning("Please enter some text before continuing.")

#     else:
#         st.success("Your input has been received!")

#         st.info(f"Selected feature: {feature}")

#         st.subheader("Your Input")
#         st.write(user_input)

#         st.subheader("StudyMate AI Response")

#         response = generate_ai_response(feature, user_input)

#         st.write(response)

st.divider()

st.caption("StudyMate AI")

