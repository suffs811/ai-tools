#!/usr/bin/python3
# author: suffs811
# Copyright (c) 2023 suffs811
# https://github.com/suffs811/ai.git
# read the README.md file for more details; software distributed under MIT license
# <> purpose: ask OpenAI's chatGPT to provide an executive summary for the report made by the terminator.
#
# usage: python3 sum-ai.py <path_to_report>


import openai

# set up the argument parser to accept the name of the binary that has suid/sudo permissions
parser = argparse.ArgumentParser(description="Generate an executive summary by passing the terminator's report to ChatGPT, then add it to the report.")
parser.add_argument("-p", "--path", help="specify the path to the report made by the terminator")
args = parser.parse_args()
path = args.path

# load OpenAI API credentials from the environment variables
openai.api_key_path = "/var/key"

# or you can use the following if you want to put the actual key in the source code (not recommended bc its insecure)
#openai.api_key = "<API_key>"

# open report to send to ChatGPT
results = open("{}".format(path))
r = results.read()

# define the prompt to be used for the API call
prompt_suid = ( 
    "You are a cyber security consultant AI."
    "Analyze the following penetration testing report that outlines the enumeration, exploitation, privilege escalation, persistence, and data exfiltration stages of a penetration test and provide an executive summary for the report in less than 50 words:"
    "{}"
    )


# define a function to generate the response from the OpenAI API
def generate_response(prompt):
    response = openai.Completion.create(
    prompt=prompt,
    max_tokens=50,
    temperature=0.5,
    model="text-davinci-002"
)
    print(prompt)
    print(response)
    return response.choices[0].text


# generate the response from the OpenAI API according to module called
response = generate_response(prompt.format(r))
print(response)

results.close()


'''
curl -X POST https://api.openai.com/v1/engines/davinci/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <API_key>" \
-d '{"prompt": "What is the syntax for using the following tool during a penetration test: ", "max_tokens": 5}'
'''
