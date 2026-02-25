def auto_reply(message_text: str):
    rules = {
        "hello": "Hi there! How can I help you today?",
        "pricing": "Visit our site for pricing details."
    }
    for keyword, reply in rules.items():
        if keyword in message_text.lower():
            return reply
    return None