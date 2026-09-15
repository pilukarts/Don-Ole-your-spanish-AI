LEVELS = ["A1", "A2", "B1", "B2", "C1", "C2"]
AUDIENCES = {
    "ninos": {"label": "Niños", "icon": "🎈"},
    "jovenes": {"label": "Jóvenes", "icon": "🎧"},
    "adultos": {"label": "Adultos", "icon": "☕"},
}

LESSON = {
    "title": "En la cafetería",
    "subtitle": "Pide algo rico y habla con confianza.",
    "words": [
        {"spanish": "un café con leche", "english": "a coffee with milk", "emoji": "☕"},
        {"spanish": "la cuenta, por favor", "english": "the bill, please", "emoji": "🧾"},
        {"spanish": "¿Cuánto cuesta?", "english": "How much is it?", "emoji": "💶"},
        {"spanish": "Quisiera…", "english": "I would like…", "emoji": "🙋"},
    ],
    "questions": [
        {"prompt": "¿Cómo pides la cuenta?", "options": ["La cuenta, por favor", "Tengo una cuenta", "Cuenta conmigo"], "answer": 0},
        {"prompt": "Completa: ___ un café con leche.", "options": ["Cuesta", "Quisiera", "Cuenta"], "answer": 1},
        {"prompt": "¿Qué significa ‘¿Cuánto cuesta?’", "options": ["Where is it?", "How much is it?", "Who wants it?"], "answer": 1},
    ],
}

