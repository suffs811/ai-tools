#!/usr/bin/python3

import openai
import argparse

# Set up the argument parser to accept the name of the cybersecurity tool as input
parser = argparse.ArgumentParser(description="Generate syntax for using a cybersecurity tool.")
parser.add_argument("tool_name", help="The name of the cybersecurity tool to generate syntax for.")
args = parser.parse_args()
tool = args.tool_name

# Load OpenAI API credentials from the environment variables
openai.api_key_path = "/var/key"

# Define the prompt to be used for the API call
prompt = ( 
    "Syntax for the gobuster tool: 'gobuster dir -u IP -w WORDLIST'. Syntax for the nikto tool: 'nikto -h IP -t 3 -ask no'. "
    "Provide the syntax for using {} during a penetration test in less than 10 words."
    )

# Define a function to generate the response from the OpenAI API
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


# Generate the response from the OpenAI API
response = generate_response(prompt.format(tool))

# Print the response
print(response)
