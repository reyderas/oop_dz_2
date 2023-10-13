dic = {}
for i in open('katalog.txt'):
    with open(i.strip(), encoding='utf-8') as file:
        lst = file.readlines()
        count_row = len(lst)
        dic[i.strip()] = count_row
lst = sorted(dic.items(), key=lambda x: x[1])
for i, j in lst:
    with open(i, encoding='utf-8') as file:
        s = file.read()
    with open('result.txt', 'a', encoding='utf-8') as file:
        head = f'\n{i}\n{j}\n{s}\n'
        file.write(head)
jg