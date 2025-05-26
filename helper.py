# Add your utilities or helper functions to this file.

import os
import openai
from dotenv import load_dotenv, find_dotenv

# these expect to find a .env file at the directory above the lesson.                                                                                                                     # the format for that file is (without the comment)                                                                                                                                       #API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService                                                                                                                                     
def load_env():
    _ = load_dotenv(find_dotenv())

def get_openai_api_key():
    load_env()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key


def gpt_based_validation(prompt_text):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a project delivery expert reviewing a scenario planning document for a KPI dashboard project. "
                    "The user has provided complete output from different agents estimating effort, and four scenarios with duration, team composition, and cost. "
                    "Your task is to validate the logic, constraints, and consistency across scenarios and raise any potential inconsistencies or modeling issues. "
                    "Provide your critique in clear bullet points, and conclude with a score out of 10 for overall consistency and realism."
                )
            },
            {
                "role": "user",
                "content": prompt_text
            }
        ],
        temperature=0.3
    )
    return response['choices'][0]['message']['content']


