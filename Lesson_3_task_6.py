def u_func(word: str = 'text'):
    return "".join([word[0].upper(), word[1:]])
print(u_func())
words = input("Введите строку из нескольких слов:").split()
words = [u_func(x) for x in words]
print(" ".join(words))