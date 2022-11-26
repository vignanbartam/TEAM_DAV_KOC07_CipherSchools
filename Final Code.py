
dict={                  #contact repository
    "ANKUSH":7282840789,
    "NAMAN": 7903078489,
    "RAMENDRA": 790307894,
    "SANSKAR": 7894561236,
    "DHYAN": 8081572449,
    "NARENDRA": 8281598116,
    "MONAL": 7634910177,
    "PIYUSH": 9570044770,
    "SIVAM": 9981840921,
    "MEHUL": 8004215422,
    "ANAMIKA": 8409590170,
    "RISHI": 8084269444,
    "MANAN": 9518186444,
    "VIGNAN": 7536044144,
    "DEV": 8403899648,
    "DAKSH": 7569841230,
    "BHARATH": 7458123690,
    "KUNAL": 6978452310,
    "KHUSHI": 754681230,
    "VANSHIKA": 8965471230
    
}
print('WELCOME TO OUR APP!!')
a=int(input('Enter1 to search a single contact👤\n Enter 2 Search Multiple Contacts👥  \n Enter 3 To List All Contacts 📜\n >>>Enter your choice: '))
#this set of code now requires the user to chose from 1,2,3 which further will make single search, multiple search from the dictionary or to list all contacts.
if a==3:
    print(dict)
    # to list all contacts
elif a==1:
    name=str(input('Enter the name whose contact info you want to search:  '))
    name=name.upper()
    if name in dict:
            print(name,dict[name]) #if the input name mathces with the repositary it shows their respective number.
    else:
        print('Contact not found')
        #asking user if he wants to add the person in the repository
        a=int(input('Do you want to add this person in the contact? \n Enter 1 for YES and 2 for NO \n  '))
        if a==1:
            b=int(input('Enter the phone number of this person:  '))
            name=name.upper()
            dict.update({name : b})
            print(dict)
        else:
            print('THANK YOU FOR USING OUR APP!')
#searching multiple contacts in the repository
elif a==2:
    result={}
    s1=[]
    s=0
    name1=input("Enter the names of the contacts seperated by commas: ").split(",") #split attribute splits the input string into list.
    for i in name1:
        i=i.upper()
        if i in dict:
            result[i]=dict[i]
            print(i,dict[i],end=' ')
        else:
            s1.append(i)
            s+=1
    if s>0:
        print('Contact not found')
else:
    print('Contact not found.')

print('-'*100)
print(' '*0, 'Thank you for using our app!!', ' '*0)
print('-'*100)
                
            