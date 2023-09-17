import pprint as PP 
from textwrap import indent
    

def my_cook_book():
    with open('recept.txt', encoding='utf-8') as file:
        cook_book = {}
        for txt in file.read().split('\n\n'):
            name, _, *args = txt.split('\n')
            tmp = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                tmp.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = tmp
    return cook_book
PP.pprint(my_cook_book(), indent = 2, width = 4)

def call_funcion( ):
   cook_book = my_cook_book()
   return cook_book
print (call_funcion( ))