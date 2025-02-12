def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(chars_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    char_set = set(text.lower())
    char_dict = dict()
    for char in char_set:
        char_dict[char] = 0
        for c in text:
            if c.lower() == char:
                char_dict[char] += 1
    return char_dict


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
