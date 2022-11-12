class Array2D:
    def __init__(self, row, col, clear_value=None, default_val=None):
        self.row = row 
        self.col = col
        self.array = []
        self.default_val = default_val

        for i in range(row + 1):
            self.array.append(self.default_val)
            for k in range(col + 1):
                self.array.append(self.default_val)

        
        table = [['.' for i in range(self.col)] for j in range(self.row)]
        print(table)

    def format_array(table_):
        return "[\n" + ''.join(["\t" + str(line) + ",\n" for line in table_]) + "]"

    def __str__(self):
        #return str(self.array)
        #return self.x
        pass

    def __repr__(self):
        return self.__str__()

    def getitem(self, i, k):
        pass

    def setitem(self, i, k, value):
        pass

    def numRows(self):
        return self.row

    def numCols(self):
        return self.col

    def clear(self, value):
        pass

array = Array2D(5, 5)
print(array)