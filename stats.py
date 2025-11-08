def get_num_words(result):
    num_words = 0
    for x in result.split():
        num_words += 1
    return num_words

def get_char_vals(result):
    char_values = {}
    for char in result:
        if char.lower() not in char_values:
            char_values[char.lower()] = 1
        else:
            char_values[char.lower()] += 1
    return char_values

def key_num(items):
    return items["num"]

def sort_on(char_values):
    ind_values = []
    for ch, count in char_values.items():
        ind_values.append({"char": ch, "num": count})
    ind_values.sort(reverse=True, key=key_num)
    return ind_values
