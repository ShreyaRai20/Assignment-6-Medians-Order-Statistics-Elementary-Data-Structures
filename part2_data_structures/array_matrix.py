"""
Array and Matrix Implementation
"""

class Array:
    def __init__(self):
        self.data = []

    def insert(self, value):
        """Insert element at end"""
        self.data.append(value)

    def delete(self, value):
        """Delete first occurrence"""
        if value in self.data:
            self.data.remove(value)

    def access(self, index):
        """Access element by index"""
        if 0 <= index < len(self.data):
            return self.data[index]
        return None


class Matrix:
    def __init__(self, rows, cols):
        """Initialize matrix with zeros"""
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_value(self, i, j, value):
        self.matrix[i][j] = value

    def get_value(self, i, j):
        return self.matrix[i][j]