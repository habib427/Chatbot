import json

def load_responses():
    with open("responses.json", "r") as file:
        return json.load(file)

def get_response(user_input, responses):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return responses.get("default", "I don't understand.")
