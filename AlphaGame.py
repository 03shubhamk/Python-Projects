import random

i = 0
while i==0 :
    print()
    print("=========================================")
    tar = chr(random.randint(65,90))
    p1 = input("Player 1, Enter the Alphabate : ")
    p2 = input("Player 2, Enter the Alphabate : ")
    p3 = input("Player 3, Enter the Alphabate : ")
    print("Target is : ",tar)

    if tar==p1:
        print("Player 1 is winner")
    elif tar==p2 :
        print("Player 2 is winner")
    elif tar==p3 :
        print("Player 3 is winner")

    elif tar==chr(ord(p1)+1) :
        print("Player 1 is winner")
    elif tar==chr(ord(p2)+1) :
        print("Player 2 is winner")
    elif tar==chr(ord(p3)+1) :
        print("Player 3 is winner")

    elif tar==chr(ord(p1)-1) :
        print("Player 1 is winner")
    elif tar==chr(ord(p2)-1) :
        print("Player 2 is winner")
    elif tar==chr(ord(p3)-1) :
        print("Player 3 is winner")
    else:
        print("No match found...!")