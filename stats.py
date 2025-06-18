def count_words(book_text):
    num_words = len(book_text.split())
    return num_words

def symbols_count(book_text):
    symbols_dict={}
    
    for char in book_text:
        proper_char = char.lower()
        if proper_char in symbols_dict:
            symbols_dict[proper_char] += 1
        else:
            symbols_dict[proper_char] = 1
    
    return symbols_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    list_of_dictionaries = []
    for char in dict:
        temp_dict = {}
        temp_dict["char"] = char
        temp_dict["num"] = dict[char]

        list_of_dictionaries.append(temp_dict)

    list_of_dictionaries.sort(reverse = True, key = sort_on)
    return list_of_dictionaries