class CSVFile():
    def __init__(self, file_name):
        self.name = file_name
        self.file = open(self.name, 'r')

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
        
fileCSV = CSVFile("shampoo_sales.csv")
print(fileCSV.get_data())