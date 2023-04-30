#!/usr/bin/python3
# author: suffs811
# Copyright (c) 2023 suffs811
# https://github.com/suffs811/ai.git
# read the README.md file for more details; software distributed under MIT license
# <> purpose: ask OpenAI's chatGPT to provide the syntax for using a tool during a penetration test.
#
# usage: python3 tool-ai.py <tool>

import openai
import argparse

# set up the argument parser to accept the name of the cybersecurity tool as input
parser = argparse.ArgumentParser(description="Generate syntax for using a cybersecurity tool.")
parser.add_argument("tool_name", help="The name of the cybersecurity tool to generate syntax for.")
args = parser.parse_args()
tool = args.tool_name

# load OpenAI API credentials from the environment variables
openai.api_key_path = "/var/key"

# or you can use the following if you want to put the actual key in the source code (not recommended bc its insecure)
#openai.api_key = "<API_key>"

# define the prompt to be used for the API call
prompt = ( 
    "Syntax for the gobuster tool: 'gobuster dir -u IP -w WORDLIST'. Syntax for the nikto tool: 'nikto -h IP -t 3 -ask no'. "
    "Provide the syntax for using {} during a penetration test in less than 10 words."
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


# generate the response from the OpenAI API
response = generate_response(prompt.format(tool))

# print the response
print(response)


'''
curl -X POST https://api.openai.com/v1/engines/davinci/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <API_key>" \
-d '{"prompt": "What is the syntax for using the following tool during a penetration test: ", "max_tokens": 5}'
'''
