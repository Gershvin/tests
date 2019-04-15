import re

def regular(text): #
    result = re.sub(r'\([^)]*\)', '', text) #напрямую ищется элемент вне скобок с помощью регулярных выражений
    return result

def unregular(text): #удаление текста из скобок без регулярных выражений
    """
Логика функции: Бра - открывающая скобка, Кет - закрывающая скобка
Последний кет закрывает текст перед последний бра

Программа удаляет текст в скобках, если:
1) в тексте встретилась первая бра
2) если бра = кет
    """
    Bra = 0
    Ket = 0
    for i in range(len(text)):
        if text[i] == '(':
            Bra += 1
        elif text[i] == ')':
            Ket += 1
        if Bra == Ket:
            print(text[i], end='')
    

print(regular("asdflj (kla (inner) asd) port (another ))(unclosed\n"))
unregular("asdflj (kla (inner) asd) port (another ))(unclosed ")