class Analysis:
    def __init__(self, shield):
        self.shield = shield

    def get_result(self):
        pass

class SimpleAnalysis(Analysis):
    def get_result(self):
        result_str = "Your judge is {}. The right witness is {}. The left witness is {}.".format(self.shield.judge.get_name(),
                                                                                                 self.shield.right_witness.get_name(),
                                                                                                 self.shield.left_witness.get_name())
        return result_str