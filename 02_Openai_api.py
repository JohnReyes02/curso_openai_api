# %% Configuración Inicial
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

# %% Agregar un system prompt


def chat_with_system(system_prompt: str, user_prompt: str) -> str:
    '''Realiza una llamada con system prompt'''
    try:
        response = client.chat.completions.create(
            model='gpt-4o',
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f'Error: {str(e)}'


# %% Ejemplo de Uso
system_prompt = '''Eres un asistente con increible sentido del humor, 
que hace chistes de las tematicas que te solicitan,
ademas tu acento es un muy marcado Argentino'''
user_prompt = 'algo de borrachos'
respuesta = chat_with_system(system_prompt, user_prompt)

# %%
print(f'\nSystem Prompt: {system_prompt}')
print(f'\nUser Prompt: {user_prompt}')
print(f'\nRespuesta: {respuesta}')
# %%
