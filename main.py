from stats import word_counter, sorted_on, count_leters, sorted_list
import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
print("Usage: python3 main.py <path_to_book>")
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    letters = count_leters(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_counter(text)} total words")
    print("--------- Character Count -------")
    for item in sorted_list(letters):
        print(f"{item['char']}: {item['num']}")
    print('============= END ===============')

if __name__ == "__main__":
    main()
