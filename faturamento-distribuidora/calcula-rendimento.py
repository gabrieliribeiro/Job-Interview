import json

f = open('./faturamento-distribuidora/informacoes.json')
data = json.load(f)

aux = 0
bigger = 0
smaller = 0
add = 0
average = 0

for day in data:
    if (day['value']) != 0:
        aux = day['value']
        if(aux>bigger):
            bigger=aux
        elif (smaller==0):
            smaller = aux
        elif(aux<smaller):
            smaller=aux
        add+=day['value']

print("O maior valor do faturamento do mês foi: R$", bigger, ".")
print("O menor valor do faturamento do mês foi: R$", smaller, ".")

average = add/len(data)

billedDays = ''

for i in data:
    if (i['value'])!=0:
        if(i['value'])>average:
            billedDays += (str(i['day']) + ' ')
        