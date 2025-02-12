def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    alpha_count_list = get_alpha_list(chars_dict)

    print_report(num_words, alpha_count_list, book_path)


def get_book_text(path):
    with open(path) as f:
        return f.read()


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


def get_alpha_list(char_dict):
    alpha_list = list()
    for key, value in char_dict.items():
        if key.isalpha():
            alpha_list.append({"char": key, "count" : value})
    alpha_list.sort(reverse=True, key=sort_on)
    return alpha_list

def sort_on(dict):
    return dict["count"]

def print_report(word_count, alpha_count, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for char in alpha_count:
        print("The '" + char["char"] + "' character was found " + str(char["count"]) + " times")
    print("--- End report ---")

main()
