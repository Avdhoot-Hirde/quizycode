import random as rd

def repo(lang):            #Function for question repository
    java = [        #Java questions with option and the correct answer
        ["What is the size of `int` in Java?", "8 bits", "16 bits", "32 bits", "64 bits", "c"],
        ["Which of these is not a Java keyword?", "static", "Boolean", "void", "private", "b"],
        ["Java was initially developed by?", "Oracle", "Microsoft", "Sun Microsystems", "IBM", "c"],
        ["What is the default value of a boolean variable?", "true", "false", "null", "0", "b"],
        ["Which method is used to start a thread in Java?", "run()", "start()", "execute()", "init()", "b"],
        ["Which operator is used to allocate memory to an object?", "malloc", "alloc", "new", "mem", "c"],
        ["Which of these is the parent class of all classes in Java?", "String", "Object", "Thread", "System", "b"],
        ["Which of these access specifiers can be used for a class?", "public", "private", "protected", "All of the above", "a"],
        ["Which keyword is used to inherit a class in Java?", "implements", "extends", "inherits", "derives", "b"],
        ["Which of these is used to handle exceptions in Java?", "try-catch", "if-else", "for loop", "switch", "a"],
        ["Which of these is not a feature of Java?", "Object-Oriented", "Platform-independent", "Pointers", "Multithreaded", "c"],
        ["Which of these is a valid way to declare a constant in Java?", "static int PI", "final int PI", "constant int PI", "constant PI", "b"],
        ["Java is a __ programming language.", "low-level", "medium-level", "high-level", "none of the above", "c"],
        ["Which of these is not a type of constructor?", "Default constructor", "Copy constructor", "Parameterized constructor", "Private constructor", "b"],
        ["Which of these is used to define an abstract method?", "abstract", "static", "final", "private", "a"],
        ["What is used to check whether two strings are equal?", "equals()", "== operator", "compare()", "check()", "a"],
        ["Which of these loops is not present in Java?", "for", "foreach", "while", "do-while", "b"],
        ["Which package contains the Random class?", "java.util", "java.lang", "java.io", "java.net", "a"],
        ["Which keyword is used to prevent inheritance in Java?", "static", "final", "const", "super", "b"],
        ["Which exception is thrown when an array is accessed out of bounds?", "NullPointerException", "ArrayIndexOutOfBoundsException", "NumberFormatException", "ClassNotFoundException", "b"]
    ]
    python = [          #Python questions with option and the correct answer
        ["Which of the following is a immutable data type in Python?", "tuple", "list", "str", "int", "a"],
        ["What is the output of: print(type([]))?", "<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>", "a"],
        ["How do you start a comment in Python?", "#", "//", "/*", "<!--", "a"],
        ["What is the correct syntax to output 'Hello World' in Python?", "echo 'Hello World'", "p('Hello World')", "print('Hello World')", "printf('Hello World')", "c"],
        ["What does the `len()` function do?", "Calculates sum", "Finds length", "Returns index", "Sorts elements", "b"],
        ["Which of the following is the correct way to declare a function in Python?", "def myFunc():", "function myFunc() {}", "myFunc() => {}", "myFunc() {};", "a"],
        ["What keyword is used to create a class in Python?", "create", "define", "class", "object", "c"],
        ["How do you create a dictionary in Python?", "{}", "[]", "()", "<>", "a"],
        ["Which of the following is a framework for Python?", "Flask", "Django", "Pyramid", "All of the above", "d"],
        ["Which of the following is not a core data type in Python?", "list", "dictionary", "class", "tuple", "c"],
        ["What is used to handle exceptions in Python?", "try-catch", "try-except", "if-else", "catch-finally", "b"],
        ["Which method is used to return the string in lowercase?", "lower()", "isLower()", "downcase()", "caseDown()", "a"],
        ["How do you create a tuple in Python?", "[1, 2, 3]", "{1, 2, 3}", "(1, 2, 3)", "<1, 2, 3>", "c"],
        ["Which of these is not a Python operator?", "**", "//", "<<<", "is", "c"],
        ["What is the output of: bool('False')?", "False", "True", "SyntaxError", "None", "b"],
        ["Which of the following is used for string formatting in Python?", "%", "&", "#", "$", "a"],
        ["What is the output of: 3*1**3?", "3", "6", "1", "9", "a"],
        ["How do you create a set in Python?", "{}", "[]", "()", "set()", "d"],
        ["Which keyword is used to import modules in Python?", "include", "require", "import", "use", "c"],
        ["How do you access a global variable inside a function in Python?", "global", "public", "extern", "super", "a"]
    ]
    js = [                          #JavaScript questions with option and the correct answer
        ["Which of the following is a JavaScript data type?", "number", "string", "boolean", "All of the above", "d"],
        ["Which symbol is used for comments in JavaScript?", "//", "/*", "#", "<!--", "a"],
        ["How do you declare a variable in JavaScript?", "let", "var", "const", "All of the above", "d"],
        ["What is the correct syntax to output 'Hello World' in an alert box?", "msg('Hello World')", "alertBox('Hello World')", "alert('Hello World')", "msgBox('Hello World')", "c"],
        ["How do you write a function in JavaScript?", "function myFunc()", "def myFunc()", "func myFunc()", "method myFunc()", "a"],
        ["Which operator is used to assign a value to a variable?", "=", "==", "===", "=>", "a"],
        ["How do you add a comment in JavaScript?", "//", "/* */", "#", "<!-- -->", "a"],
        ["Which method is used to add an element at the end of an array in JavaScript?", "append()", "push()", "add()", "insert()", "b"],
        ["How do you find the length of an array in JavaScript?", "length()", "len()", "size()", "length", "d"],
        ["Which function is used to parse a string into an integer in JavaScript?", "int()", "parseInt()", "toInteger()", "Number()", "b"],
        ["What is the output of typeof null?", "'null'", "'undefined'", "'object'", "'string'", "c"],
        ["Which of the following is a JavaScript framework?", "Angular", "Django", "Flask", "Rails", "a"],
        ["Which method is used to remove the last element of an array?", "pop()", "remove()", "delete()", "shift()", "a"],
        ["How do you round a number in JavaScript?", "Math.ceil()", "Math.floor()", "Math.round()", "All of the above", "c"],
        ["What does `===` operator do in JavaScript?", "Checks for equality", "Checks for equality and type", "Assigns value", "None of the above", "b"],
        ["Which method can be used to create a new array from the results of calling a function on every element?", "map()", "forEach()", "filter()", "reduce()", "a"],
        ["What is the output of: console.log('3' + 2);?", "32", "5", "TypeError", "NaN", "a"],
        ["Which object represents the global scope in browsers?", "window", "global", "document", "console", "a"],
        ["Which of the following is not a reserved word in JavaScript?", "interface", "throws", "program", "short", "c"],
        ["How do you write an IF statement in JavaScript?", "if (i == 5)", "if i = 5", "if i == 5 then", "if (i = 5)", "a"]
    ]

    if lang==1:
        return java
    elif lang==2:
        return python
    else:
        return js

def question(opt):                  #Function for showing any 5 of question for the selected language and checking the result and calculating the score
    points=0
    lang=repo(opt)
    que=rd.sample(lang,5)
    print("Each question consist of 1 point")
    for i in range(0,(len(que))):
        Qs=que[i]
        print(f"\nQ{i+1}. {Qs[0]}")
        print()
        print(f"a. {Qs[1]}\tb. {Qs[2]}\nc. {Qs[3]}\td. {Qs[4]}")
        r=input("your answer(a,b,c,d): ")
        print()
        if r==Qs[-1]:
            print("Correct Answer")
            points+=1
            if (i==len(que)-1):
                print(f"Your final score is: {points}")
            else:
                print(f"Current Score is: {points}")
            print()
        else:
            print("Incorrect answer")
            print(f"Current Score is: {points}")

def register():
    print('\n')
    sp=rd.choice(['@','*','_'])
    name=input("Enter your name: ")
    global nm
    nm=name.split(' ')
    age=int(input("Enter your age: "))
    enroll=input("Enter your Enrollment number: ")
    branch=input("Enter your branch: ")
    email=input("Enter your email ID: ")
    passwordv=nm[0]+sp+str(age)
    print(f"your password is: {passwordv}")
    print("Registeration is done.\n\n")
    def choice():
        c=input("Want to login: (yes/no)")
        if c=='yes':
            login(email,passwordv)
        elif c=='no':
            exit()
        else: 
            print("Wrong choice\n\n")
            choice()
    choice()

def login(em,p2):
    email=input("Email ID: ")
    p=input("Enter password: ")
    if p!=p2 or email!=em:
        print("Retry.\n\n")
        login(em,p2)
    else:
        print("1. Take Quiz: \n2. Registration: \n3. Quit: ")
        l=int(input("Enter your choice(1,2,3): "))
        match l:
            case 1:
                domain()
            case 2:
                register()
            case 3:
                exit()


def domain():                           #Function to select the choice for quiz
    print(f"\nWelcome {nm[0]} get ready for the Quiz")
    print("\n1. Java: \n2. Python: \n3. JavaScript: ")
    opt=int(input("Enter field(1,2,3): "))
    match opt:
        case 1:
            question(1)
        case 2:
            question(2)
        case 3:
            question(3)
        case _:
            print("Wrong entry")
            domain()
    retake=input("Want to play again?(yes/no): ")
    if retake=="yes":
        domain()

nm=''
while True:
    print("1. Register: \n2. Quit: ")
    quiz=int(input("Enter your choice(1,2): "))
    match quiz:
        case 1:
            register()
        case 2:
            print("Thankyou")
            break
        case _:
            print("wrong choice")
            break