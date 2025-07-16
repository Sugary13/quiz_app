# 🧠 Quiz App con Interfaz Gráfica (Tkinter)

Este proyecto es una aplicación interactiva de preguntas tipo quiz desarrollada en Python. Las preguntas se obtienen automáticamente desde una API pública (Open Trivia DB) y se presentan al usuario con botones de "True" o "False" dentro de una interfaz gráfica construida con `Tkinter`.

---

## 🎯 ¿Qué hace?

- Consume preguntas reales desde [Open Trivia DB](https://opentdb.com/api_config.php)
- Muestra cada pregunta en una ventana interactiva
- Evalúa tus respuestas y muestra puntaje actualizado
- Al finalizar, te indica que completaste el quiz

---

## 📦 Estructura del proyecto

.

├── main.py # Punto de entrada: maneja flujo del programa

├── data.py # Consumo de la API y extracción de preguntas

├── images/

│ ├── false.png

│ ├── true.png

│ ├── right.png

├── question_model.py # Clase Question que representa cada pregunta

├── quiz_brain.py # Lógica del quiz (avance, respuesta, puntaje)

├── ui.py # Interfaz gráfica con Tkinter

└── README.md


---

## 📡 Fuente de datos

Este proyecto utiliza la API de Open Trivia DB:

https://opentdb.com/api.php?amount=10&type=boolean

Respuesta esperada:

```json
{
  "response_code": 0,
  "results": [
    {
      "category": "Science & Nature",
      "type": "boolean",
      "difficulty": "easy",
      "question": "The chemical symbol for Iron is Fe.",
      "correct_answer": "True",
      ...
    }
  ]
}
```

En data.py se valida si el response_code es 0 (éxito), y si no, se muestra un mensaje de error amigable.

▶️ Cómo ejecutarlo

1. Asegúrate de tener Python 3 instalado.

2. Instala el paquete necesario (solo requests):

pip install requests

3. Ejecuta el programa:

python main.py

🛠 Tecnologías usadas

- Python 3

- Tkinter para GUI

- requests para consumo de APIs

- Programación orientada a objetos (OOP)
