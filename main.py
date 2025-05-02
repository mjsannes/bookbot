### BOOKBOT PYTHON CODE
# Morgan Sannes
# 25-04-30


# import external functions
import sys
from stats import count_words, count_characters, sort_character_counts

# function to convert book into text
def get_book_text(path_to_file):

    # open the path to the file
    with open(path_to_file) as f:

        # get all the contents of the book as a string
        file_contents = f.read()
        
        # return the file contents in the function
        return file_contents

# main function
def main():

    # check if exactly one argument (plus script name) is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # define the book path
    book_path = sys.argv[1]

    # previously used book: "books/frankenstein.txt"

    # obtain the text of the book using the path
    book_text = get_book_text(book_path)

    # obtain the count of the books
    num_words = count_words(book_text)

    # count all the characters
    char_counts = count_characters(book_text)

    # order/sequence the sorted characters (most to least)
    sorted_chars = sort_character_counts(char_counts)

    # print the book text to the console
    print(f"{num_words} words found in the document")

    # print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")

# past inputs, for archive
    # print the character count
    # print(char_counts)

# validation of the input code
if __name__ == "__main__":
    main()