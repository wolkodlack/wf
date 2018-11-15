

class Searcher:
    """
    Searcher class
    """

    _matrix = None
    _dictionary = None

    def __init__(self, matrix, dictionary):
        """

        :param matrix:
        :param dictionary:
        """
        self._matrix = matrix
        self._dictionary = dictionary

    def search(self):
        """
        Combines search types
        :return:
        """

        self._search_in_lines()
        self._search_in_columns()
        self._search_lt_rb()

    def _search_in_lines(self):
        """
        Searches in Lines
        :return:
        """
        print(" # Line search")
        for line_num in range(0, self._matrix.size):
            line = self._matrix.get_row(line_num)
            self._line_search(line_num, line)

    def _search_in_columns(self):
        """
        Search in columns
        :return:
        """
        print(" # Column search")
        for col_num in range(10, self._matrix.size):
            column = self._matrix.get_column(col_num)
            self._line_search(col_num, column)

    def _search_lt_rb(self):
        """
        Searches form left-top to right-bottoms
        :return:
        """
        print(" # Search LeftTop -> RightBottom")
        word = ''
        for num in range(0, self._matrix.size):
            line = self._matrix.get_diagonal_lt_rb(num)
            self._line_search(num, line)

        for num in range(self._matrix.size, self._matrix.size * 2 - 1):
            line = self._matrix.get_diagonal_lt_rb(num)
            self._line_search(num, line)

        return word

    def _line_search(self, line_num, line):
        """
        Dose search in string buffer.
        :param line_num:
        :param line:
        :return:
        """
        # print('(lineNum:{}) line: {}'.format(line_num, line))

        length = len(line)
        for start in range(0, length):
            for end in range(start + 1, length + 1):
                word = line[start:end]
                # print(' <- start:{} end:{}  --> word:{}'.format(start, end, word))

                w = self._dictionary.search(word)
                if w:
                    print("Found(lineNum:{}) word:'{}' at ({}..{}) in: {}"
                          .format(line_num, word, start, end - 1, line))

