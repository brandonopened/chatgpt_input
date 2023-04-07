import openai 

openai.api_key = "<YOUR API KEY>"

user_input = input("What work experience do you have? ")
career_q = "What skills do you see in the following experience statement; write the skills as a numbered list"

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": career_q + user_input },
    ],
    temperature=0,
)

p1 = print(response['choices'][0]['message']['content'])
print(p1)

user_input2 = input("Which skills would you like to explore further as a career track? List the skills by their number as in 1,2,3:  ")
career_q2 = "Based on the selected skills, pick 3 careers that would be a perfect match for those skills"

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": career_q2 + user_input2 },
    ],
    temperature=0,
)

print(response['choices'][0]['message']['content'])
