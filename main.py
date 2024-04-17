def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_char_dict(text)
    print(char_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_dict(text):
    num_char_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered in num_char_dict:
            num_char_dict[lowered] += 1
        else:
            num_char_dict[lowered] = 1
    return num_char_dict


main()

