def number_of_words(text):
    words = text.split()
    return len(words)


def number_of_each_character(text):
    dict_char = {}
    for word in text:
        lower = word.lower()
        if lower in dict_char:
            dict_char[lower] += 1
        else:
            dict_char[lower] = 1
    return dict_char


def sort_on(dict):
    return dict["num"]


def func(dict_char):
    list = []
    for i in dict_char:
        list.append({"char": i, "num": dict_char[i]})
    list.sort(reverse=True, key=sort_on)
    return list
