

import random

class Course:
    
    def __init__(self, cid, cname, credits):
        self.cid=cid
        self.cname=cname
        self.credits=credits


    def __str__(self):
        return f"{self.cid}({self.credits}): {self.cname}"

    __repr__ = __str__

    def __eq__(self, other):
        if other==None:
            return False
        if self.cid==other.cid:
            return True
        return False



class Catalog:
    
    def __init__(self):
        self.courseOfferings={}

    def addCourse(self, cid, cname, credits):
        if cid not in self.courseOfferings:
            self.courseOfferings[cid]=Course(cid, cname, credits)
            return "Course added successfully" 
        return "Course already added"

    def removeCourse(self, cid):
        if cid in self.courseOfferings:
            del self.courseOfferings[cid]
            return "Course removed successfully"
        return "Course not found"


class Semester:
    

    def __init__(self, sem_num):
        self.sem_num = sem_num
        self.courses = []



    def __str__(self):
        if len(self.courses) == 0:
            return "No courses"
        list1 = []
        for element in self.courses:
            list1.append(element.cid)
        return ", ".join(list1)

    __repr__ = __str__

    def addCourse(self, course):
        if isinstance(course, Course)==False or type(course.cid) != str or type(course.cname) != str or type(course.credits) != int:
            return "Invalid course"
        if course not in self.courses:
            self.courses.append(course)
            return None
        return "Course already added"

    def dropCourse(self, course):
        if isinstance(course, Course)==False or type(course.cid) != str or type(course.cname) != str or type(course.credits) != int:
            return "Invalid course"
        if course not in self.courses:
            return "No such course"
        if course in self.courses:
            self.courses.remove(course)

    @property
    def totalCredits(self):
        list1 = []
        for element in self.courses:
            list1.append(element.credits)
        k = sum(list1)
        return k

    @property
    def isFullTime(self):
        if self.totalCredits >= 12:
            return True
        return False

    
class Loan:
    

    def __init__(self, amount):
        self.amount = amount


    def __str__(self):
        return f"Balance: ${self.amount}"

    __repr__ = __str__


    @property
    def __loanID(self):
        return random.randint(10000, 99999)


class Person:
    

    def __init__(self, name, ssn):
        self.name = name
        self.__ssn = ssn

    def __str__(self):
        return f"Person({self.name}, ***-**-{self.__ssn[7:11]})"

    __repr__ = __str__

    def get_ssn(self):
        return self.__ssn

    def __eq__(self, other):
        if other == None:
            return False
        if self.__ssn == other.__ssn:
            return True
        return False

class Staff(Person):
    
    def __init__(self, name, ssn, supervisor=None):
        self.supervisor = supervisor
        super().__init__(name, ssn)


    def __str__(self):
        return f"Staff({self.name}, {self.id})"

    __repr__ = __str__


    @property
    def id(self):
        i = 0
        k = 0
        while i + 1 < len(list(self.name)):
            if list(self.name)[i] == ' ':
                k = list(self.name)[i + 1].lower()
            i = i + 1
        return '905' + str(self.name[0].lower()) + str(k) + str(
            self.get_ssn()[7:11])

    @property   
    def getSupervisor(self):
        return self.supervisor

    def setSupervisor(self, new_supervisor):
        self.supervisor = new_supervisor
        return "Completed!"


    def applyHold(self, student):
        student.hold = False
        return "Completed!"

    def removeHold(self, student):
        student.hold = True
        return "Completed!"

    def unenrollStudent(self, student):
        student.active = False
        return "Completed!"


class StudentAccount:
    
    
    price_credit=1000
    def __init__(self, student):
        self.student = student
        self.balance = 0
        self.loans = {}


    def __str__(self):
        return f"Name: {self.student.name}\nID: {self.student.id}\nBalance: ${self.balance}"

    __repr__ = __str__


    def makePayment(self, amount):
        self.balance -= amount
        return self.balance


    def chargeAccount(self, amount):
        self.balance += amount
        return self.balance



class Student(Person):
    
    def __init__(self, name, ssn, year):
        random.seed(1)
        self.year = year
        self.semesters = {}
        self.hold = True
        self.active = True
        self.account = self.__createStudentAccount()
        super().__init__(name, ssn)


    def __str__(self):
        return f"Student({self.name}, {self.id}, {self.year})"

    __repr__ = __str__

    def __createStudentAccount(self):
        if self.active == True:
            return StudentAccount(self)


    @property
    def id(self):
        i = 0
        k = 0
        while i + 1 < len(list(self.name)):
            if list(self.name)[i] == ' ':
                k = list(self.name)[i + 1].lower()
            i = i + 1
        return (self.name[0]).lower() + str(k) + self.get_ssn()[7:11]

    def registerSemester(self):
        if self.active == False or self.hold == False:
            return "Unsuccessful operation"
        self.semesters[len(self.semesters) +
                       1] = Semester(len(self.semesters) + 1)
        if len(self.semesters) == 1 or len(self.semesters) == 2:
            self.year = "Freshman"
        elif len(self.semesters) == 3 or len(self.semesters) == 4:
            self.year = "Sophomore"
        elif len(self.semesters) == 5 or len(self.semesters) == 6:
            self.year = "Junior"
        else:
            self.year = "Senior"



    def enrollCourse(self, cid, catalog, semester):
        if cid not in catalog.courseOfferings:
            return "Course not found"

        for element in self.semesters[semester].courses:
            if element.cid == cid:
                return "Course already enrolled"

        if self.hold == True and self.active == True:
            self.semesters[semester].addCourse(catalog.courseOfferings[cid])
            self.account.chargeAccount((self.account.price_credit) *
                                       catalog.courseOfferings[cid].credits)
            return "Course added successfully"

        if self.hold == False or self.active == False:
            return "Unsuccessful operation"

    def dropCourse(self, cid, semester):
        if self.hold == False or self.active == False:
            return "Unsuccessful operation"
        for element in self.semesters[semester].courses:
            if element.cid == cid:
                self.semesters[semester].dropCourse(element)
                return "Course dropped successfully"
        return "Course not found"

    def getLoan(self, amount):
        if self.active == False:
            return "Unsuccessful operation"
        if len(self.semesters) == 0:
            return "Not full-time"
        if self.semesters[len(self.semesters)].isFullTime == False:
            return "Not full-time"
        if self.active == True and self.semesters[len(
                self.semesters)].isFullTime == True:
            x = Loan(amount)
            self.account.loans[x._Loan__loanID] = x
            self.account.makePayment(amount)



####################### STAND ALONE FUNCTION ###############################################


def createStudent(person):
    
    return Student(person.name, person.get_ssn(), "Freshman")

