import os
import openai
import config

openai.api_key = config.OPENAI_API_KEY


def openAiQuery(query):
    response = openai.Completion.create(
        engin = "davinci-instruct-beta-v3",
        prompt = query, 
        temperature = 0.8,
        max_tokes=200,
        top_p =1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if "choices" in response:
        if len(response["choices"]) > 0 :
            answer = response["choices"][0]["text"]
        else:
            ansewr = "Oppps sorry, you beat the AI this time"
    else:
        ansewr = "Oppps sorry, you beat the AI this time"

    return(answer)

