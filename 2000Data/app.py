import os
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']

# Configure the model ID. Change this to your model ID.
model = "ada:ft-personal-2023-11-22-07-16-27"

# Let's use a drug from each class
drugs = [
    "A CN Gel(Topical) 20gmA CN Soap 75gm",  # Class 0
    "Addnok Tablet 20'S",  # Class 1
    "ABICET M Tablet 10's",  # Class 2
    "Ferikind S 50mg Injection 2.5ml" #Class 5
]

# Returns a drug class for each drug
for drug_name in drugs:
    prompt = "Drug: {}\nMalady:".format(drug_name)

    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=1,
        max_tokens=1,
    )

    # Print the generated text
    drug_class = response.choices[0].text
    # The result should be 0, 1, and 2, 5
    print(drug_class)