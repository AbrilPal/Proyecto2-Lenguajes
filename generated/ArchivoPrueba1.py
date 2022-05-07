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
    print()
    print("entrada: ", fileRead)
    print()
    words = []
    currentWord = ''
    for character in fileRead:
        if character != " ":
            currentWord = currentWord + character
        else:
            words.append(currentWord)
            currentWord = ''
    
    if currentWord != '':
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


# NODOSnodes.append(Node('1', True, False))nodes.append(Node('2', False, True))nodes.append(Node('3', False, True))nodes.append(Node('4', False, True))nodes.append(Node('5', False, True))nodes.append(Node('6', False, True))nodes.append(Node('7', False, True))nodes.append(Node('8', False, True))nodes.append(Node('9', False, True))nodes.append(Node('10', False, True))nodes.append(Node('11', False, True))nodes.append(Node('12', False, True))nodes.append(Node('13', False, True))nodes.append(Node('14', False, True))nodes.append(Node('15', False, True))nodes.append(Node('16', False, True))nodes.append(Node('17', False, True))nodes.append(Node('18', False, True))nodes.append(Node('19', False, True))nodes.append(Node('20', False, True))nodes.append(Node('21', False, True))nodes.append(Node('22', False, True))nodes.append(Node('23', False, True))nodes.append(Node('24', False, True))nodes.append(Node('25', False, True))links.append(Link('1', '2', 'a'))links.append(Link('1', '3', 'b'))links.append(Link('1', '4', 'c'))links.append(Link('1', '5', 'd'))links.append(Link('1', '6', 'e'))links.append(Link('1', '7', 'f'))links.append(Link('1', '8', 'g'))links.append(Link('1', '9', 'h'))links.append(Link('1', '10', 'i'))links.append(Link('1', '11', '0'))links.append(Link('1', '12', '1'))links.append(Link('2', '13', 'a'))links.append(Link('2', '14', 'b'))links.append(Link('2', '15', 'c'))links.append(Link('2', '16', 'd'))links.append(Link('2', '17', 'e'))links.append(Link('2', '18', 'f'))links.append(Link('2', '19', 'g'))links.append(Link('2', '20', 'h'))links.append(Link('2', '21', 'i'))links.append(Link('2', '22', '0'))links.append(Link('2', '23', '1'))links.append(Link('3', '13', 'a'))links.append(Link('3', '14', 'b'))links.append(Link('3', '15', 'c'))links.append(Link('3', '16', 'd'))links.append(Link('3', '17', 'e'))links.append(Link('3', '18', 'f'))links.append(Link('3', '19', 'g'))links.append(Link('3', '20', 'h'))links.append(Link('3', '21', 'i'))links.append(Link('3', '22', '0'))links.append(Link('3', '23', '1'))links.append(Link('4', '13', 'a'))links.append(Link('4', '14', 'b'))links.append(Link('4', '15', 'c'))links.append(Link('4', '16', 'd'))links.append(Link('4', '17', 'e'))links.append(Link('4', '18', 'f'))links.append(Link('4', '19', 'g'))links.append(Link('4', '20', 'h'))links.append(Link('4', '21', 'i'))links.append(Link('4', '22', '0'))links.append(Link('4', '23', '1'))links.append(Link('5', '13', 'a'))links.append(Link('5', '14', 'b'))links.append(Link('5', '15', 'c'))links.append(Link('5', '16', 'd'))links.append(Link('5', '17', 'e'))links.append(Link('5', '18', 'f'))links.append(Link('5', '19', 'g'))links.append(Link('5', '20', 'h'))links.append(Link('5', '21', 'i'))links.append(Link('5', '22', '0'))links.append(Link('5', '23', '1'))links.append(Link('6', '13', 'a'))links.append(Link('6', '14', 'b'))links.append(Link('6', '15', 'c'))links.append(Link('6', '16', 'd'))links.append(Link('6', '17', 'e'))links.append(Link('6', '18', 'f'))links.append(Link('6', '19', 'g'))links.append(Link('6', '20', 'h'))links.append(Link('6', '21', 'i'))links.append(Link('6', '22', '0'))links.append(Link('6', '23', '1'))links.append(Link('7', '13', 'a'))links.append(Link('7', '14', 'b'))links.append(Link('7', '15', 'c'))links.append(Link('7', '16', 'd'))links.append(Link('7', '17', 'e'))links.append(Link('7', '18', 'f'))links.append(Link('7', '19', 'g'))links.append(Link('7', '20', 'h'))links.append(Link('7', '21', 'i'))links.append(Link('7', '22', '0'))links.append(Link('7', '23', '1'))links.append(Link('8', '13', 'a'))links.append(Link('8', '14', 'b'))links.append(Link('8', '15', 'c'))links.append(Link('8', '16', 'd'))links.append(Link('8', '17', 'e'))links.append(Link('8', '18', 'f'))links.append(Link('8', '19', 'g'))links.append(Link('8', '20', 'h'))links.append(Link('8', '21', 'i'))links.append(Link('8', '22', '0'))links.append(Link('8', '23', '1'))links.append(Link('9', '13', 'a'))links.append(Link('9', '14', 'b'))links.append(Link('9', '15', 'c'))links.append(Link('9', '16', 'd'))links.append(Link('9', '17', 'e'))links.append(Link('9', '18', 'f'))links.append(Link('9', '19', 'g'))links.append(Link('9', '20', 'h'))links.append(Link('9', '21', 'i'))links.append(Link('9', '22', '0'))links.append(Link('9', '23', '1'))links.append(Link('10', '13', 'a'))links.append(Link('10', '14', 'b'))links.append(Link('10', '15', 'c'))links.append(Link('10', '16', 'd'))links.append(Link('10', '17', 'e'))links.append(Link('10', '18', 'f'))links.append(Link('10', '19', 'g'))links.append(Link('10', '20', 'h'))links.append(Link('10', '21', 'i'))links.append(Link('10', '22', '0'))links.append(Link('10', '23', '1'))links.append(Link('11', '24', '0'))links.append(Link('11', '25', '1'))links.append(Link('12', '24', '0'))links.append(Link('12', '25', '1'))links.append(Link('13', '13', 'a'))links.append(Link('13', '14', 'b'))links.append(Link('13', '15', 'c'))links.append(Link('13', '16', 'd'))links.append(Link('13', '17', 'e'))links.append(Link('13', '18', 'f'))links.append(Link('13', '19', 'g'))links.append(Link('13', '20', 'h'))links.append(Link('13', '21', 'i'))links.append(Link('13', '22', '0'))links.append(Link('13', '23', '1'))links.append(Link('14', '13', 'a'))links.append(Link('14', '14', 'b'))links.append(Link('14', '15', 'c'))links.append(Link('14', '16', 'd'))links.append(Link('14', '17', 'e'))links.append(Link('14', '18', 'f'))links.append(Link('14', '19', 'g'))links.append(Link('14', '20', 'h'))links.append(Link('14', '21', 'i'))links.append(Link('14', '22', '0'))links.append(Link('14', '23', '1'))links.append(Link('15', '13', 'a'))links.append(Link('15', '14', 'b'))links.append(Link('15', '15', 'c'))links.append(Link('15', '16', 'd'))links.append(Link('15', '17', 'e'))links.append(Link('15', '18', 'f'))links.append(Link('15', '19', 'g'))links.append(Link('15', '20', 'h'))links.append(Link('15', '21', 'i'))links.append(Link('15', '22', '0'))links.append(Link('15', '23', '1'))links.append(Link('16', '13', 'a'))links.append(Link('16', '14', 'b'))links.append(Link('16', '15', 'c'))links.append(Link('16', '16', 'd'))links.append(Link('16', '17', 'e'))links.append(Link('16', '18', 'f'))links.append(Link('16', '19', 'g'))links.append(Link('16', '20', 'h'))links.append(Link('16', '21', 'i'))links.append(Link('16', '22', '0'))links.append(Link('16', '23', '1'))links.append(Link('17', '13', 'a'))links.append(Link('17', '14', 'b'))links.append(Link('17', '15', 'c'))links.append(Link('17', '16', 'd'))links.append(Link('17', '17', 'e'))links.append(Link('17', '18', 'f'))links.append(Link('17', '19', 'g'))links.append(Link('17', '20', 'h'))links.append(Link('17', '21', 'i'))links.append(Link('17', '22', '0'))links.append(Link('17', '23', '1'))links.append(Link('18', '13', 'a'))links.append(Link('18', '14', 'b'))links.append(Link('18', '15', 'c'))links.append(Link('18', '16', 'd'))links.append(Link('18', '17', 'e'))links.append(Link('18', '18', 'f'))links.append(Link('18', '19', 'g'))links.append(Link('18', '20', 'h'))links.append(Link('18', '21', 'i'))links.append(Link('18', '22', '0'))links.append(Link('18', '23', '1'))links.append(Link('19', '13', 'a'))links.append(Link('19', '14', 'b'))links.append(Link('19', '15', 'c'))links.append(Link('19', '16', 'd'))links.append(Link('19', '17', 'e'))links.append(Link('19', '18', 'f'))links.append(Link('19', '19', 'g'))links.append(Link('19', '20', 'h'))links.append(Link('19', '21', 'i'))links.append(Link('19', '22', '0'))links.append(Link('19', '23', '1'))links.append(Link('20', '13', 'a'))links.append(Link('20', '14', 'b'))links.append(Link('20', '15', 'c'))links.append(Link('20', '16', 'd'))links.append(Link('20', '17', 'e'))links.append(Link('20', '18', 'f'))links.append(Link('20', '19', 'g'))links.append(Link('20', '20', 'h'))links.append(Link('20', '21', 'i'))links.append(Link('20', '22', '0'))links.append(Link('20', '23', '1'))links.append(Link('21', '13', 'a'))links.append(Link('21', '14', 'b'))links.append(Link('21', '15', 'c'))links.append(Link('21', '16', 'd'))links.append(Link('21', '17', 'e'))links.append(Link('21', '18', 'f'))links.append(Link('21', '19', 'g'))links.append(Link('21', '20', 'h'))links.append(Link('21', '21', 'i'))links.append(Link('21', '22', '0'))links.append(Link('21', '23', '1'))links.append(Link('22', '13', 'a'))links.append(Link('22', '14', 'b'))links.append(Link('22', '15', 'c'))links.append(Link('22', '16', 'd'))links.append(Link('22', '17', 'e'))links.append(Link('22', '18', 'f'))links.append(Link('22', '19', 'g'))links.append(Link('22', '20', 'h'))links.append(Link('22', '21', 'i'))links.append(Link('22', '22', '0'))links.append(Link('22', '23', '1'))links.append(Link('23', '13', 'a'))links.append(Link('23', '14', 'b'))links.append(Link('23', '15', 'c'))links.append(Link('23', '16', 'd'))links.append(Link('23', '17', 'e'))links.append(Link('23', '18', 'f'))links.append(Link('23', '19', 'g'))links.append(Link('23', '20', 'h'))links.append(Link('23', '21', 'i'))links.append(Link('23', '22', '0'))links.append(Link('23', '23', '1'))links.append(Link('24', '24', '0'))links.append(Link('24', '25', '1'))links.append(Link('25', '24', '0'))links.append(Link('25', '25', '1'))keywordsNodes.append(Node('1', 'True', 'False'))keywordsNodes.append(Node('2', 'False', 'False'))keywordsNodes.append(Node('3', 'False', 'True'))keywordsLinks.append(Link('1', '2', 'i'))keywordsLinks.append(Link('2', '3', 'f'))
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