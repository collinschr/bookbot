from stats import count_words, symbols_count, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    symbols_dict = symbols_count(book_text)

    print(f"============ BOOKBOT ============ \n Analyzing book found at {filepath}..." )

    print(f"----------- Word Count ---------- \n Found {num_words} total words")

    print("--------- Character Count -------")
    
    sorted_char_list = sort_dict(symbols_dict)
    i = 0
    for dict in sorted_char_list:
       print(f"{dict['char']}: {dict['num']}")

    print("============= END ===============")

main()

