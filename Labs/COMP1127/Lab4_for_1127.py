
''' Details of the student record st1, the dictionaries and functions'''
def myzip(lst1,lst2):
    if lst1 ==[] or lst2 == []:
        return []
    else:
        return [(lst1[0],lst2[0])] + myzip(lst1[1:],lst2[1:])

def student(sid,fname,lname, crses):
    """Constructor for student"""
    courses = []
    while crses != []:
        courses += [(crses[0],crses[1])]
        crses = crses[2:]
    return [sid,[fname,lname],courses]

def get_id(std):
    """Returns students ID"""
    return std[0]

def get_name(std):
    """Returns students Name"""
    return std[1]

def get_courses(std):
    """Returns a list of tuples of course codes and grade"""
    return std[2]

def get_fname(name):
    """Returns first name"""
    return name[0]

def get_lname(name):
    """Returns last name"""
    return name[1]

def get_ccode(course_det):
    """Returns course code part of the tuple"""
    return course_det[0]

def get_grade(course_det):
    """Returns grade part of the tuple"""
    return course_det[1]

#A student record for Jane Doe
st1 = student('620000101',
        "Jane","Doe",
        ["COMP1126",80, "COMP1127",60, 
        "COMP1210",50,"COMP1161",60,
        "COCR2003",85,"COMP2140",80])

#A dictionary of course codes as keys and their corresponding credit values
credit_list={   'COMP1126':3,
                'COMP1127':3,
                'COMP1161':3,
                'COMP1210':3,
                'COMP1220':3,
                'COMP2140':3,
                'COMP2111':3,
                'COCR2003':1    }

#A dictionary with letter grades as keys and their quality points
qp_list = {"A+":4.3,"A":4.0,"A":3.7,"B+":3.3,"B":3.0,"B":2.7,"C+":2.3,\
"C":2.0,"F1":1.7,"F2":1.3,"F3": 0.0}

#A function that performs an operation on each element in a list
def my_map(f,lst):
    if lst == []:
        return []
    else:
        return [f(lst[0])] + my_map(f, lst[1:])

# A function that prints a student’s details including GPA. It needs function calcGPA
# def print_students_gpa(std):
# #Prints the students details and GPA'''
#     print ("Student Id:", get_id(std))
#     print ("Student name:", get_fname(get_name(std)), get_lname(get_name(std)))
#     print ("GPA: %.2f" %(calcGPA(std)))

'''Write a function computeLetterGrade() which takes a number grade and returns the
corresponding letter grade'''
def computeLetterGrade(Grade):
    #implementing grade function with match case:
    if Grade > 89:
            return ("A+")
    elif Grade >= 80:
            return ("A")
    elif Grade >= 75:
            return ("A-")
    elif Grade >= 70:
            return ("B+")
    elif Grade >= 65:
            return ("B")
    elif Grade >= 60:
            return ("B-")
    elif Grade >= 55:
            return ("C+")
    elif Grade >= 50:
            return ("C")
    elif Grade >= 45:
            return ("F1")
    elif Grade >= 40:
            return ("F2")
    elif Grade >= 0:
            return ("F3")
    else:
        raise ValueError("Invalid grade")
#print (computeLetterGrade(100))

'''QUestion 2: Write a function calcLetterGrade() which takes a student as input and returns a list
of tuples where the first part of the tuple is the course code and second part of 
the tuple is the letter grade

From the student structure, first extract the course list which is a list of tuples of course
codes and the number grades. 

Get the number grades from the course list and create a new
list in which each number grade is converted to a letter grade. 

Recreate a new courses list with the list of courses and the list of letter grades. '

Example: >>> calcLetterGrade(st1)
[('COMP1126', 'A'), ('COMP1127', 'B-'), ('COMP1210', 'C'),
('COMP1161', 'B-'), ('COCR2003', 'A'), ('COMP2140', 'A')]'''
#*  Hint: Use my_map to apply a function to every element of the list. Also remember that zip
#*  takes two lists as inputs and creates a list of tuples e.g.


def calcLetterGrade(student):
    #* returns a list of tuples of course CODES & GRADES
    Course_List = get_courses(student)
    
    #* iterates and unpacks the grades from CourseList tuple
    #* underscore (_) indicates that 1st part of tuple isnt needed
    Number_Grades = [grades for (_, grades) in Course_List] # assigns 1st elmt to _ & 2nd elmnt to grades
    
    #* applies computeLetterGrade func to each index in grade lst
    Letter_Grades = list(my_map(computeLetterGrade,Number_Grades))
    
    # New list with list of courses + list of letter grades
    NewCourseList = list(myzip([Course_Tuple[0] for Course_Tuple in Course_List], Letter_Grades))
    return NewCourseList
    #print(calcLetterGrade(st1))


def convert_to_wtqp(codegrade):
    result1 = 0
    result2 = 0
    
    for my_key_cc,my_value_cc in credit_list.items():
        if my_key_cc == get_ccode(codegrade).upper():
            result1 = my_value_cc
 
            
    for my_key_lgrade,my_value_lgrade in qp_list.items():
        if my_key_lgrade == get_grade(codegrade):
            result2 = my_value_lgrade
            
    return (result1,result2)
 
 
def calc_gpa(std):
    cc_grade_point = []
    cc_credit_weight = []
    cc_lgrade_value = []
    result = 0
 
    lst_cc_lgrade = calc_letter_grade(std)
 
    for i in lst_cc_lgrade:
        cc_lgrade_value.append(convert_to_wtqp(i))
    
    for i in cc_lgrade_value:
        cc_grade_point.append(i[0]*i[1])
    
    for i in cc_lgrade_value :
        cc_credit_weight.append(i[0])
 
         
    result=(sum(cc_grade_point)/sum(cc_credit_weight))
 
    return result