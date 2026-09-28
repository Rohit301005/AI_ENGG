import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError('api error')

client = Groq(api_key = my_api_key)
model = "openai/gpt-oss-20b"
role = 'user'
# 3 promts
prompt1 = "Hi"
prompt2 = "Explain time travel in details"
prompt3 = "Write  a 1000 words eassy on machine learning"

prompts = [prompt1,prompt2,prompt3]

for prompt in prompts:
    message = {
    'role' : role,
    'content' : prompt
    }
    messages = [message]
    response = client.chat.completions.create(model= model, messages = messages, max_tokens = 50)
    usage = response.usage
    print(f'Prompt : {prompt} --> your_token: {usage.prompt_tokens} completion_tokens : {usage.completion_tokens}')


# system
# message_system = {
#     'role' : 'system',
#     'content' : ''
# }

# message me role and content

# message = {
#     'role' : role,
#     'content' : prompt
# }

# messages = [message_system,message]

# response = client.chat.completions.create(model= model, messages = messages)