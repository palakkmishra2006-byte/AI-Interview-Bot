import google.generativeai as genai

# Paste your API key here
genai.configure(api_key="AIzaSyDM9nwUmpMc4gj17WBYsNUDmnI4sFMrA1Y")

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content(
    "Ask me one beginner Python interview question."
)

print(response.text)