#Importing functions from Stats
from stats import get_num_words #Takes string dump and slices it to get wordcount.

#Entry function, runs get_book_text, calls necessary processing, and prints results.
def main():
    content = (get_book_text("books/frankenstein.txt"))
    num_words = get_num_words(content)
    print(f"Found {num_words} total words")
    
#Takes the file from the address specified in main, converts it to a string, and returns it.
def get_book_text(file_path): #Takes a file path as input...
    with open(file_path, "r", encoding="utf-8") as f: #Opens it...
        content = f.read() #Returns the contents as a string.
        return (content)

main()