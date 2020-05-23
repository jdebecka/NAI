class Confusion_Matrix:
    def __init__(self, acc_class_name):
        self.actual_class_name = acc_class_name
        self.true_pos = 0
        self.true_neg = 0
        self.false_pos = 0
        self.false_neg = 0

    def add_true_pos(self):
        self.true_pos += 1

    def add_true_neg(self):
        self.true_neg += 1

    def add_false_pos(self):
        self.false_pos += 1

    def add_false_neg(self):
        self.false_neg += 1
