def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_char_dict(text)
    sorted_list = sorted_dict(char_dict)
    gen_report(sorted_list)
    

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

def sort_on(dict_entry):
    return dict_entry["num"]

def sorted_dict(char_dict):
    dict_list = []
    for key, value in char_dict.items():
        if key.isalpha():
            new_dict = {"character": key, "num": value}
            dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)   
    return  dict_list

def gen_report(sorted_list):
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"---- Begin Report of {book_path} ----")
    print()
    print(f"{num_words} words found in the document")
    print()
    for chars in sorted_list:
        char = chars["character"]
        count = chars["num"]
        print(f"The '{char}' character was found {count} times.")
    print()
    print("---- End Report ----")
    return
main()

