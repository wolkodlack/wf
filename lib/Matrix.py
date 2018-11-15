

import random
import string


class Matrix:
    """
    
    """
    size = None

    _data = []

    def __init__(self, size):
        self.size = size
        self._generate()
        self.dump()

    @staticmethod
    def _get_letter():
        """
        Just content generator.
        :return:
        """
        return random.choice(string.ascii_letters)

    def _generate(self):
        """
        Generates matrix with random context. Size defined in the instance.
        :return:
        """
        for h in range(0, self.size):
            self._data.append([])
            for w in range(0, self.size):
                self._data[h].append(self._get_letter())

    def dump(self):
        """
        Pretty matrix dumper
        :return:
        """
        print("Matrix generated:")
        head = " ".join(str(i).rjust(2) for i in range(0, self.size))
        print("   ", '  |', head)

        for num, line in enumerate(self._data):
            print(str(num).rjust(3, ' '), " -> ", end='')
            for ch in line:
                print(" {} ".format(ch), end='')
            print()

    def get_line(self, line_number):
        """
        Returns line of matrix by it num from top to bottom.
        :param line_number:
        :return:
        """
        if line_number < 0 or line_number > len(self._data):
            return ""

        line = self._data[line_number]
        return ''.join(line)

    def get_column(self, column_number):
        """
        Returns column of matrix by it num from top to bottom.
        :param column_number:
        :return:
        """
        if column_number < 0 or column_number > self.size:
            return ""

        column = [row[column_number] for row in self._data]

        return ''.join(column)

    def get_row_lt_rb(self, row):
        """
        Returns data from diagonal row. I.e. from left-top to right-bottom.
        :param row:
        :return:
        """

        # print("i:{} j:{}".format(i, j))
        word = ''
        if row < self.size:
            c = 0
            r = row
            while c < self.size:
                word += self.get_char(r, c)
                # print("line:{} col:{} row:{} --> {}".format(row, c, r, word) )

                if row < self.size:
                    c += 1
                    r -= 1

                if r < 0:
                    break
        else:
            c = row - self.size + 1
            r = self.size - 1
            while c < self.size:
                # print(" >>> line:{} col:{} row:{} --> ".format(row, c, r) )
                word += self.get_char(r, c)
                # print("line:{} col:{} row:{} --> {}".format(row, c, r, word) )

                c += 1
                r -= 1

        return word

    def get_char(self, h, w):
        return self._data[h][w]
