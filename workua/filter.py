def filter_word(word):
    word_string = ''
    for i in word:
        if i == "'":
            word_string += "`"
        elif i == ",":
            continue
        else:
            word_string += i
    return word_string
