class Level:
    def __init__(self, level_name):
        self.level_name = level_name
        self.board = list()
        with open(level_name) as map:
            lines = map.readlines()
            for line in lines:
                temp = list()
                for item in line:
                    temp.append(item)
                self.board.append(temp)