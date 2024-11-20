import random as rd
import psycopg2 as ps

def repo(lang):            #Function for question repository
    q='select * from java'
    cur.execute(q)
    java=cur.fetchall()
    q='select * from python'
    cur.execute(q)
    python=cur.fetchall()
    q='select * from js'
    cur.execute(q)
    js=cur.fetchall()

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
                query="update player set points=%s"
                val=(points,)
                cur.execute(query,val)
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
    enroll=input("Enter your Enrollment number: ").upper()
    branch=input("Enter your branch: ").upper()
    email=input("Enter your email ID: ")
    passwordv=nm[0]+sp+str(age)
    query='insert into player values(%s,%s,%s,%s,%s,%s,0)'
    val=(name,age,enroll,branch,email,passwordv)
    cur.execute(query,val)
    con.commit()
    print(f"your password is: {passwordv}")
    print("\nRegisteration is done.\n\n")
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

def opt(enroll):
    print("1. Take Quiz: \n2. Registration: \n3. Change password: \n4. Details: \n5. Edit Profile: \n6. Remove account: \n7. Quite: ")
    l=int(input("Enter your choice(1,2,3,4,5,6,7): ")) 
    match l:
        case 1:
            domain()
        case 2:
            register()
        case 3:
            changepass(log,enrol_log,pname)
        case 4:
            show(log,enrol_log)
        case 5:
            edit(log,enrol_log)
        case 6:
            remove(log,enrol_log)
        case 7:
            exit()

def login():
    global enrol_log, log,pname
    enroll=input("Enter enrollment number: ").upper()
    query='select password,name from player  where enroll=%s'
    val=(enroll,)
    cur.execute(query,val)
    data=cur.fetchone()
    pname=data[1]
    if len(data[0])> 0:
        p=input("Enter password: ")
        if  p!=data[0]:
            print("Wrong password\nRetry.\n\n")
            login()
        else:
            enrol_log=enroll
            log = True
            print('\n Logged In\n')
            opt(enroll)
            
            
    else: print("Wrong username")
    con.commit()

def changepass(loged,enrol,name):
    if loged==False:
        print("Login first: ")
        login()
    else:
        pswd=input("Enter  new password: ")
        query="update player set password=%s where  enroll=%s"
        val=(pswd,enrol)
        cur.execute(query,val)
        con.commit()
        print(f"{name} your password is changed: ")
        opt(enrol)
        

def show(loged,enrol):
    if loged==False:
        print("Login first: ")
        login()
    else:
        query="select name,enroll,age,branch,email from player where enroll=%s"
        val=(enrol,)
        cur.execute(query,val)
        data=cur.fetchone()
        # for i in data:
        print(data)
        con.commit()
        opt(enrol)

def edit(loged,enroll):
    if loged==False:
        print("Login first: ")
        login()
    else:
        print("Enter detail to edit profile: ")
        print("\n1.Name: \n2. Age: \n3. Email ID: \n4: All: ")
        opt=int(input("Enter choice: "))
        match(opt):
            case 1:
                name=input("Enter name: ")
                query="update player set name=%s where enroll=%s"
                val=(name,enroll)
                cur.execute(query,val)
                con.commit()
                print("Name is updated: ")
            case 2:
                age=int(input("Enter age: "))
                query="update player set age=%s where enroll=%s"
                val=(age,enroll)
                cur.execute(query,val)
                con.commit()
                print("Age is updated: ")
            case 3:
                mail=input("Enter mail: ")
                query="update player set email=%s where enroll=%s"
                val=(mail,enroll)
                cur.execute(query,val)
                con.commit()
                print("Email is updated: ")
            case 4:
               name=input("Enter name: ")
               age=int(input("Enter age: "))
               mail=input("Enter mail: ") 
               query="update player set name=%s,age=%s,email=%s where enroll=%s"
               val=(name,age,mail,enroll)
               cur.execute(query,val)
               con.commit()
               print("All details are updated: ")
        opt(enroll)

def remove(loged,enroll):
    if loged==False:
        print("Login first: ")
        login()
    else:
        query="delete from player where enroll=%s"
        val=(enroll,)
        cur.execute(query,val)
        con.commit()
        print("Account deleted👍\n")
        opt(enroll)




def result():
    en=input("Enter enrollment Number: ")
    query="select points from player where enroll=%s"
    val=(en,)
    cur.execute(query,val)
    p=cur.fetchone()
    print(f'Points scored in last game is: {p[0]}')
    con.commit()

def domain():                           #Function to select the choice for quiz
    print(f"\nWelcome {pname} get ready for the Quiz")
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

if __name__=="__main__":
    global log,pname
    log=False
    con=ps.connect(database='postgres',user='postgres',password='avd',port='5432')
    cur=con.cursor()
    while True:
        print("\n1. Register: \n2. Login: \n3. Score: \n4. Quit: ")
        quiz=int(input("Enter your choice(1,2,3): "))
        match quiz:
            case 1:
                register()
            case 2:
                login()
            case 3:
                result()
            case 4:
                print("Thankyou")
                break
            case _:
                print("wrong choice")
                break