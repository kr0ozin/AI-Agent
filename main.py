import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Basic AI Agent")
    parser.add_argument("user_prompt")
    parser.add_argument("--verbose", "-v", action="store_true")

    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    if len(sys.argv) < 2:
        print("Prompt must be provided as an argument")
        sys.exit(1)

    messages = [
        types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
    ]
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages,
    )

    if args.verbose:
        print(f"User prompt: {sys.argv[1]}")
        print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
        print("Response tokens: " + str(response.usage_metadata.candidates_token_count))

    print(response.text)



if __name__ == "__main__":
    main()
