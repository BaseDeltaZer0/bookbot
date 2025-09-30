def main():
    print(get_book_text("books/frankenstein.txt"))

def get_book_text(file_path): #Takes a file path as input...
    with open(file_path, "r", encoding="utf-8") as f: #Opens it...
        contents = f.read() #Returns the contents as a string.
        return (contents)

main()