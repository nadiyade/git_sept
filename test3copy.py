# Функция получает на вход длинную строку с множеством слов. Она должна вернуть ту же строку, но в словах, 
#которые длиннее 6 символов,функция должна вместо всех символов после шестого поставить одну звездочку.

a = str(input('Введите предложение.\n'))

def shortener(string):
  result = ''
  s = string.split()
  for elem in s:
    if len(elem) <= 6:
      elem = elem +' '
    else:
      elem = elem[0:6] + '*' + ' '
    result = result + str(elem)
  return result
b = str(shortener(a))
print(b)
