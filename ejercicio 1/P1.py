def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == "".join(reversed(word))

if __name__ == "__main__":
    word = "anita lava la tina"
    print(f"Is palindrome: {is_palindrome(word)}")