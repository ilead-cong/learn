#######################################################
#物理学家作为父类，编写子类‘理论物理学家’和‘实验物理学家’
#######################################

class Physicist:
    '''
    '''
    def __init__(self, name, iq=120, looks='handsom', subject='physics'):
       self.name = name
       self.iq = iq
       self.looks = looks
       self.subject = subject

    def research(self, field):
        print("{0} research {1}".format(self.name, field))

    def speak(self):
        print("My name is ", self.name)
        print("I am ", self.looks)
        print("Intelligence is ", self.iq)
        print("I like ", self.subject)

class ExperimentalPhysicist(Physicist):
    '''
    '''
    def __init__(self, main_study, name, iq=120, looks='handsom', subject='physics'):
        self.main_study = main_study
        super().__init__(name, iq, looks, subject)

    def experiment(self):
        print("{0} is in Physics Lab.".format(self.name))

class TheoreticalPhysicist(Physicist):
    '''
    '''
    def __init__(self, theory, name, iq=120, looks='handsom', subject='physics'):
        self.theory = theory
        super().__init__(name, iq, looks, subject)

    def research(self, field, base):
        super().research(field)
        print("My theory is {0}, it is based on {1}".format(self.theory, base))

einstein = TheoreticalPhysicist('Relativity', 'Albert Einstein', iq=160, looks='handsom', subject='physics')
einstein.speak()
einstein.research('field', 'base')