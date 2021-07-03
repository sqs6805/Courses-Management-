# HW2
#Due Date: 02/20/2021, 11:59PM

"""                                   
### Collaboration Statement:
I completed this with some help from the instructor during office hours
             
"""

import random

class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''
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
    ''' 
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.courseOfferings
        {'CMPSC132': CMPSC132(3): Programming in Python II, 'CMPSC360': CMPSC360(3): Discrete Mathematics}
        >>> C.removeCourse('CMPSC360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC132': CMPSC132(3): Programming in Python II}
        >>> isinstance(C.courseOfferings['CMPSC132'], Course)
        True
    '''
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
    '''
        >>> cmpsc131 = Course('CMPSC131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> semester = Semester(1)
        >>> semester
        No courses
        >>> semester.addCourse(cmpsc132)
        >>> semester.addCourse(math230)
        >>> semester
        CMPSC132, MATH 230
        >>> semester.isFullTime
        False
        >>> semester.totalCredits
        7
        >>> semester.addCourse(phys213)
        >>> semester.addCourse(econ102)
        >>> semester.addCourse(econ102)
        'Course already added'
        >>> semester.addCourse(phil119)
        >>> semester.isFullTime
        True
        >>> semester.dropCourse(phil119)
        >>> semester.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> semester.totalCredits
        16
        >>> semester.dropCourse(cmpsc131)
        'No such course'
        >>> semester.addCourse(Course(42, 'name',"zero credits"))
        'Invalid course'
        >>> semester.courses
        [CMPSC132(3): Programming in Python II, MATH 230(4): Calculus, PHYS 213(2): General Physics, ECON 102(3): Intro to Economics, JAPNS 001(4): Japanese I]
    '''

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
    '''
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.getLoan(4000)
        'Not full-time'
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2)
        'Course added successfully'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC360', C,1)
        'Course added successfully'
        >>> s1.getLoan(4000)
        'Not full-time'
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> s1.getLoan(4000)
        >>> s1.account.loans
        {27611: Balance: $4000}
        >>> s1.getLoan(6000)
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $6000}
    '''
    

    def __init__(self, amount):
        self.amount = amount


    def __str__(self):
        return f"Balance: ${self.amount}"

    __repr__ = __str__


    @property
    def __loanID(self):
        return random.randint(10000, 99999)


class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''

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
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> st1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC360', C, 1)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC132}
    '''
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
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2)
        'Course added successfully'
        >>> C.addCourse('CMPEN270', 'Digital Design', 4)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN270', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
    '''
    
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
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC311', C, 1)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132, CMPSC360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC132', C, 1)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC360', 1)
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC360', 1)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: No courses}
        >>> s1.enrollCourse('CMPSC360', C, 2)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
    '''
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
    """
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> s = createStudent(p)
        >>> s
        Student(Jason Smith, js2629, Freshman)
        >>> isinstance(s, Student)
        True
    """
    return Student(person.name, person.get_ssn(), "Freshman")

