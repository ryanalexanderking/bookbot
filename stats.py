def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    char_count_dict = {}
    for char in text:
        char_count_dict.setdefault(char.lower(), 0)
        char_count_dict[char.lower()] += 1
    return char_count_dict

def get_sorted_char_dicts(char_count_dict):
    sorted_char_dicts = []
    for char in char_count_dict:
        sorted_char_dicts.append({'char': char, 'num': char_count_dict[char]})
    
    sorted_char_dicts.sort(key=lambda x: x['num'], reverse=True)
    return sorted_char_dicts