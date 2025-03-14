def get_book_text(filepath):
    """Reads a file and returns its contents as a string."""
    with open(filepath) as f:
        return f.read()

def main():
    """Reads and prints the contents of the frankenstein.txt file."""
    book_text = get_book_text("./books/frankenstein.txt")
    print(book_text)

if __name__ == "__main__":
    main()
