#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print ("welcome to bank kanjoos")
restart = 'Y'
chances = 3
balance=67.14
while chances>=0:
    pin=int(input("\n enter the pin of you kanjoos bank card"))
    if pin == (1234):
        print("\n you have entered the correct pin \n")
        while restart not in ('n','no','NO','N'):
            
            print("please press 1 to check your balance \n")
            print('please press 2 for withdrawl \n')
            print('please press 3 to deposit \n')
            print ('please press 4 to return card')
            option = int (input('enter the choice'))
            
            if option ==1:
                print ('balance of your kanjoos account is', balance)
                restart=input('would you like to start over')
                if restart ==('n','no','N','NO'):
                    print('thank you')
                    break
            
            if option ==2:
                option2='Y'
                withdrawl=float(input('enter the value to be withdrawn \n 10,20,40,60,80,100 \n'))
                if withdrawl in [10,20,40,60,80,100]:
                    balance = balance-withdrawl
                    print('\n your balance is :', balance)
                    if restart ==('n','no','N','NO'):
                        print('thank you')
                        break
                elif withdrawn not in [10,20,40,60,80,100]:
                    print ('invalid value entered \n please retry kanjoos')
                    restart =('Y')
                elif withdrawl ==1:
                    withdrawl =float (input('\n please enter the desired amount : '))
                    
                    
            elif option ==3:
                payin=float(input('\n how much would you like to pay in'))
                balance=balance+payin
                print('\n your balance is ', balance)
                restart = input ('would you like to go back')
                if restart ==('n','no','N','NO'):
                    print ('thank you')
                    break
                    
            elif option==4:
                print ('\n please wait your card is returned..........')
                restart='Y'
    elif pin!=(1234):
        print ('\n incorrect password \n')
        chances =chances-1
        if chances==0:
            print ('\n no more attempts!!!!!!')
            break


# In[ ]:





# In[ ]:




