class multipleFunction():
    def triangle():
        H=int(input("Height:"))
        B=int(input("Breadth:"))
        Area = (H*B)/2
        print("Area of Triangle:",Area)
        H1=int(input("Height1:"))
        H2=int(input("Height2:"))
        B1=int(input("Breadth1:"))
        perimeter=H1+H2+B1
        print("Perimeter of Triangle:",perimeter)

    def percentage():
        sub1=int(input("Subject 1="))
        sub2=int(input("Subject 2="))
        sub3=int(input("Subject 3="))
        sub4=int(input("Subject 4="))
        sub5=int(input("Subject 5="))
        total=sub1+sub2+sub3+sub4+sub5
        print("Total:", total)
        percent=total/500 * 100
        percentage=percent
        print("Percentage:",percentage)

    def ElegibilityforMarriage_Elegible():
        Gender=input("Your Gender:")
        Age=int(input("Your Age:"))
        if Gender == "Female":
            if Age>=18:
                print("Elegible for Marriage")
            else:
                print("Not Elegible for Marriage")
    
        elif Gender == "Male":
            if Age>=21:
                print("Elegible for Marriage")
            else:
                print("Not elegible for Marriage")

    def OddEven_OddEven():
        Num=int(input("Enter a Number:"))
        if Num %2 ==0:
            print(Num,"is Even number")
        else:
            print(Num,"is Odd number")

    
    def SubfieldsInAI_Subfields():
        print("Sub-fields in AI are:")
        list=("Machine learning", "Neural Network", "Vision", "Robotics", "Speech Processing", "Natural Language Processing")
        for Name in list:
            print(Name)