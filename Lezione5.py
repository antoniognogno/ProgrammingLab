class CSVFile():
    def __init__(self, file_name):
        self.name = file_name
        try:
            self.file = open(self.name, 'r')
        except Exception as e:
            print("Errore: Questo file non esiste: {}.    Tipo di errore {}".format(self.name, e))
            
    def get_data(self):
        result = []
        values = []
        for line in self.file:
            line = line.split(',')
            if line[0] != 'Date':
                values.append(line)
                result.append(values)
                values.clear
        return values

class NumericalCSVFile(CSVFile):
    def get_data(self):
        linea = 1
        values = super().get_data()
        for value in values:
            linea+=1
            value[0] = value[0].replace("-", "")
            value[0] = float(value[0])
            try:
                value[1] = float(value[1])
            except:
                value[1] = 0
                print("Errore alla linea {}: assegnato valore di default 0".format(linea))
        return values


fileCSVFloat = NumericalCSVFile("shampoo_sales.csv")
values = fileCSVFloat.get_data()
print(values)

