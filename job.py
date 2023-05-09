from pprint import pprint

with open('file1.txt', 'rt', encoding = 'utf-8') as file:    
    dishes = {}
    for ln in file:
        dishes_name = ln.strip()
        quantity = int(file.readline())
        Ingredients = []
        for r in range(quantity):  
            Name, weight, units = file.readline().strip().split(' | ')
            Ingredients.append({'Name': Name, 'weight': weight , 'units': units})
        file.readline()
        dishes[dishes_name] = Ingredients 
pprint(dishes, sort_dicts=False)  



#..........................................2 задание..........................



cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }

def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for dish in dishes:    
        if dish in cook_book:
            for ing in cook_book[dish]:  
                ing['quantity'] *= person_count
                hap_d = ing.pop('ingredient_name')
                res[hap_d] = ing
    return res             

r = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(r)

# ................3 задача.................................


def rt(rty):
    with open(rty, encoding= 'utf=8') as f1: 
        y = f1.read()
        return y                  
r = ['1.txt', '2.txt', '3.txt'] 
bn = {}
for u in r:           
    line_count = sum(1 for line in open(u, encoding= 'utf=8'))    
    h = rt(u)    
    bn[u] = [line_count, h]    
sorted_dict = {}  
sorted_keys = sorted(bn, key=bn.get)
for w in sorted_keys:
   sorted_dict[w] = bn[w]
for key, value in sorted_dict.items():
    print(key)
    for kl in value:
        print(kl)
