# system and temperature

import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("api error")
client = Groq(api_key = my_api_key)
model = "openai/gpt-oss-20b"
role = 'user'
prompt = 'i love you'

# System
message_system = {
    'role': 'system',
    'content' : 'you are my girlfriend',

}

# message me role and content
message = {
    'role' : role,
    'content' : prompt,
}

messages = [message_system,message]

# temperature by  default is 0 meaning safe play, and its range is [o,2]
response = client.chat.completions.create(model = model, messages = messages, temperature = 2)
# print(response)
print('####################')
answer = response.choices[0].message.content
print(answer)
