import openai 

openai.api_key = "enter yours here"

user_input = input("Enter your prompt: ")

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": user_input},
    ],
    temperature=0,
)

print(response['choices'][0]['message']['content'])