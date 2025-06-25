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

# %% Crear lista para almacenar mensajes

messages = []
system_prompt = '''Eres un asistente con increible sentido del humor, 
que hace chistes de las tematicas que te solicitan,
ademas tu acento es un muy marcado Argentino'''

# Agregar un system prompt inicial
messages.append({
    'role': 'system',
    'content': system_prompt
})

# Primera pregunta
messages.append({
    'role': 'user',
    'content': 'Un chiste de borrachos'
})

# Obtener respuesta
response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=messages
)

# %%

assistant_response = response.choices[0].message.content
assistant_response

# %% Guardar la respuesta del asistente

messages.append({
    'role': 'assistant',
    'content': assistant_response
})

# Hacer una pregunta de seguimiento
messages.append({
    'role': 'user',
    'content': 'Explicamelo'
})

# Obtener nueva respuesta
response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=messages
)

# Guardar la nueva respuesta
assistant_response = response.choices[0].message.content
messages.append({
    'role': 'assistant',
    'content': assistant_response
})

print('\nSegunda respuesta:', assistant_response)

# %% Para ver cómo va la memoria hasta ahora

messages

# %% Función helper para hacer más fácil agregar mensajes y obtener respuestas

def chat(prompt: str, message_history: list) -> str:
    '''
    Envía un mensaje y obtiene una respuesta manteniendo el historial
    '''
    if len(message_history) == 0:
        system_prompt = 'Eres un asistente con increible sentido del humor, que hace chistes de las tematicas que te solicitan, ademas tu acento es un muy marcado Colombiano'
        message_history.append({
            'role': 'system',
            'content': system_prompt
        })
    # Agregar el nuevo prompt al historial
    message_history.append({
        'role': 'user',
        'content': prompt
    })

    # Obtener respuesta
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=message_history
    )

    # Guardar y retornar la respuesta 
    assistant_response = response.choices[0].message.content
    message_history.append({
        'role': 'assistant',
        'content': assistant_response
    })

    return assistant_response

# %%

messages_function = []
chat('Un chiste de borrachos', messages_function)

# %%

chat('ahora de padres e hijos', messages_function)

# %%
messages_function

# %%
