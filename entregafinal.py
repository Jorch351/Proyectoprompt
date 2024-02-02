import openai

# Configura tu clave de API de OpenAI
openai.api_key = 'tu_clave_de_api'

def generate_summary(text):
    # Define el prompt para la generación de texto
    prompt = f"Resumir el siguiente texto:\n{text}\n\nResumen:"

    # Llamada a la API de OpenAI para generar el resumen
    response = openai.Completion.create(
        engine="text-davinci-002",  # Puedes cambiar el motor según tus necesidades
        prompt=prompt,
        max_tokens=150,  # Ajusta este valor según la longitud deseada del resumen
        temperature=0.7  # Ajusta la temperatura para controlar la creatividad del modelo
    )

    # Extrae el texto generado por OpenAI
    generated_text = response['choices'][0]['text']
    return generated_text

# Interacción con el usuario
user_input = input("Ingrese el texto que desea resumir: ")
summary = generate_summary(user_input)

print("\nResumen generado por OpenAI GPT-3:")
print(summary)