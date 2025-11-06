import sys
from stats import count_words
from stats import count_unique
from stats import sort_dictionary


def print_book(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


input = sys.argv
if len(input) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_path = input[1]
content = print_book(file_path)

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {count_words(content)} total words")
print("--------- Character Count -------")
unique_dict = count_unique(content)
sorted_list = sort_dictionary(unique_dict)
for i in sorted_list:
    print(f"{i["char"]}: {i["num"]}")
print("============= END ===============")
