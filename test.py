import openai
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']

FINE_TUNED_MODEL="curie:ft-personal-2023-11-21-07-01-13"
YOUR_PROMPT="What is the remote for?"

response = openai.Completion.create(
    model=FINE_TUNED_MODEL,
    prompt=YOUR_PROMPT
    # additional parameters
    # temperature,
    # frequency_penalty,
    # presence_penalty
    # ..etc
)
print(response)