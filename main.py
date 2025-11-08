import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        path_string = f.read()
        return path_string
    
from stats import get_num_words, get_char_vals, sort_on

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        result = get_book_text(sys.argv[1])
        total = f"Found {get_num_words(result)} total words"
        values = get_char_vals(result)
        sorted = sort_on(values)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(total)
        print("--------- Character Count -------")
        for each in sorted:
            if each["char"].isalpha():
                print(f"{each["char"]}: {each["num"]}")
        print("============= END ===============")
    
   
main()