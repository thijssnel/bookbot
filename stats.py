def word_counter(string):
    words = string.split()
    return len(words)

def count_leters(string):
    letter_dict = {}
    words = string.split()

    for word in words:
        for letter in word:
            if letter.lower() not in letter_dict:
                letter_dict[letter.lower()] = 0
            if letter.lower() in letter_dict:
                letter_dict[letter.lower()] += 1
    return letter_dict

def sorted_on(items):
    return items["num"]

def sorted_list(char_dict):
    dict_list = []
    for char, num in char_dict.items():
        dict_list.append({"char":char, "num":num})
    dict_list.sort(reverse=True, key=sorted_on)
    return dict_list