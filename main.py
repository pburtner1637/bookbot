from stats import count_words, count_characters, sort_char_counts

def get_book_text(filepath):
    """Reads a file and returns its contents as a string."""
    with open(filepath) as f:
        return f.read()

def main():
    """Reads the book, counts words, and prints the result."""
    book_text = get_book_text("./books/frankenstein.txt")
    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    sorted_char_counts = sort_char_counts(char_counts)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char_counts:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
