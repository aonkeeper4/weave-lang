class Token:

    def __init__(self, t, val=""):
        self.type = t
        self.val = val

    def __str__(self):
        return "Token({}, {})".format(self.type, self.val)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.val == '' or other.val == '':
            return self.type == other.type
        else:
            return self.type == other.type and self.val == other.val

    def __hash__(self):
        return hash(self.type) + hash(self.val)
