from google import genai

client = genai.Client(
    api_key="AQ.Ab8RN6JE5EL90hzHkb2kfrpTudP2cjQOSeG4msgxkboAif0x2A"
)

# Generate interview question
question_response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Ask me one beginner Python interview question."
)

question = question_response.text

print("\nInterview Question:")
print(question)

# Get user's answer
answer = input("\nYour Answer: ")

# Evaluate the answer
feedback_response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""
You are a technical interviewer.

Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer and provide:

1. Score out of 10
2. Strengths
3. Areas for Improvement
4. Ideal Answer
"""
)

print("\nFeedback:")
print(feedback_response.text)