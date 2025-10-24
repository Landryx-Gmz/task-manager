import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_simple_task(description):

    if not client.api_key:
        return["Error: la API key de OpenAI no esta configurada."]

    try:
        prompt = f"""Desglosa la singiente tarea compleja en una lista de 3 a 5 subtareas simples y accionables.

Tarea: {description}
        
Formato de respuesta:
-Subtarea 1
-Subtarea 2
-Subtarea 3
-etc.

Responde solo con la lista de subtareas, un por línea, empezando cada línea con un guión. """

        params = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "Eres un asistente experto en gestión de tareas que ayuda a dividir tareas complejas en pasos simples y accionables."},
                {"role":"user", "content": prompt}
            ],
            # "max_completion_tokens": 300,
            # "verbosity": "medium",
            # "reasoning_effort": "minimal"
        }

        response =client.chat.completions.create(**params)
        content = response.choices[0].message.content.strip()

        subtasks = []

        for line in content.split("\n"):
            line = line.strip()
            if line and line.startswith("-"):
                subtask = line[1:].strip()
                if subtask:
                    subtasks.append(subtask)
        return subtasks if subtasks else ["Error: No se han podido generar las subtareas."]

    except Exception as e:
        print(f"Error detallado: {str(e)}")
        return ["Error: No se ha podido realizar la conexión a OpenAI"]