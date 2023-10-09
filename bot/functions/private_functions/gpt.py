import openai
import asyncio

openai.api_key = 'your openai key' 


async def generate_completion(prompt, content):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, lambda: generate_completion_func(prompt=prompt, content=content))
    return result

def generate_completion_func(prompt, content):
    message1 = prompt
    response =  openai.ChatCompletion.create(
          model="gpt-3.5-turbo-0613",
        messages=[{"role": "system", "content": ''},
                  {"role": "user", "content": str(content)+str(' '+message1)}],
        temperature=1,
        max_tokens=900,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0)
    print(response)
    return response.choices[0]['message']['content']



