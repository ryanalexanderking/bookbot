import sys

from stats import get_num_words, get_char_count, get_sorted_char_dicts

def get_book_text(filepath):
    with open(filepath, 'r') as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')#
        sys.exit(1)
        return

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = get_num_words(book_text)
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    char_count_dict = get_char_count(book_text)
    sorted_char_dicts = get_sorted_char_dicts(char_count_dict)
    for char_dict in sorted_char_dicts:
        if char_dict['char'].isalpha():
            print(f'{char_dict['char']}: {char_dict['num']}')
    print('============= END ===============')

main()