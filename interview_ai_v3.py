from google import genai

client = genai.Client(
    api_key="AQ.Ab8RN6LJQ73Zk5A19MvUFtX9uAFPwLtz8zNfsfIWAHBr8kPq3w"
)

total_questions = 3

print("Welcome to AI Interview Bot")
print("=" * 40)

for i in range(total_questions):

    print(f"\nQuestion {i+1}/{total_questions}")
    print("-" * 30)

    question_response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Ask one beginner Python interview question."
    )

    question = question_response.text

    print(question)

    answer = input("\nYour Answer: ")

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

print("\nInterview Completed!")
print("=" * 40)