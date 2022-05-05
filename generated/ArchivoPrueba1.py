import sys

class Node:
    def __init__(self, id, isInitial, isFinal):
        self.id = id
        self.isInitial = isInitial
        self.isFinal = isFinal

class Link:
    def __init__(self, source, target, label):
        self.source = source
        self.target = target
        self.label = label

def separate_words(fileRead):
    print(fileRead)
    words = []
    currentWord = ''
    for character in fileRead:
        if character != " ":
            currentWord = currentWord + character
        else:
            print(currentWord, "  i")
            words.append(currentWord)
            currentWord = ''
    
    if currentWord != '':
        print(currentWord, " uuu ")
        words.append(currentWord)
    
    return words

def test_word(word, nodes, links):
    initialStates = []
    acceptStates = []

    for node in nodes:
        if node.isInitial:
            initialStates.append(node)
        if node.isFinal:
            acceptStates.append(node)
    
    itBelongs = False

    # recorrer los estados iniciales
    for initialState in initialStates:
        currentState = initialState

        # verificar cada letra de la palabra en el afd
        for iWord in range(len(word)):
            letter = word[iWord]

            currentState = evaluate_character(letter, currentState, nodes, links)

            if (currentState == -1):
                break
            else:
                if iWord == (len(word) - 1):
                    if currentState.isFinal:
                        itBelongs = True
    
    return itBelongs

# Devuelve -1 si no existe transicion desde el nodo hacia otro con la letter, de lo contrario devuelve el nodo target
def evaluate_character(letter, currentState, nodes, links):
    initialState = currentState
    stateId = -1

    for link in links:
        if link.source == initialState.id and link.label == letter:
            stateId = link.target
    
    if stateId != -1:
        for node in nodes:
            if node.id == stateId:
                return node
    return stateId
            
    


# INICIO DE PROGRAMA
testFileName = sys.argv[1]
file = open(testFileName, "r")
words = separate_words(file.read())

# tokens y keywords
tokens = []
keywords = []

# Nodos y Links de Tokens
nodes = []
links = []

# Nodos y Links de Keywords
keywordsNodes = []
keywordsLinks = []


# NODOS
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