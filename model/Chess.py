from model import Rules


class Chess():
    def __init__(self, rule=Rules.default):
        self.init_board(rule.initial_position)

    def init_board(self, initial_position):
        pass

    def move(self, source_pos, target_pos):
        self.is_valid(source_pos, target_pos)
        pass

    def is_valid(self, source_pos, target_pos):
        """
        Checks the validity of the move with the given self.rule
        :param source_pos:
        :param target_pos:
        :return:
        """
        pass