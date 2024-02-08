#9/10 points

# Create un oggetto CSVFile che rappresenti un file CSV, e che:
# 1) venga inizializzato sul nome del file csv, e
# 2) abbia un attributo “name” che ne contenga il nome
# 3) abbia un metodo “get_data()” che torni i dati dal file CSV come lista di liste, 
# ad es: [ ['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ... 

class CSVFile():
    def __init__(self, name):
        self.name = name

    def get_data(self):
        list = []
        file = open(self.name, 'r')
        for line in file:
            #remove \n
            line = line.strip()
            elements = line.split(',')
            
            if elements[0] != 'Date':
                list.append(elements)
        
        if not list:
            return None
        return list