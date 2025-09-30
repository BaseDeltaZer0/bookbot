def main():
    content = (get_book_text("books/frankenstein.txt"))
    num_words = get_word_count(content)
    print(f"Found {num_words} total words")
    

def get_book_text(file_path): #Takes a file path as input...
    with open(file_path, "r", encoding="utf-8") as f: #Opens it...
        content = f.read() #Returns the contents as a string.
        return (content)

def get_word_count(content):
    word_list = content.split()
    word_count = len(word_list)
    return word_count

main()