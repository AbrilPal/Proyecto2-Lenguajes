
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

for word in words:
    # si es keyword
    if test_word(word, keywordsNodes, keywordsLinks):
        keywords.append(word)
    elif test_word(word, nodes, links):
        tokens.append(word)

print("TOKENS: ")
for token in tokens:
    print(token)

print()

print("\rKEYWORDS: ")
for keyword in keywords:
    print(keyword)

print()