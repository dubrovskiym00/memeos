
def calc():
    calc42=int(input(""))
    calc24=int(input(""))
    calc1375=calc42*calc24
    print(calc1375)
def calc1():
    calc42=int(input(""))
    calc24=int(input(""))
    calc1375=calc42+calc24
    print(calc1375)
def calc2():
    calc42=int(input(""))
    calc24=int(input(""))
    calc1375=calc42/calc24
    print(calc1375)
def calc3():
    calc42=int(input(""))
    calc24=int(input(""))
    calc1375=calc42-calc24
    print(calc1375)
def calcinfo():
    print("calc -> калькулятор(умножение)")
    print("calc1 -> калькулятор(плюс)")
    print("calc2 -> калькулятор(деление)")
    print("calc3 -> калькулятор(минус)")
def cost():
    costitem=int(input("Сколько стоит 1 вещь?"))
    cost1=int(input("Сколько хотите купить?"))
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
    else:
        cmd()
cmd()
          
