#%% Configuración Inicial
from openai import OpenAI
import os

# %% Configurar la API key
from dotenv import load_dotenv
load_dotenv() # Carga el archivo de las variables de entorno

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

# %% 
completion = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {
            'role': 'user',
            'content': '¡Hola! ¿Me ayudas a aprender sobre la API de OpenAI?'
        }
    ]
)

# %%
completion.choices[0].message

# %% Ver la respuesta en Markdown
from IPython.display import display,Markdown
display(Markdown(completion.choices[0].message.content))

# %%
print(completion.choices[0].message.role)
# %%
