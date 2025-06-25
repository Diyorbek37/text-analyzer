def analyze_text(text):
    letter_count = len(text.replace(" ", ""))
    word_count = len(text.split())
    sentence_count = text.count('.') + text.count('!') + text.count('?')

    return letter_count, word_count, sentence_count


if __name__ == "__main__":
    user_text = input("Enter your text: ")
    letters, words, sentences = analyze_text(user_text)

    print(f"Total letters (excluding spaces): {letters}")
    print(f"Total words: {words}")
    print(f"Total sentences: {sentences}")
