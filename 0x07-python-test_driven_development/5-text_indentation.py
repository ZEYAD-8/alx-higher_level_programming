
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    endings = {".", "?", ":"}
    for letter in text:
        print(letter, end="")
        if letter in endings:
            print("\n")
