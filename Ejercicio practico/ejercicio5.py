def invest_word(word):
    invested_word = "".join(reversed(word))
    return invested_word

text = input("Ingrese la palabra: ")

print("Palabra invertida:", invest_word(text))