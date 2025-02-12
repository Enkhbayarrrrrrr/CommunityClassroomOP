def printSpring():
    print("Хавар болж цэцэгс цэцэглэлээ.")

def printSummer():
    print("Зун болж халуун боллоо.")

def printFall():
    print("Намар болж навчис уналаа.")

def printWinter():
    print("Өвөл болж цас орлоо.")

def main():
    season = int(input("Улиралаа оруулна уу (1=Хавар, 2=Зун, 3=Намар, 4=Өвөл): "))

    if season == 1:
        printSpring()
    elif season == 2:
        printSummer()
    elif season == 3:
        printFall()
    elif season == 4:
        printWinter()
    else:
        print("Буруу утга оруулсан байна!")

if __name__ == "__main__":
    main()
