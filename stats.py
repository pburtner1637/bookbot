def count_words(text):
    """Counts the number of words in a string."""
    words = text.split()
    return len(words)

def count_characters(text):
    """Counts the occurrences of each character in a string."""
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
    
def sort_char_counts(char_counts):
    """Sorts character counts and returns a list of dictionaries."""
    sorted_chars = []
    for char, count in char_counts.items():
        sorted_chars.append({"char": char, "count": count})
    sorted_chars.sort(key=lambda x: x["count"], reverse=True)
    return sorted_chars
