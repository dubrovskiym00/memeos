import math
def calc():
    calc42=float(input(""))
    calc24=float(input(""))
    calc1375=calc42*calc24
    print(calc1375)
def calc1():
    calc42=float(input(""))
    calc24=float(input(""))
    calc1375=calc42+calc24
    print(calc1375)
def calc2():
    calc42=float(input(""))
    calc24=float(input(""))
    calc1375=calc42/calc24
    print(calc1375)
def calc3():
    calc42=float(input(""))
    calc24=float(input(""))
    calc1375=calc42-calc24
    print(calc1375)
def calcinfo():
    print("calc -> калькулятор(умножение)")
    print("calc1 -> калькулятор(плюс)")
    print("calc2 -> калькулятор(деление)")
    print("calc3 -> калькулятор(минус)")
def cost():
    costitem=float(input("Сколько стоит 1 вещь?"))
    cost1=float(input("Сколько хотите купить?"))
    costvariation=costitem*cost1
    print(costvariation)
    cmd()
def duck():
    print("ты че дурак чтоле?")
def windows():
    print("А111121 0Ш1БКА СТ0П 00000000000000,0,0,0,0,0,0,ВЫ0,ВЫ0Авы,па0 ф,п0 ,е,0 ,0 фв0, 0п, фвап0 ва0000000")
    cmd()
def this():
    input("ты попал в корень системы")
    license()
def dota():
    print("#YOURECRAZYPEOPLE!")
def warface():
    print("Эта система не для таких петухов как ты")
def cs():
    print("Уважуха!")
    cmd()
def UC():
    print("Если витёк это смотрит, привет ютубу!")
def Vitec():
    print("Ну привет...")
def pi():
    pi=(math.pi)
    print(pi)
    cmd()
def memory():
    print("Скоро будет")
def memoryview():
    print("Скоро будет")
def cocaine():
    print("Отсыпь немного...")
def mayak():
    print("Не светит!")
def mybook():
    jojo=str(input(""))
    if jojo=="1":
        print("бел.лит")
        print("физ-ра")
        print("бел. мова")
        print("англ. яз")
        print("изобр. иск.")
    else:
        cmd()
def clear():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    
    cmd()
def pip_install_turtle():
    import turtle
def paint():
    print("Скоро будет")
def pip_install_system():
    import sys
def pip_install_random():
    import random
def pip_install_time():
    import time
def pip_install_all():
    import turtle
    import sys
    import random
    import time
def quit():
    sys.exit()
def random():
    a=int(input(""))
    b=int(input(""))
    c=random.randint(a,b)
    print(c)
def cmd():
    
    a=str(input(">>>"))
    if a=="calc":
        calc()
    if a=="this":
        this()
    if a=="duck":
        duck()
    if a=="meme":
        meme()
    if a=="windows":
        windows()
    if a=="dota":
        dota()
    if a=="warface":
        warface()
    if a=="cs":
        cs()
    if a=="Vitec":
        Vitec()
    if a=="UC":
        UC()
    if a=="calc1":
        calc1()
    if a=="calc2":
        calc2()
    if a=="calc3":
        calc3()
    if a=="calcinfo":
        calcinfo()
    if a=="cost":
        cost()
    if a=="pi":
        pi()
    if a=="memory":
        memory()
    if a=="memoryview":
        memoryview()
    if a=="cocaine":
        cocaine()
    if a=="mayak":
        mayak()
    if a=="clear":
        clear()
    else:
        cmd()
cmd()
          
