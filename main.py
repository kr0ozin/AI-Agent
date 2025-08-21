import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import SYSTEM_PROMPT
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python import schema_run_python_file
from functions. write_file import schema_write_file
import sys
import argparse

def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Basic AI Agent")
    parser.add_argument("user_prompt")
    parser.add_argument("--verbose", "-v", action="store_true")

    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if not args.user_prompt:
        print("AI Assistant")
        print("\nUsage: python main.py <prompt>")
        print("Example: python main.py 'Why are the Giants the best team in the NFL?'")
        sys.exit(1)

    user_prompt = args.user_prompt
    verbose = args.verbose

    if verbose:
        print(f"User prompt: {user_prompt}")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose)

def generate_content(client, messages, verbose):
    
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file
        ]
    )
    
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=SYSTEM_PROMPT
            )
    )
    if verbose:
        print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
        print("Response tokens: " + str(response.usage_metadata.candidates_token_count))

    if response.function_calls:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(f"Response: \n{response.text}")



if __name__ == "__main__":
    main()
