def word_counter(text:str):
    counter = 0
    splited_text = text.split()
    for word in splited_text:
        counter +=1
    return f"Found {counter} total words"

def char_counter(text:str):
    lower_case_text = text.lower()
    counted_char_dic = {}

    for char in lower_case_text:
        if char not in counted_char_dic:
            counted_char_dic[char] = 1
        else:
            counted_char_dic[char] += 1
    return counted_char_dic

def dictionary_sorter(dictionary,item_helper):
    dict_list = []
    for key in dictionary:
        dict_list.append({"char":key,"num":dictionary[key]})
    dict_list.sort(reverse=True, key=item_helper)
    return dict_list

def num_helper(item):
    return item["num"]