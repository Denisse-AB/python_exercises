class Ruler:
    def __init__(self, word, inches):
        self.word = word
        self.inches = inches

    def __add__(self, other):
        w = self.word +'-'+ other.word
        i = self.inches + other.inches
        return Ruler(w, i)

    def __str__(self):
        return str(self.word) + "'" + str(self.inches) + '"'

r1 = Ruler('hello', 9.3)
r2 = Ruler('world', 7.2)
r3 = r1 + r2
print(r3)