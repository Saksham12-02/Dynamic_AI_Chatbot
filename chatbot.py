import json
import random
import ollama

# Load intents
with open("intents.json", "r") as f:
    data = json.load(f)

# Conversation memory
messages = []

def get_intent_response(user_input):

    user_input = user_input.lower()

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_input:
                return random.choice(intent["responses"])

    return None


def chatbot_response(user_input):

    # Check intents first
    intent = get_intent_response(user_input)

    if intent:
        return intent

    # Otherwise use AI
    messages.append({
        "role": "user",
        "content": user_input
    })

    response = ollama.chat(
        model="llama3.2",
        messages=messages
    )

    answer = response["message"]["content"]

    messages.append({
        "role": "assistant",
        "content": answer
    })

    return answer