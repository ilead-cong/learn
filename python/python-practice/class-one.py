##########################################
#the practice of QiWei python class study
class Student:
    '''
    describe the students'homework
    '''
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject
    def do_work(self, time):
        if self.grade >= 3 and time > 2:
            return True
        elif self.grade < 3 and time > 0.5:
            return True
        else:
            return False

class Teacher:
    '''
    describe the teachers'evaluation to about the students' homework
    '''
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    def evaluate(self, result):
        if result:
            return 'You are great'
        else:
            return 'You should work hard'

stu_zhang = Student('zhang', 5, 'math')
tea_wang = Teacher('wang', 'math')
teacher_said = tea_wang.evaluate(stu_zhang.do_work(1))
print("Teacher{0} said: {1}, {2}".format(tea_wang.name, stu_zhang.name, teacher_said))

stu_newton = Student('Newton', 6, 'physics')
tea_heng = Teacher('heng', 'physics')
teacher_said= tea_wang.evaluate(stu_newton.do_work(4))
print("Teacher{0} said: {1}, {2}".format(tea_wang.name, stu_newton.name, teacher_said))