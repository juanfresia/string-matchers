def encode_text(text, enconding=""):
    """Given a string, returns a list of the same text, with every simbol in the string
    replaced as an unique int. Encoding is needed if the string is not an utf-8 string"""
    return [ord(c) for c in text]
