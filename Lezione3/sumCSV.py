#10/10 points

#Scrivete una funzione sum_csv(file_name)
#che sommi tutti i valori delle vendite degli
#shampoo del file passato come argomento

def sum_csv(file_name):
    values = []
    file = open(file_name, 'r')
    for line in file:
        #remove \n
        line = line.strip()
        
        elements = line.split(',')

        if elements[0] != 'Date':
            # Setto il valore
            value = elements[1]
            try:
                value = float(value)
                values.append(value)
            except:
                pass
    if not values:
        return None
    return sum(values)

