class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def is_passing(self):
        return self.score >= 50


s1 = Student("Amna", 72)
s2 = Student("Bilal", 41)

print(s1.name, s1.is_passing())
print(s2.name, s2.is_passing())

s3 = Student("Zain", 50)
print(s3.name, s3.is_passing())
