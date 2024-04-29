def count_words(text):
    """Count the number of words in a given text."""
    # Split the text into words based on whitespace
    words = text.split()
    return len(words)


def main():
    # Ask the user to enter text
    text = input("Enter text to count words: ")
    # Get the number of words using the count_words function
    word_count = count_words(text)
    # Print the number of words
    print(f"The text contains {word_count} words.")

if __name__ == "__main__":
    main()
