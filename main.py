import sys
from stats import word_counter,char_counter,dictionary_sorter,num_helper

if len(sys.argv) <2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = "books/frankenstein.txt"
def get_book_text(path) -> str:
    with open(path) as f:
        text = f.read()
    return text

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    text = get_book_text(sys.argv[1])

    print("----------- Word Count ----------")
    print(word_counter(text))
    print("--------- Character Count -------")

    counted_chars =char_counter(text)
    sorted_characters = dictionary_sorter(counted_chars,num_helper)
    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")


    print("============= END ===============")


main()