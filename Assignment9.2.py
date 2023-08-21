def subtract_time(t1, t2):
    h1, m1, s1 = t1
    h2, m2, s2 = t2

    total_seconds1 = h1 * 3600 + m1 * 60 + s1
    total_seconds2 = h2 * 3600 + m2 * 60 + s2

    if total_seconds1 < total_seconds2:
        total_seconds1, total_seconds2 = total_seconds2, total_seconds1

    result_seconds = total_seconds1 - total_seconds2

    hours, remainder = divmod(result_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return hours, minutes, seconds

def add_time(t1, t2):
    h1, m1, s1 = t1
    h2, m2, s2 = t2

    total_seconds1 = h1 * 3600 + m1 * 60 + s1
    total_seconds2 = h2 * 3600 + m2 * 60 + s2

    result_seconds = total_seconds1 + total_seconds2

    hours, remainder = divmod(result_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return hours, minutes, seconds

def show(inp):
    h, m, s = inp
    print(f"The result is: {h}:{m}:{s}")

def menu():
    print("Enter your enter and exit time in a 24-hour format:")
    num1 = int(input("Hour of enter -> "))
    num2 = int(input("Minute of enter -> "))
    num3 = int(input("Second of enter -> "))
    num4 = int(input("Hour of exit -> "))
    num5 = int(input("Minute of exit -> "))
    num6 = int(input("Second of exit -> "))
    
    print(f"So your enter time was = {num1}:{num2}:{num3} and the exit time is = {num4}:{num5}:{num6}")
    
    tim1 = (num1, num2, num3)
    tim2 = (num4, num5, num6)
    
    print("Do you want to add or subtract time? 1 - Add 2 - Subtract")
    opt = int(input())
    
    if opt == 1:
        show(add_time(tim1, tim2))
    elif opt == 2:
        show(subtract_time(tim1, tim2))
    else:
        print("Wrong input")

menu()
