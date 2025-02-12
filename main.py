def main():
    with open("books/frankenstein.txt") as f:  # Loads txt file into string.
        file_contents = f.read()
        # print(file_contents)
    # print(count_words(file_contents))
    result = count_chars(file_contents)
    print(result)


def count_words(text):
    words = text.split()
    return len(words)


def count_chars(text):
    char_set = set(text.lower())
    char_dict = dict()
    for char in char_set:
        char_dict[char] = 0
        for c in text:
            if c.lower() == char:
                char_dict[char] += 1
    return char_dict


main()
