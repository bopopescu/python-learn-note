from weakref import WeakKeyDictionary


class Grade(object):

    def __init__(self):
        self._value = 0

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Grade must between 0 and 100")
        self._value = value


class Exam(object):
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


exam = Exam()
exam.writing_grade = 82
exam.science_grade = 99
print("Writing", exam.writing_grade)
print("Science", exam.science_grade)

second_exam = Exam()
second_exam.writing_grade = 75
print("Second Writing", second_exam.writing_grade)
print("First Writing", exam.writing_grade)


class UpgradeGrade(object):

    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None: return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Grade must between 0 and 100")
        self._values[instance] = value


class NewExam(object):
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


exam = NewExam()
exam.writing_grade = 82
exam.science_grade = 99
print("Writing", exam.writing_grade)
print("Science", exam.science_grade)

second_exam = Exam()
second_exam.writing_grade = 75
print("Second Writing: ", second_exam.writing_grade)
