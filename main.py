from stats import num_of_words
from stats import count_of_characters
from stats import sorted_list_of_characters
import sys

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def report_on_book(book):
    strings = get_book_text(book)
    words = num_of_words(strings)
    characters = count_of_characters(strings)
    sorted_characters = sorted_list_of_characters(characters)
    char_lines = [f"{entry['char']}: {entry['num']}" for entry in sorted_characters]
    chars_report = "\n".join(char_lines)

    report = (
        f"============ BOOKBOT ============\n"
        f"Analyzing book found at {book}...\n"
        f"----------- Word Count ----------\n"
        f"Found {words} total words\n"
        f"--------- Character Count -------\n"
        f"{chars_report}\n"
        f"============= END ==============="
    )
    return report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    book = sys.argv[1]
    strings = get_book_text(book)
    words = num_of_words(strings)
    count = count_of_characters(strings)
    report = report_on_book(book)
    return print(report)
main()