def spin_words(sentence):
    list_str = sentence.split()
    counter = 0
    for i in list_str:
        if len(i) >= 5:
            list_str[counter] = i[::-1]
        counter += 1
    return ' '.join(list_str)


# Решение в 1 строку
'''def spin_words(sentence):
    return ' '.join([word if len(word) < 5 else word[::-1] for word in sentence.split()])'''
