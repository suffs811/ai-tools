#!/usr/bin/python3
# author: suffs811
# Copyright (c) 2023 suffs811
# https://github.com/suffs811/ai.git
# read the README.md file for more details; software distributed under MIT license
# <> purpose: ask OpenAI's chatGPT to provide the syntax for using a sudoable/SUID binary for privilege escalation from GTFObins.
#
# usage: python3 priv-ai.py <suid/sudo> -b <binary/file name>


import openai
import argparse


# set up the argument parser to accept the name of the binary that has suid/sudo permissions
parser = argparse.ArgumentParser(description="Generate the GTFObins syntax for escalating privileges from a suid file/sudo command.")
parser.add_argument("module", help="the capabilities you or the binary has (either 'suid' or 'sudo')")
parser.add_argument("-b", "--binary", help="specify the command or file that is suid/sudo (ex: 'env' or 'tar')")
args = parser.parse_args()
module = args.module
binary = args.binary

# load OpenAI API credentials from the environment variables
openai.api_key_path = "/var/key"

# or you can use the following if you want to put the actual key in the source code (not recommended bc its insecure)
#openai.api_key = "<API_key>"

# define the prompt to be used for the API call
prompt_suid = ( 
    "You are a cyber security consultant AI."
    "Search https://gtfobins.github.io/ and return the syntax for {} under the 'SUID' heading. If no SUID heading exists, reply 'this command's SUID bitset cannot be exploited for privilege escalation.'"
    )

prompt_sudo = ( 
    "You are a cyber security consultant AI."
    "Search https://gtfobins.github.io/ and return the syntax for {} under the 'Sudo' heading. If no SUID heading exists, reply 'this command cannot be exploited for privilege escalation using sudo.'"
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

if module == "suid":
    prompt = prompt_suid
    response_suid = generate_response(prompt.format(binary))
    print(response)
elif module == "sudo":
    prompt = prompt_sudo
    response_sudo = generate_response(prompt_sudo.format(binary))
    print(response)
else:
    print("\n*** please specify either 'suid' or 'sudo' ***")





'''
curl -X POST https://api.openai.com/v1/engines/davinci/completions \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <API_key>" \
-d '{"prompt": "What is the syntax for using the following tool during a penetration test: ", "max_tokens": 5}'
'''
