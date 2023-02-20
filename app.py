import numpy as np

class App:
    def __init__(self):
        self.rows: int = self.get_int("Enter row count: ")
        self.matrix: list[list[int]] = self.get_matrix(self.rows)
        self.result: list[list[int]] = self.gauss(self.matrix)

        print("Rezultāts: ", self.result)

    def get_int(self, txt: str = "Enter int: ") -> int:
        num = None

        while num == None:
            try:
                num = int(input(txt))
            except:
                num = self.get_int("Try again: ")

        return num

    def get_matrix(self, rows: int) -> list[list[int]]:
        return [
            [3, -6, 3, -12],
            [2, 3, 4, 8],
            [4, 5, -2, 4]
        ]

        matrix = []

        for _ in range(rows):
            row = [self.get_int() for _ in range(rows+1)]
            matrix.append(row)

        return matrix

    def gauss(self, matrix: list[list[int]]) -> list[int]:
        divider = matrix[0][0]

        print(f"Dividing R0 by {divider}")

        for i in range(len(matrix[0])):
            matrix[0][i] = matrix[0][i] / divider
        
        vector = [item[len(item) - 1] for item in matrix]
        matrix = [item[ : -1] for item in matrix]

        matrix = np.matrix(matrix)
        vector = np.array(vector)
        n = matrix.shape[0]

        print("Starting matrix:")
        print(np.concatenate((matrix, vector.reshape(-1, 1)), axis=1))

        for i in range(n):
            pivot = matrix[i, i]
            if pivot == 0:
                raise ValueError("Can't perform Gaussian elimination: 0 pivot encountered")
            for j in range(i + 1, n):
                factor = matrix[j, i] / pivot
                print(f"{factor}R{i} + R{j}")
                matrix[j, i:] -= factor * matrix[i, i:]
                vector[j] -= factor * vector[i]

            print("After elimination:")
            print(np.concatenate((matrix, vector.reshape(-1, 1)), axis=1))

        x = np.zeros(n)

        for i in range(n - 1, -1, -1):
            s = sum(matrix[i, j] * x[j] for j in range(i + 1, n))
            x[i] = (vector[i] - s) / matrix[i, i]

        return x


_ = App()