import re

def regular(text): #
    result = re.sub(r'\([^)]*\)', '', text)
    return result

def unregular(text): #первый кет закрывает последний бра
    bra = []
    ket = []
    Bra = 0
    Ket = 0
    for i in range(text.find('('), len(text)):
        if text[i-1] == '(':
            bra.append(i)
        elif text[i-1] == ')':
            ket.append(i)
    for i in range(len(text)):
        if text[i] == '(':
            Bra += 1
        elif text[i] == ')':
            Ket += 1
        if Bra == Ket:
            print(text[i], end='')
    

print(regular("asdflj (kla (inner) asd) port (another ))(unclosed\n"))
unregular("asdflj (kla (inner) asd) port (another ))(unclosed ")