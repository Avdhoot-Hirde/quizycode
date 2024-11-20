import random as rd
def repo(lang):
    with open("q_java.txt","r") as jv:            #Function for calling question repository
        java = jv.readlines()
    with open("q_py.txt",'r') as p:
        python = p.readlines()
    with open('q_js.txt','r') as j:
        js = j.readlines()

    if lang==1:
        return java
    elif lang==2:
        return python
    else:
        return js

def convert(opt):
    lang=repo(opt)
    L=[]
    for i in lang:
        j=i.replace('\n','')
        jl=j.split(',')
        L.append(jl)
    return L

def question(opt):                  #Function for showing any 5 of question for the selected language and checking the result and calculating the score
    points=0
    lang=convert(opt)
    que=rd.sample(lang,5)
    print("Each question consist of 1 point")
    for i in range(0,(len(que))):
        Qs=que[i]
        print(f"\nQ{i+1}. {Qs[0]}")
        print()
        print(f"a. {Qs[1]}\tb. {Qs[2]}\nc. {Qs[3]}\td. {Qs[4]}")
        r=input("your answer(a,b,c,d): ")
        print()
        if r==(Qs[-1].strip()):
            print("Correct Answer")
            points+=1
            if (i==len(que)-1):
                print(f"Your final score is: {points}")
                with open("result.txt",'r') as result:
                    rer=result.readlines()
                for j in rer:
                    ele=j.split(',')
                    if enroll==ele[0]:
                        with open('result.txt','a') as result_in:
                            result_in.write(f',{str(points)}')
                    else:
                        with open('result.txt',"a") as result_n_in:
                            result_n_in.write(f"\n{enroll},{points}")
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
    nm=name.split(' ')
    age=int(input("Enter your age: "))
    enroll=input("Enter your Enrollment number: ")
    branch=input("Enter your branch: ")
    email=input("Enter your email ID: ")
    passwordv=nm[0]+sp+str(age)
    print(f"your password is: {passwordv}")
    print("Registeration is done.\n\n")
    with open("data.txt","a") as datain:
        datain.write(f"{name},{str(age)},{enroll},{branch},{email},{passwordv}\n")
    def choice():
        c=input("Want to login: (yes/no)")
        if c=='yes':
            login()
        elif c=='no':
            exit()
        else: 
            print("Wrong choice\n\n")
            choice()
    choice()

def login():
    global enroll
    enroll=input("Enrollment ID: ")
    p=input("Enter password: ")
    with open("data.txt","r") as dataout:
        detail=dataout.readlines()
    for i in detail:
        line=i.split(',')
        last=line[-1].replace("\n","")
        if(enroll==line[2] and p==last):
            print("LOGINED")
            print("1. Take Quiz: \n2. Quit: ")
            l=int(input("Enter your choice(1,2): "))
            match l:
                case 1:
                    domain()
                case 2:
                    exit()
            break
        elif detail.index(i)==(len(detail)-1):
            if(enroll!=line[2] and p!=line[-1]):
                print("Account not found or wrong entry:")
                print("\n1. Register: \n2. Login: ")
                opt=input("Enter your choice(1,2): ")
                match opt:
                    case '1':
                        register()
                    case '2':
                        login()

        else: 
            continue

def domain():                           #Function to select the choice for quiz
    print(f"\nWelcome get ready for the Quiz")
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

def result():
    en=input("Enter enrollment Number: ")
    with open('result.txt','r') as result:
        r=result.readlines()
    for i in r:
        ele=i.split(',')
        if en==(ele[0].split()):
            for j in range(1,len(ele)):
                print(f"Enrollment: {ele[0]}",end=": ")
                print(f"{j}th: {ele[j]}",end=",")


while True:
    print("\n1. Register: \n2. Login: \n3. Quit: ")
    quiz=int(input("Enter your choice(1,2,3): "))
    match quiz:
        case 1:
            register()
        case 2:
            login()
        case 3:
            print("Thankyou")
            break
        case _:
            print("wrong choice")
            break