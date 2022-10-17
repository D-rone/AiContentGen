import os
import openai
import config

openai.api_key = config.OPENAI_API_KEY


def productDeescription(query)
    reponse = openai.Completion.create(
        engin = "davinci-instruct-beta-v3",
        prompt = "",
        temperature = 0.5,
        max_tokes=200,
        top_p =1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print (reponse)
query = "apple iphone"
productDeescription(query)