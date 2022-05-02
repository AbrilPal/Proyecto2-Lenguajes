
from platform import node


def is_Int(num):
    try:
        int(num)
        return True
    except:
        return False

def is_Decimal(num):
    try:
        float(num)
        return True
    except:
        return False

def is_String(cadena):
    if type(cadena)==str:
        return True
    else:
        return False

# Test

print()
print(words)
print()

for word in words:
    # si es keyword
    if word == '':
        print("EspacioEnBlanco")
    if test_word(word, keywordsNodes, keywordsLinks):
        keywords.append(word)
    elif test_word(word, nodes, links):
        tokens.append(word)

for token in tokens:
    if is_Int(token) == True:
        print("numeroEntero", token)
    elif is_Decimal(token) == True:
        print("numeroDecimal", token)
    elif is_String(token) == True:
        print("cadena", token)

print("TOKENS: holi prueba ")
print(tokens)

print("\rKEYWORDS: ")
print(keywords)