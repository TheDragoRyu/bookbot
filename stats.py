def count_words(file_contents):
    array = file_contents.split()
    return len(array)


def count_unique(file_contents):
    dict = {}
    for character in file_contents:
        character = character.lower()
        if character in dict:
            dict[character] += 1
        else:
            dict[character] = 1
    return dict


def sort_dictionary(dict):
    list = []
    for key in dict:

        if key.isalpha() is False:
            continue

        value = dict[key]
        list.append({"char": key, "num": value})
    list.sort(reverse=True, key=sort_on)
    return list


def sort_on(items):
    return items["num"]
