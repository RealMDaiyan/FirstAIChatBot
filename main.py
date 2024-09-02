import openai

with open(".env", "r") as file:
    openai.api_key = open(".env", "r").read().strip()

def get_response(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question},
            ],
            max_tokens=150
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

while True:
    question = input("You: ")
    if question.lower() in ["exit", "quit"]:
        break
    print("Bot:", get_response(question))
