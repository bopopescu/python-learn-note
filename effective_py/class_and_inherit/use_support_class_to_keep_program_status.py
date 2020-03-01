import collections

'''
    尽量用辅助类来维护程序的状态，不要用字典和元组

    python内置的字典类型可以很好地保存某个对象在其生命周期的动态内部状态

    所谓动态， 是指这些待保存的信息，其标识符无法提前获知，
    例如，要把许多学生的成绩记录下来，但这些学生的名字，我们事先并不知道，
    于是，可以定义一个类，把学生名字全部保存到字典里面，这样就不用把每个学
    生都表示成对象了，也无需在每个对象中预设一个存放其名字的属性
'''


class SimpleGradeBooK(object):

    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)


book = SimpleGradeBooK()
book.add_student("Issac Newton")
book.report_grade("Issac Newton", 90)
print(book.average_grade("Issac Newton"))

'''
    由于字典用起来很方便，所以有可能因为功能过分膨胀而导致代码出问题，
    例如，要扩充SimpleGradeBook类，使它能够按照科目来保存成绩，而不是像
    原来那样，把所有科目的成绩都保存到一起，要实现这个功能，可以修改_grade
    字典的结构，把每个学生的名字与另外一份字典关联起来，使得学生的名字成为
    _grades字典中每个条目的键，使得另外的那份字典成为改键值所对应的值，
    然后，在另外那份字典中，把每个科目当作键，把该科目下的各项值当作值，
    建立映射关系
'''


class BySubjectGradebook(object):

    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade_list)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count


# 不要使用包含字典的字典
"""
    nametuple 的局限

    尽管nametuple在很多场合都非常有用，但是一定要知道，有些时候使用nametuple反而不好

    namedtuple类无法指定各个参数的默认值，对于可选属性比较多的数据来说，namedtuple用起来
    很不方便，如果这些数据并不是一系列简单的属性，那还是定义自己的类比较好
"""

Grade = collections.namedtuple("Grade", ("score", "weight"))


class Subject(object):

    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student(object):

    def __init__(self):
        self._subject = {}

    def subject(self, name):
        if name not in self._subject:
            self._subject[name] = Subject()
        return self._subject[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subject.values():
            total += subject.average_grade()
            count += 1
        return total / count


class GradeBook(object):

    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]


book = GradeBook()
albert = book.student("Albert Einstein")
math = albert.subject("Math")
math.report_grade(80, 0.10)
print(albert.average_grade())

'''
    不要使用包含其他字典的字典，也不要使用过长的元组

    如果容器中包含简单而又不可变的数据，那么可以先使用namedtuple来表示，
    待稍后由需要时，再修改为完整的类

    保存内部状态的字典如果变得比较复杂，那就应该把这些代码拆解为多个辅助类

'''
