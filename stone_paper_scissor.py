
import random
import time

while True:

    whilcount=int(input("enter how many round you want to play:"))
    count =1
    cscore = 0
    yscore =0
    dict = { "st" :1, "p":2,"sc":3}
    dict2 = { "st": "stone","p": "paper","sc": "scissor"}


    while(count<=whilcount):

        your_choice = input("enter your choice: st for STONE // p for PAPER //sc for SCISSOR:")
        dict = { "st" :1, "p":2,"sc":3}
        you = dict[your_choice]

        computer_choice = random.choice(list(dict.keys()))
        computer =dict[computer_choice]


        print("computer choice is ",  dict2[computer_choice])
        print("your choice is ", dict2[your_choice])


        if(computer==2 and you==2):
            print("draw")

        elif(computer==1 and you==1):
            print("draw")
        elif(computer==3 and you==3):
            print("draw")

        elif(computer==1 and you==2):
            print("you win ")
            yscore+=1
            print("your score =",yscore ,"computer score =",cscore)

        elif(computer==1 and you==3):
            print("you lose")
            cscore+=1
            print("your score =",yscore ,"computer score =",cscore)

        elif(computer==2 and you==1):
            print("you lose")
            cscore+=1
            print("your score =",yscore ,"computer score =",cscore)

        elif(computer==2 and you==3):
            print("you win")
            yscore+=1
            print("your score =",yscore ,"computer score =",cscore)

        elif(computer==3 and you==2):
            print("you lose")
            cscore+=1
            print("your score =",yscore ,"computer score =",cscore)

        elif(computer==3 and you==1):
            print("you win")
            yscore+=1
            print("your score =",yscore ,"computer score =",cscore)
        else:
            print("something went wrong")
        count +=1

    print()
    print("calculating score","."*whilcount)
    time.sleep(0.35)


    print("your score is ",yscore)
    print("computer score is ",cscore)

    if(yscore>cscore):
        print("you win")
    elif(yscore==cscore):
        print(" game is draw")

    else:
        print("you lose")

    print(" ")
    r =int(input("Do you want to play again? if yes enter '0',else enter '1' for exit:"))
    if(r==1):
        print("exiting game...")
        time.sleep(0.4)
        break
    else:
        print("starting the game again")
        time.sleep(0.4)
        print()
        print("/","*"*50,"/")
        print()