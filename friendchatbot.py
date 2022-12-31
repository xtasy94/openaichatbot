import openai


openai.api_key = "YOUR OPENAI API"


model_engine = "text-davinci-002"

while True:
    
    message = input("You: ")

   
    response = openai.Completion.create(
        engine=model_engine,
        prompt=f"You: {message}\nFriend: ",
        max_tokens=1024,
        temperature=0.5,
    )

    
    print("Friend:", response.choices[0].text)
