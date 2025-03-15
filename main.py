from stats import count_words

def get_book_text(filepath):
    """Reads a file and returns its contents as a string."""
    with open(filepath) as f:
        return f.read()

def count_words(text):
    """Counts the number of words in a string."""
    words = text.split()
    return len(words)

def main():
    """Reads the book, counts words, and prints the result."""
    book_text = get_book_text("./books/frankenstein.txt")
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()
