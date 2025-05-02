


# word count function
def count_words(book_text):
    words = book_text.split()
    return len(words)

# character count function
def count_characters(book_text):
    char_counts = {}
    book_text_lower = book_text.lower()
    for char in book_text_lower:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

# define the method of sortation
def sort_on(dict_item):
    return dict_item["num"]

# perform the sortation
def sort_character_counts(char_counts):
    sorted_list = [{"char": char, "num": count} for char, count in char_counts.items() if char.isalpha()]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


    