
# -> Dictionary analysis:
#
# local:wolkodlack@wdnote:/media/media/proj/DataRobot/wf[0]$ cat words.txt | sed 's/./#/g' | sort | uniq -c
# 64 ##
# 584 ###
# 2329 ####
# 4554 #####
# 7207 ######
# 9808 #######
# 10364 ########
# 9212 #########
# 7328 ##########
# 5010 ###########
# 3173 ############
# 1777 #############
# 788 ##############
# 369 ###############
# 136 ################
# 61 #################
# 22 ##################
# 6 ###################
# 3 ####################
# 2 #####################
# 2 ######################
#


class DictLoader:
    _file_name = 'words.txt'
    _data = {}

    def __init__(self, name):
        """
        Init
        :param name:
        """
        self.file_name = name
        self._load()

    def _load(self):
        """
        Loads dictionary from file
        :return:
        """
        with open(self.file_name) as fp:
            for line in fp:
                _len = len(line) - 1
                if _len not in self._data.keys():
                    self._data[_len] = []
                self._data[_len].append(line.strip())

                # print("Line: {}:{}".format(_len, line))

        print('Dictionary statistics:')
        for key in sorted(self._data.keys()):
            c = len(self._data[key])
            print("word length:{} -> count words:{}".format(str(key).ljust(2), c))
        print()

    def search(self, word):
        """
        Does search word in dictionary
        :param word:
        :return:
        """
        length = len(word)

        if length in self._data.keys():
            if word in self._data[length]:
                return True

        return False

