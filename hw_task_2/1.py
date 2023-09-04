def new_func(stroka, stopwords):
    stroka_words = stroka.split()

    def del_stop_words(word):
        return word not in stopwords

    filtered_words = filter(del_stop_words, stroka_words)
    result_string = ' '.join(filtered_words)
    return result_string

stopwords = ["Python", "php", "go", "C"]
stroka = "study Python Disk C php"
filtered_string = new_func(stroka, stopwords)
print(filtered_string)












