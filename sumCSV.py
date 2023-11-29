# Inizializzo una lista vuota per salvare i valori
values = []
# Apro e leggo il file, linea per linea
file = open('shampoo_sales.csv', 'r')

for line in file:
    line = line.split(',')

    if line[0] != 'Date':
        values.append(line[1])

sum = 0
for i in values:
    sum += float(i)

print(sum)
