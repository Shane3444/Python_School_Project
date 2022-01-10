from datetime import date
import module_registration as mr
from tkinter import *
import matplotlib as plt
import project_mars
import project_alpha
import project_proxima
import project_kepler
import welcome_module as wm
import random as rd
import Project_side
import mysql.connector
def proceed(uwindow):
      uwindow.destroy()
conn = mysql.connector.connect(host='localhost',user='root',passwd='tiger',database='system28')
cur = conn.cursor()
tbam1 = 6350
tbam2 = 14990
tbam3 = 15250
tbam4 = 15600
wm.welcome()
print('''
+=============================================================================+
|                                                                             |
|   ==+== x   + ==+== +==== x===+ +===+ ==+== +==== +     +     +==== x===+   |
|     |   |\\  |   |   |     |   | |       |   |     |     |     |     |   |   |
|     |   | \\ |   |   +===  +===+ +===+   |   +===  |     |     +===  +===+   |
|     |   |  \\|   |   |     |  \\      |   |   |     |     |     |     |  \\    |
|   ==+== +   x   +   +==== +   \\ +===+   +   +==== +==== +==== +==== +   \\   |
|                                                                             |
+=============================================================================+''')
print('\t\t\t\t\t      To Infinity And Beyond...')

while True:
      print("_"*78)
      print('-'*78)
      print('\t\t        +----------------------------+')
      print('\t\t        |     S.NO.    |   OPTIONS   |')
      print('\t\t        +----------------------------+')
      print('\t\t        |       1      |   SIGN-UP   |')
      print('\t\t        |       2      |   LOGIN     |')
      print('\t\t        |       3      |   EXIT      |')
      print('\t\t        +----------------------------+')
      c = int(input('\n Enter Your Choice    : \t'))
      if c == 3:
            print("_"*78)
            print('-'*78)
            print('\t\t           THANK YOU FOR VISITING !!')
            print("_"*78)
            print('-'*78)
            break
      if c == 1:
            mr.tk_register()
            print(' You have been registered !\n\n')
      if c == 2:
            print('\n')
            print('-'*78)
            print('''
                  ██╗      ██████╗  ██████╗ ██╗███╗   ██╗
                  ██║     ██╔═══██╗██╔════╝ ██║████╗  ██║
                  ██║     ██║   ██║██║  ███╗██║██╔██╗ ██║
                  ██║     ██║   ██║██║   ██║██║██║╚██╗██║
                  ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║
                  ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝''')
            print('-'*78)
            name=input(' Enter Name           : \t')
            mail=input(' Enter E-Mail ID      : \t')
            PASS=input(' Enter Password       : \t')
            cur.execute('select * from intrstlr')
            recs = cur.fetchall()
            flag = 0
            for i in recs:
                  if i[-3] == PASS and i[-4] == mail and i[0]!='ADMIN':
                        flag = 1
                        break
                  elif i[0]=='ADMIN' and i[-3] == PASS and i[-4] == mail:
                        flag=2
                        Project_side.admin()
                        break
            else:
                  print()
                  print('-'*78)
                  print('\n You are not registered !')
                  print("_"*78)
                  print('-'*78)
                  continue
            if flag==2:
                  continue
            
            while True:
                  if flag == 1:                    
                        print("_"*78)
                        print('-'*78)
                        print('\t\t            Interstellar Space Travel ')
                        print("_"*78)
                        print('-'*78)
                        print('\t\t        +---------------------------------+')
                        print('\t\t        |    S.NO.     |   DESTINATION    |')
                        print('\t\t        +---------------------------------+')
                        print('\t\t        |      1       |       MARS       |')
                        print('\t\t        |      2       | PROXIMA CENTAURI |')
                        print('\t\t        |      3       |  ALPHA CENTAURI  |')
                        print('\t\t        |      4       |   KEPLER 452-B   |')
                        print('\t\t        |      5       |     LIFT OFF     |')
                        print('\t\t        |      6       |      BOOKING     |')
                        print('\t\t        |      7       |     USER PAGE    |')
                        print("\t\t        |      8       |       EXIT       |")
                        print('\t\t        +---------------------------------+')
                        c3 = int(input('\n Enter Your Choice    : \t'))
                        if c3==8:
                              print()
                              print('-'*78)
                              print(" Exiting to Main Menu...")
                              print("_"*78)
                              print('-'*78)
                              break
                        if c3 == 7:
                              q1='select email,tcode from spacebook'
                              cur.execute(q1)
                              recs = cur.fetchall()
                              for i in recs:
                                    if mail == i[0]:
                                          tcode=i[1]
                              uwindow = Tk()
                              uwindow.attributes('-fullscreen',True)
                              uwindow.configure(bg='black')
                              bimg=PhotoImage(file='\\\srlab\\tcdata\system28\Documents\Shourya_XII-A\Interstellar.png')
                              Label(uwindow,image=bimg).place(x=0,y=0)
                              Label(uwindow,text='USER-PAGE',font=('Copperplate Gothic Bold',24),bg='black',fg='white').place(x=550,y=5)
                              LabelFrame(uwindow, text='Your Bookings',font=('Copperplate Gothic Light',20),bg='black',fg='white',width=1350,height=450).place(x=5,y=70)
                              luck = rd.randint(0,10)
                              if tcode=='tc1':
                                    Label(uwindow,text='You have booked for a trip to Mars ! We give you our compliments \n Thank you for booking with us. A customer care executive will contact you shortly ',bg='black',fg='cyan',font=('Copperplate Gothic Light',20)).place(x=60,y=110)
                                    lf1=LabelFrame(uwindow,text='Mars',height=300,width=300,bg='black',fg='white',font=('Copperplate Gothic Light',16)).place(x=215,y=190)
                                    IMG1=PhotoImage(file="\\\srlab\\tcdata\system28\Documents\Shourya_XII-A\\mars - Copy.png")
                                    LF1=Label(lf1,image=IMG1).place(x=225,y=210)
                                    lf=LabelFrame(uwindow,text='Ticket',height=300,width=700,bg='black',fg='white',font=('Copperplate Gothic Light',16)).place(x=615,y=190)
                                    Name=  'Name \t\t: '+name
                                    Mail=  'Email \t\t: '+mail
                                    amount='Amount \t\t: $'+str(tbam1)
                                    ddate ='Departure Date \t: 14 January'
                                    line="~"*52
                                    info1='Report 3 days before departure date to prepare'
                                    info2='for your journey at ISSR, Houston,USA'
                                    Label(lf,text=Name,bg='black',fg='cyan',font=('Copperplate Gothic Bold',15)).place(x=625,y=210)
                                    Label(lf,text=Mail,bg='black',fg='cyan',font=('Copperplate Gothic Bold',15)).place(x=625,y=250)
                                    Label(lf,text=amount,bg='black',fg='cyan',font=('Copperplate Gothic Bold',15)).place(x=625,y=290)
                                    Label(lf,text=ddate,bg='black',fg='cyan',font=('Copperplate Gothic Bold',15)).place(x=625,y=330)
                                    Label(lf,text=line,bg='black',fg='cyan',font=('Copperplate Gothic Bold',15)).place(x=625,y=370)
                                    Label(lf,text=info1,bg='black',fg='cyan',font=('Copperplate Gothic Bold',18)).place(x=625,y=410)
                                    Label(lf,text=info2,bg='black',fg='cyan',font=('Copperplate Gothic Bold',18)).place(x=625,y=450)

                              elif tcode=='tc2':
                                    Label(uwindow,text='You have booked for a trip to Proxima Centauri ! We give you our compliments \n Thank you for booking with us. A customer care executive will contact you shortly ',bg='black',fg='cyan',font=('Copperplate Gothic Light',20)).place(x=60,y=110)
                                    IMG2=PhotoImage(file="\\\srlab\\tcdata\system28\Documents\Shourya_XII-A\\proxima - Copy.png")
                                    lf2=LabelFrame(uwindow,text='Proxima Centauri',height=300,width=300,bg='black',fg='white',font=('Copperplate Gothic Light',16)).place(x=215,y=190)
                                    LF2=Label(lf2,image=IMG2).place(x=225,y=210)
                                    lf=LabelFrame(uwindow,text='Ticket',height=300,width=700,bg='black',fg='white',font=('Copperplate Gothic Light',16)).place(x=615,y=190)
                                    Name=  'Name \t\t: '+name
                                    Mail=  'Email \t\t: '+mail
                                    amount='Amount \t\t: $'+str(tbam2)
                                    ddate ='Departure Date \t: 10 March'
                                    line="~"*52
                                    info1='Report 3 days before departure date to prepare'
                                    info2='for your journey at ISSR, Houston,USA'
                                    Label(lf,text=Name,bg='black',fg='cyan',font=('Copperplate Gothic Bold',15)).place(x=625,y=210)
                                    Label(lf,text=Mail,bg='black',fg='cyan',font=('Copperplate Gothic Bold',15)).place(x=625,y=250)
                                    Label(lf,text=amount,bg='black',fg='cyan',font=('Copperplate Gothic Bold',15)).place(x=625,y=290)
                                    Label(lf,text=ddate,bg='black',fg='cyan',font=('Copperplate Gothic Bold',15)).place(x=625,y=330)
                                    Label(lf,text=line,bg='black',fg='cyan',font=('Copperplate Gothic Bold',15)).place(x=625,y=370)
                                    Label(lf,text=info1,bg='black',fg='cyan',font=('Copperplate Gothic Bold',18)).place(x=625,y=410)
                                    Label(lf,text=info2,bg='black',fg='cyan',font=('Copperplate Gothic Bold',18)).place(x=625,y=450)
                              elif tcode=='tc3':
                                    Label(uwindow,text='You have booked for a trip to Alpha Centauri ! We give you our compliments \n Thank you for booking with us. A customer care executive will contact you shortly ',bg='black',fg='cyan',font=('Copperplate Gothic Light',20)).place(x=60,y=110)
                                    IMG3=PhotoImage(file="\\\srlab\\tcdata\system28\Documents\Shourya_XII-A\\alpha - Copy.png")
                                    lf3=LabelFrame(uwindow,text='Alpha Centauri',height=300,width=300,bg='black',fg='white',font=('Copperplate Gothic Light',16)).place(x=215,y=190)
                                    LF3=Label(lf3,image=IMG3).place(x=225,y=210)
                                    lf=LabelFrame(uwindow,text='Ticket',height=300,width=700,bg='black',fg='white',font=('Copperplate Gothic Light',16)).place(x=615,y=190)
                                    Name=  'Name \t\t: '+name
                                    Mail=  'Email \t\t: '+mail
                                    amount='Amount \t\t: $'+str(tbam3)
                                    ddate ='Departure Date \t: 20 June'
                                    line="~"*52
                                    info1='Report 3 days before departure date to prepare'
                                    info2='for your journey at ISSR, Houston,USA'
                                    Label(lf,text=Name,bg='black',fg='cyan',font=('Copperplate Gothic Bold',15)).place(x=625,y=210)
                                    Label(lf,text=Mail,bg='black',fg='cyan',font=('Copperplate Gothic Bold',15)).place(x=625,y=250)
                                    Label(lf,text=amount,bg='black',fg='cyan',font=('Copperplate Gothic Bold',15)).place(x=625,y=290)
                                    Label(lf,text=ddate,bg='black',fg='cyan',font=('Copperplate Gothic Bold',15)).place(x=625,y=330)
                                    Label(lf,text=line,bg='black',fg='cyan',font=('Copperplate Gothic Bold',15)).place(x=625,y=370)
                                    Label(lf,text=info1,bg='black',fg='cyan',font=('Copperplate Gothic Bold',18)).place(x=625,y=410)
                                    Label(lf,text=info2,bg='black',fg='cyan',font=('Copperplate Gothic Bold',18)).place(x=625,y=450)

                              elif tcode=='tc4':
                                    Label(uwindow,text='You have booked for a trip to Kepler 452-B ! We give you our compliments \n Thank you for booking with us. A customer care executive will contact you shortly ',bg='black',fg='cyan',font=('Copperplate Gothic Light',20)).place(x=60,y=110)
                                    IMG4=PhotoImage(file="\\\srlab\\tcdata\system28\Documents\Shourya_XII-A\\kepler - Copy.png")
                                    lf4=LabelFrame(uwindow,text='Kepler 452-B',height=300,width=300,bg='black',fg='white',font=('Copperplate Gothic Light',16)).place(x=215,y=190)
                                    LF4=Label(lf4,image=IMG4).place(x=225,y=210)
                                    lf=LabelFrame(uwindow,text='Ticket',height=300,width=700,bg='black',fg='white',font=('Copperplate Gothic Light',16)).place(x=615,y=190)
                                    Name=  'Name \t\t: '+name
                                    Mail=  'Email \t\t: '+mail
                                    amount='Amount \t\t: $'+str(tbam4)
                                    ddate ='Departure Date \t: 9 September'
                                    line="~"*52
                                    info1='Report 3 days before departure date to prepare'
                                    info2='for your journey at ISSR, Houston,USA'
                                    Label(lf,text=Name,bg='black',fg='cyan',font=('Copperplate Gothic Bold',15)).place(x=625,y=210)
                                    Label(lf,text=Mail,bg='black',fg='cyan',font=('Copperplate Gothic Bold',15)).place(x=625,y=250)
                                    Label(lf,text=amount,bg='black',fg='cyan',font=('Copperplate Gothic Bold',15)).place(x=625,y=290)
                                    Label(lf,text=ddate,bg='black',fg='cyan',font=('Copperplate Gothic Bold',15)).place(x=625,y=330)
                                    Label(lf,text=line,bg='black',fg='cyan',font=('Copperplate Gothic Bold',15)).place(x=625,y=370)
                                    Label(lf,text=info1,bg='black',fg='cyan',font=('Copperplate Gothic Bold',18)).place(x=625,y=410)
                                    Label(lf,text=info2,bg='black',fg='cyan',font=('Copperplate Gothic Bold',18)).place(x=625,y=450)

                              else:
                                    Label(uwindow,text='You have not booked for any of the adventures. We hope to be at your services soon !',bg='black',fg='cyan',font=('Copperplate Gothic Light',20)).place(x=60,y=110)
                                    IMG1=PhotoImage(file="\\\srlab\\tcdata\system28\Documents\Shourya_XII-A\\mars - Copy.png")
                                    IMG2=PhotoImage(file="\\\srlab\\tcdata\system28\Documents\Shourya_XII-A\\proxima - Copy.png")
                                    IMG3=PhotoImage(file="\\\srlab\\tcdata\system28\Documents\Shourya_XII-A\\alpha - Copy.png")
                                    IMG4=PhotoImage(file="\\\srlab\\tcdata\system28\Documents\Shourya_XII-A\\kepler - Copy.png")
                                    lf1=LabelFrame(uwindow,text='Mars',height=300,width=300,bg='black',fg='cyan',font=('Copperplate Gothic Light',16)).place(x=70,y=150)
                                    lf2=LabelFrame(uwindow,text='Proxima Centauri',height=300,width=300,bg='black',fg='cyan',font=('Copperplate Gothic Light',16)).place(x=380,y=150)
                                    lf3=LabelFrame(uwindow,text='Alpha Centauri',height=300,width=300,bg='black',fg='cyan',font=('Copperplate Gothic Light',16)).place(x=690,y=150)
                                    lf4=LabelFrame(uwindow,text='Kepler 452-B',height=300,width=300,bg='black',fg='cyan',font=('Copperplate Gothic Light',16)).place(x=1000,y=150)
                                    LF1=Label(lf1,image=IMG1).place(x=80,y=170)
                                    LF2=Label(lf2,image=IMG2).place(x=390,y=170)
                                    LF3=Label(lf3,image=IMG3).place(x=700,y=170)
                                    LF4=Label(lf4,image=IMG4).place(x=1010,y=170)
                              LabelFrame(uwindow, text='Your Coupons',font=('Copperplate Gothic Light',20),bg='black',fg='white',width=1350,height=100).place(x=5,y=550)
                              if luck not in [1,2,3,4]:
                                    Label(uwindow,text='You have no coupons active right now ! Better Luck Next Time !',bg='black',fg='cyan',font=('Copperplate Gothic Light',20)).place(x=60,y=580)
                              if luck == 1 and tcode!='tc1':
                                    Label(uwindow,text='Congratulations ! You have won a free trip to Mars !',bg='black',fg='cyan',font=('Copperplate Gothic Light',20)).place(x=60,y=580)

                              if luck == 2 and tcode!='tc2':
                                    Label(uwindow,text='Congratulations ! You have won a free trip to Proxima Centauri !',bg='black',fg='cyan',font=('Copperplate Gothic Light',20)).place(x=60,y=580)

                              if luck == 3 and tcode!='tc3':
                                    Label(uwindow,text='Congratulations ! You have won a free trip to Alpha Centauri !',bg='black',fg='cyan',font=('Copperplate Gothic Light',20)).place(x=60,y=580)

                              if luck == 4 and tcode!='tc4':
                                    Label(uwindow,text='Congratulations ! You have won a free trip to Kepler 452-B !',bg='black',fg='cyan',font=('Copperplate Gothic Light',20)).place(x=60,y=580)

                              Button(uwindow,text='CONTINUE',font=('Copperplate Gothic Bold',20),command=lambda:proceed(uwindow)).place(x=550,y=710)
                              uwindow.mainloop()      

                        if c3 == 6:
                              query = 'select * from intrstlr where mail = "{}"'.format(mail)
                              cur.execute(query)
                              recs = cur.fetchone()
                              
                              if recs[-1]=='0' :
                                    print("="*78+"\n")
                                    print(' You are not eligible. Try Again Later ...')
                              elif recs[-1]==None:
                                    print("="*78+"\n")
                                    print(' You are not eligible right now. You have to give the test to qualify.')
                              elif recs[-1]=='1':
                                    print('''
            ██████╗  ██████╗  ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗ 
            ██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝██║████╗  ██║██╔════╝ 
            ██████╔╝██║   ██║██║   ██║█████╔╝ ██║██╔██╗ ██║██║  ███╗
            ██╔══██╗██║   ██║██║   ██║██╔═██╗ ██║██║╚██╗██║██║   ██║
            ██████╔╝╚██████╔╝╚██████╔╝██║  ██╗██║██║ ╚████║╚██████╔╝
            ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝''')
                                    print("="*78+"\n")            
                                    print('\t\t        +---------------------------------+')
                                    print('\t\t        |    T.CODE    |   DESTINATION    |')
                                    print('\t\t        +---------------------------------+')
                                    print('\t\t        |      1       |       MARS       |')
                                    print('\t\t        |      2       | PROXIMA CENTAURI |')
                                    print('\t\t        |      3       |  ALPHA CENTAURI  |')
                                    print('\t\t        |      4       |   KEPLER 452-B   |')
                                    print('\t\t        +---------------------------------+\n')
                                    tc = int(input(' Enter ticket code of desired destination \t: '))
                                    print('.'*71)
                                    x1="select phno from intrstlr where mail='{}'".format(mail)
                                    cur.execute(x1)
                                    arec=cur.fetchone()
                                    if tc == 1:
                                          print('\t        +-----------------------------------------------+')
                                          print('\t        |                     TICKET                    |')
                                          print('\t        +-----------------------------------------------+')
                                          print('\t        |    T.CODE      : 1                            |')
                                          print('\t        |    Email       : {} |'.format(mail.ljust(28)))
                                          print("\t        |   Phone No.    : {} |".format(arec[0].ljust(28)))
                                          print('\t        | Destination    : Mars                         |')
                                          print('\t        |...............................................| ')
                                          print('\t        |    Amount      : ${} |'.format(str(tbam1).ljust(27)))
                                          print('\t        | Departure Date : 14 January                   |')
                                          print('\t        |...............................................|')
                                          print('\t        | Report 3 days before departure date to prepare|')
                                          print('\t        | for your journey at ISSR,Houston,USA          |')
                                          print('\t        +-----------------------------------------------+')
                                          print('\t        | Pay the required amount at the departure point|')
                                          print('\t        | 1 week before the departure date to prevent   |')
                                          print('\t        | any inconvinience.                            |')
                                          print('\t        +-----------------------------------------------+')
                                          print('\t        | Keep a screenshot of this ticket safe with    |')
                                          print('\t        | yourself throughout the trip. Thank You!      |')
                                          print('\t        +-----------------------------------------------+')
                                          today=date.today()
                                          x="insert into spacebook values('{}','{}','{}',{})".format(mail,"tc1",today.strftime("%y-%m-%d"),arec[0])
                                          x1='update saletable set tbooked = tbooked + 1 where tcode = "tc1" '
                                          x2='update monthsale set tbooked = tbooked + 1 where month = "{}" '.format(today.strftime("%B"))
                                          cur.execute(x)
                                          cur.execute(x1)
                                          cur.execute(x2)
                                          cur.execute("commit")
                                          flg=1
                                    if tc == 2:
                                          print('\t        +-----------------------------------------------+')
                                          print('\t        |                     TICKET                    |')
                                          print('\t        +-----------------------------------------------+')
                                          print('\t        |    T.CODE      : 2                            |')
                                          print('\t        |    Email       : {} |'.format(mail.ljust(28)))
                                          print("\t        |   Phone No.    : {} |".format(arec[0].ljust(28)))
                                          print('\t        | Destination    : Proxima Centauri             |')
                                          print('\t        |...............................................| ')
                                          print('\t        |    Amount      : ${} |'.format(str(tbam2).ljust(27)))
                                          print('\t        | Departure Date : 10 March                     |')
                                          print('\t        |...............................................|')
                                          print('\t        | Report 3 days before departure date to prepare|')
                                          print('\t        | for your journey at ISSR,Houston,USA          |')
                                          print('\t        +-----------------------------------------------+')
                                          print('\t        | Pay the required amount at the departure point|')
                                          print('\t        | 1 week before the departure date to prevent   |')
                                          print('\t        | any inconvinience.                            |')
                                          print('\t        +-----------------------------------------------+')
                                          print('\t        | Keep a screenshot of this ticket safe with    |')
                                          print('\t        | yourself throughout the trip. Thank You!      |')
                                          print('\t        +-----------------------------------------------+')

                                          today=date.today()
                                          x="insert into spacebook values('{}','{}','{}',{})".format(mail,"tc2",today.strftime("%y-%m-%d"),arec[0])
                                          x1='update saletable set tbooked = tbooked + 1 where tcode = "tc2" '
                                          x2='update monthsale set tbooked = tbooked + 1 where month = "{}" '.format(today.strftime("%B"))
                                          cur.execute(x)
                                          cur.execute(x1)
                                          cur.execute(x2)
                                          cur.execute("commit")
                                          flg=2
                                    if tc == 3:
                                          print('\t        +-----------------------------------------------+')
                                          print('\t        |                     TICKET                    |')
                                          print('\t        +-----------------------------------------------+')
                                          print('\t        |    T.CODE      : 3                            |')
                                          print('\t        |    Email       : {} |'.format(mail.ljust(28)))
                                          print("\t        |   Phone No.    : {} |".format(arec[0].ljust(28)))
                                          print('\t        | Destination    : Alpha Centauri               |')
                                          print('\t        |...............................................| ')
                                          print('\t        |    Amount      : ${} |'.format(str(tbam3).ljust(27)))
                                          print('\t        | Departure Date : 20 June                      |')
                                          print('\t        |...............................................|')
                                          print('\t        | Report 3 days before departure date to prepare|')
                                          print('\t        | for your journey at ISSR,Houston,USA          |')
                                          print('\t        +-----------------------------------------------+')
                                          print('\t        | Pay the required amount at the departure point|')
                                          print('\t        | 1 week before the departure date to prevent   |')
                                          print('\t        | any inconvinience.                            |')
                                          print('\t        +-----------------------------------------------+')
                                          print('\t        | Keep a screenshot of this ticket safe with    |')
                                          print('\t        | yourself throughout the trip. Thank You!      |')
                                          print('\t        +-----------------------------------------------+')

                                          today=date.today()
                                          x="insert into spacebook values('{}','{}','{}',{})".format(mail,"tc3",today.strftime("%y-%m-%d"),arec[0])
                                          x1='update saletable set tbooked = tbooked + 1 where tcode = "tc3" '
                                          x2='update monthsale set tbooked = tbooked + 1 where month = "{}" '.format(today.strftime("%B"))
                                          cur.execute(x)
                                          cur.execute(x1)
                                          cur.execute(x2)
                                          cur.execute("commit")
                                          flg=3
                                    if tc == 4:
                                          print('\t        +-----------------------------------------------+')
                                          print('\t        |                     TICKET                    |')
                                          print('\t        +-----------------------------------------------+')
                                          print('\t        |    T.CODE      : 4                            |')
                                          print('\t        |    Email       : {} |'.format(mail.ljust(28)))
                                          print("\t        |   Phone No.    : {} |".format(arec[0].ljust(28)))
                                          print('\t        | Destination    : Kepler 452-B                 |')
                                          print('\t        |...............................................| ')
                                          print('\t        |    Amount      : ${} |'.format(str(tbam4).ljust(27)))
                                          print('\t        | Departure Date : 9 September                  |')
                                          print('\t        |...............................................|')
                                          print('\t        | Report 3 days before departure date to prepare|')
                                          print('\t        | for your journey at ISSR,Houston,USA          |')
                                          print('\t        +-----------------------------------------------+')
                                          print('\t        | Pay the required amount at the departure point|')
                                          print('\t        | 1 week before the departure date to prevent   |')
                                          print('\t        | any inconvinience.                            |')
                                          print('\t        +-----------------------------------------------+')
                                          print('\t        | Keep a screenshot of this ticket safe with    |')
                                          print('\t        | yourself throughout the trip. Thank You!      |')
                                          print('\t        +-----------------------------------------------+')

                                          today=date.today()
                                          x="insert into spacebook values('{}','{}','{}',{})".format(mail,"tc4",today.strftime("%y-%m-%d"),arec[0])
                                          x1='update saletable set tbooked = tbooked + 1 where tcode = "tc4" '
                                          x2='update monthsale set tbooked = tbooked + 1 where month = "{}" '.format(today.strftime("%B"))
                                          cur.execute(x)
                                          cur.execute(x1)
                                          cur.execute(x2)
                                          cur.execute("commit")
                                          flg=4
                        if c3 == 1:
                              project_mars.mars()
                              print('-'*78)
                              print('''
                  ███╗   ███╗ █████╗ ██████╗ ███████╗
                  ████╗ ████║██╔══██╗██╔══██╗██╔════╝
                  ██╔████╔██║███████║██████╔╝███████╗
                  ██║╚██╔╝██║██╔══██║██╔══██╗╚════██║
                  ██║ ╚═╝ ██║██║  ██║██║  ██║███████║
                  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝''')
                              print('-'*78)
                              print(' Space Vehicle  \t  : SP-67-4-A')
                              print(' Resort/Hotel   \t  : Mars Resort')
                              print(' Departure Date \t  : 14 January')
                              print(' Arrival Date   \t  : 20 February\n')
                              print('                        Day 1                           ')
                              print(' Arrival at Landing Station         ... 0128 hrs : $ 2050')
                              print(' Hyper Loop Ride to Mars Resort     ... 0148 hrs : $ 200 ')
                              print('.'*71)
                              print('                        Day 2                           ')
                              print(' Visit To Phoebos Moon              ... 0830 hrs : $ 400')
                              print(' Visit To Space Travel Museum       ... 1430 hrs : $ 150')
                              print('.'*71)
                              print('                        Day 3                           ')
                              print(' Visit To Deimos Moon               ... 0830 hrs : $ 550')
                              print(' Visit To North Pole                ... 1600 hrs : $ 600')
                              print('.'*71)
                              print('                        Day 4                           ')
                              print(' Visit To Alien Zoo(Optional)       ... 0830 hrs : $ 300')
                              print(' Day At Leisure                                     ')
                              print('.'*71)
                              print('                        Day 5                           ')
                              print(' Arrival at Launching Station       ... 0120 hrs : $ 100')
                              print(' Departure                          ... 0130 hrs : $ 2000   ')
                              print('.'*71)
                              print('                           Total                 : $',tbam1)
                        if c3 == 2:
                              project_proxima.proxima()
                              print('-'*78)
                              print('''
      ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗███╗   ███╗ █████╗         
      ██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝██║████╗ ████║██╔══██╗        
      ██████╔╝██████╔╝██║   ██║ ╚███╔╝ ██║██╔████╔██║███████║        
      ██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗ ██║██║╚██╔╝██║██╔══██║        
      ██║     ██║  ██║╚██████╔╝██╔╝ ██╗██║██║ ╚═╝ ██║██║  ██║        
      ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝        
       ██████╗███████╗███╗   ██╗████████╗ █████╗ ██╗   ██╗██████╗ ██╗
      ██╔════╝██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██║   ██║██╔══██╗██║
      ██║     █████╗  ██╔██╗ ██║   ██║   ███████║██║   ██║██████╔╝██║
      ██║     ██╔══╝  ██║╚██╗██║   ██║   ██╔══██║██║   ██║██╔══██╗██║
      ╚██████╗███████╗██║ ╚████║   ██║   ██║  ██║╚██████╔╝██║  ██║██║
       ╚═════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝
                                                                     ''')
                              print('-'*78)
                              print(' Space Vehicle  \t  : ALPHA-450-Z')
                              print(' Resort/Hotel   \t  : Proxima Resort Grand')
                              print(' Departure Date \t  : 10 March')
                              print(' Arrival Date   \t  : 14 April')
                              print('\n Warning : People Sensitive to High Radiation Protect\n ion Suits are not permitted for this trip\n')
                              print('                        Day 1                           ')
                              print(' Arrival at Proxima Centauri b      ... 0128 hrs : $ 6700')
                              print(' Hyper Loop Ride to Resort          ... 0148 hrs : $ 550')
                              print('.'*71)
                              print('                        Day 2                              ')
                              print(' Visit To Proxima Centauri Star     ... 0830 hrs : $ 550')
                              print(' Visit To Space Travel Museum       ... 1430 hrs : $ 50 ')
                              print('.'*71)
                              print('                        Day 3                              ')
                              print(' Visit To North Pole                ... 0830 hrs : $ 300')
                              print(' Star Gazing                        ... 1600 hrs       ')
                              print('.'*71)
                              print('                        Day 4                           ')
                              print(' Visit To Alien Zoo(Optional)       ... 0830 hrs : $ 240')
                              print(' Day At Leisure                                     ')
                              print('.'*71)
                              print('                        Day 5                           ')
                              print(' Arrival at Launching Station       ... 0120 hrs : $ 100')
                              print(' Departure                          ... 0130 hrs : $ 6500   ')
                              print('.'*71)
                              print('                           Total                 : $',tbam2)
                              print('.'*71)
                        if c3 == 3:
                              project_alpha.alpha()
                              print('-'*78)
                              print('''
       █████╗ ██╗     ██████╗ ██╗  ██╗ █████╗                        
      ██╔══██╗██║     ██╔══██╗██║  ██║██╔══██╗                       
      ███████║██║     ██████╔╝███████║███████║                       
      ██╔══██║██║     ██╔═══╝ ██╔══██║██╔══██║                       
      ██║  ██║███████╗██║     ██║  ██║██║  ██║                       
      ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝                       
       ██████╗███████╗███╗   ██╗████████╗ █████╗ ██╗   ██╗██████╗ ██╗
      ██╔════╝██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██║   ██║██╔══██╗██║
      ██║     █████╗  ██╔██╗ ██║   ██║   ███████║██║   ██║██████╔╝██║
      ██║     ██╔══╝  ██║╚██╗██║   ██║   ██╔══██║██║   ██║██╔══██╗██║
      ╚██████╗███████╗██║ ╚████║   ██║   ██║  ██║╚██████╔╝██║  ██║██║
       ╚═════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝''')
                              print('-'*78)
                              print(' Space Vehicle  \t  : ALPHA-450-Z')
                              print(' Resort/Hotel   \t  : Resort Alpha Grand')
                              print(' Departure Date \t  : 20 June')
                              print(' Arrival Date   \t  : 17 July')
                              print('\n Warning : People Sensitive to High Radiation Protect\n ion Suits are not permitted for this trip\n')
                              print('                        Day 1                           ')
                              print(' Arrival at Alpha Centauri Bb       ... 0128 hrs : $ 6700')
                              print(' Hyper Loop Ride to Resort          ... 0148 hrs : $ 550')
                              print('.'*71)
                              print('                        Day 2                           ')
                              print(' Visit To Alpha Centauri A          ... 0830 hrs : $ 400')
                              print(' Visit To Space Travel Museum       ... 1430 hrs : $ 50')
                              print('.'*71)
                              print('                        Day 3                           ')
                              print(' Visit To Alpha Centauri B          ... 0830 hrs : $ 400')
                              print(' Visit To Columbus Space Colony     ... 1600 hrs : $ 50')
                              print('.'*71)
                              print('                        Day 4                           ')
                              print(' Visit To Alpha Centauri C(Optional)... 0830 hrs : $ 400')
                              print(' Day At Leisure                                     ')
                              print('.'*71)
                              print('                        Day 5                           ')
                              print(' Arrival at Launching Station       ... 0120 hrs : $ 200')
                              print(' Departure                          ... 0130 hrs : $ 6500')
                              print('.'*71)
                              print('                        Total                    : $',tbam3)
                              print('.'*71)
                        if c3 == 4:
                              project_kepler.kepler()
                              print('-'*78)
                              print('''
            ██╗  ██╗███████╗██████╗ ██╗     ███████╗██████╗ 
            ██║ ██╔╝██╔════╝██╔══██╗██║     ██╔════╝██╔══██╗
            █████╔╝ █████╗  ██████╔╝██║     █████╗  ██████╔╝
            ██╔═██╗ ██╔══╝  ██╔═══╝ ██║     ██╔══╝  ██╔══██╗
            ██║  ██╗███████╗██║     ███████╗███████╗██║  ██║
            ╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝                                                
            ██╗  ██╗███████╗██████╗               ██████╗   
            ██║  ██║██╔════╝╚════██╗              ██╔══██╗  
            ███████║███████╗ █████╔╝    █████╗    ██████╔╝  
            ╚════██║╚════██║██╔═══╝     ╚════╝    ██╔══██╗  
                 ██║███████║███████╗              ██████╔╝  
                 ╚═╝╚══════╝╚══════╝              ╚═════╝   
                                                            ''')
                              print('-'*78)
                              print(' Space Vehicle  \t  : PSLV-VOL-2')
                              print(' Resort/Hotel   \t  : Resort Keploxia')
                              print(' Departure Date \t  : 9 September')
                              print(' Arrival Date   \t  : 1 November')
                              print('                        Day 1                           ')
                              print(' Arrival at Proxima Centauri b      ... 0128 hrs : $ 6700')
                              print(' Hyper Loop Ride to Resort          ... 0148 hrs : $ 550')
                              print('.'*71)
                              print('                        Day 2                           ')
                              print(' Visit To Host Star                 ... 0830 hrs : $ 600')
                              print(' Visit To Star Wars Amusement Park  ... 1430 hrs : $ 200')
                              print('.'*71)
                              print('                        Day 3                           ')
                              print(' Water Sports At Panagea Ocean      ... 0830 hrs : $ 700')
                              print(' Star Gazing                        ... 1600 hrs  ')
                              print('.'*71)
                              print('                        Day 4                           ')
                              print(' Visit To Alien Zoo                 ... 0830 hrs : $ 150')
                              print(' Remaining Day At Leisure                           ')
                              print('.'*71)
                              print('                        Day 5                           ')
                              print(' Arrival at Launching Station       ... 0120 hrs : $ 200')
                              print(' Departure                          ... 0130 hrs : $ 6500')
                              print('.'*71)
                              print('                           Total                 : $',tbam4)
                              print('.'*71)
                        if c3 == 5:
                              query = 'select * from intrstlr where mail = "{}"'.format(mail)
                              cur.execute(query)
                              rec = cur.fetchone()
                              if rec[-1]=='0' :
                                    print(' You are not eligible. Try Again Later ...')
                              elif rec[-1]=='1' :
                                    print("_"*78)
                                    print('-'*78)
                                    print('\n\tYOU HAVE ALREADY QUALIFIED FOR SPACE TRAVEL.\n YOU CAN BOOK FOR ANY DESTINATION USING OPTION 6')
                              elif rec[-1]==None:
                                    print('\n WARNING : IF YOU FAIL TO ANSWER MORE THAN 6 ANSWERS CORRECTLY, YOU WILL NOT \n BE ABLE TO APPLY FOR BOOKING.')
                                    choice = input('\n DO YOU WANT TO CONTINUE(Y/N): ')
                                    if choice == 'Y':
                                          for i in recs:    
                                                if i[-1]!='0':
                                                      window = Tk()
                                                      window.attributes('-fullscreen',True)
                                                      window.title("Beginners' Test")
                                                      val1 = StringVar()
                                                      val2 = StringVar()
                                                      val3 = StringVar()
                                                      val4 = StringVar()
                                                      val5 = StringVar()
                                                      val6 = StringVar()
                                                      val7 = StringVar()
                                                      val8 = StringVar()
                                                      COUNT = IntVar()
                                                      Img = PhotoImage(file='\\\srlab\\tcdata\system28\Documents\Shourya_XII-A\Interstellar.png')
                                                      l1=Label(window,image=Img)
                                                      l1.place(x=0,y=0)
                                                      l1.image= Img
                                                      val1.set(' ')
                                                      val2.set(' ')
                                                      val3.set(' ')
                                                      val4.set(' ')
                                                      val5.set(' ')
                                                      val6.set(' ')
                                                      val7.set(' ')
                                                      val8.set(' ')
                                                      value1,value2,value3=0,0,0
                                                      L=Label(relief="groove",text='Beginners Test for Space Travel',font=('Copperplate Gothic Bold',22),
                                                            bg='black',fg='cyan').grid(row=0,column=3,padx=400,pady=10,columnspan=10)
                                                      Label(font=('Terminal',16),bg='black',fg='white',
                                                            text='Before proceding any further, prepare for a beginners test to know if you are eligible for this adventure. Answer 6 out of these 8 \nquestions correctly to proceed ! :'
                                                            ,justify="left").grid(row=1,column=0,columnspan=20,pady=10,padx=5)

                                                      Label(relief="sunken",highlightcolor="white",borderwidth=2,text='Question No.1 : A Person not wearing a Space Suit explodes in Space ',font=('Copperplate Gothic Light',15),
                                                            bg='black',fg='cyan',justify="left").grid(row=2,column=3,padx=100,columnspan=10)
                                                      Radiobutton(text='True',variable=val1,value=0,font=('Copperplate Gothic Light',15),
                                                                  bg='black',fg='cyan').grid(row=3,column=5,pady=10)
                                                      Radiobutton(text='False',variable=val1,value=1,font=('Copperplate Gothic Light',15),
                                                                  bg='black',fg='cyan').grid(row=3,column=9,pady=10)

                                                      Label(relief="sunken",highlightcolor="white",borderwidth=2,text='Question No.2 : A fire in a space can only be put out using water ',font=('Copperplate Gothic Light',15),
                                                            bg='black',fg='cyan',justify="left").grid(row=4,column=3,padx=100,columnspan=10)
                                                      Radiobutton(text='True',variable=val2,value=0,font=('Copperplate Gothic Light',15),
                                                                  bg='black',fg='cyan').grid(row=5,column=5,pady=10)
                                                      Radiobutton(text='False',variable=val2,value=1,font=('Copperplate Gothic Light',15),
                                                                  bg='black',fg='cyan').grid(row=5,column=9,pady=10)

                                                      Label(relief="sunken",highlightcolor="white",borderwidth=2,text='Question No.3 : A special bag is used if a person feels like vomiting in space ',font=('Copperplate Gothic Light',15),
                                                            bg='black',fg='cyan',justify="left").grid(row=6,column=3,padx=100,columnspan=10)
                                                      Radiobutton(text='True',variable=val3,value=1,font=('Copperplate Gothic Light',15),
                                                                  bg='black',fg='cyan').grid(row=7,column=5,pady=10)
                                                      Radiobutton(text='False',variable=val3,value=0,font=('Copperplate Gothic Light',15),
                                                                  bg='black',fg='cyan').grid(row=7,column=9,pady=10)

                                                      Label(relief="sunken",highlightcolor="white",borderwidth=2,text='Question No.4 : You can hear sound in Space',font=('Copperplate Gothic Light',15),
                                                            bg='black',fg='cyan',justify="left").grid(row=8,column=3,padx=100,columnspan=10)
                                                      Radiobutton(text='True',variable=val4,value=0,font=('Copperplate Gothic Light',15),
                                                                  bg='black',fg='cyan').grid(row=9,column=5,pady=10)
                                                      Radiobutton(text='False',variable=val4,value=1,font=('Copperplate Gothic Light',15),
                                                                  bg='black',fg='cyan').grid(row=9,column=9,pady=10)

                                                      Label(relief="sunken",highlightcolor="white",borderwidth=2,text='Question No.5 : Black Holes suck everything that comes anywhere around them ',font=('Copperplate Gothic Light',15),
                                                            bg='black',fg='cyan',justify="left").grid(row=10,column=3,padx=100,columnspan=10)
                                                      Radiobutton(text='True',variable=val5,value=0,font=('Copperplate Gothic Light',15),
                                                                  bg='black',fg='cyan').grid(row=11,column=5,pady=10)
                                                      Radiobutton(text='False',variable=val5,value=1,font=('Copperplate Gothic Light',15),
                                                                  bg='black',fg='cyan').grid(row=11,column=9,pady=10)

                                                      Label(relief="sunken",highlightcolor="white",borderwidth=2,text='Question No.6 : It would be hard to fly through the asteroid belt ',font=('Copperplate Gothic Light',15),
                                                            bg='black',fg='cyan',justify="left").grid(row=12,column=3,padx=100,columnspan=10)
                                                      Radiobutton(text='True',variable=val6,value=0,font=('Copperplate Gothic Light',15),
                                                                  bg='black',fg='cyan').grid(row=13,column=5,pady=10)
                                                      Radiobutton(text='False',variable=val6,value=1,font=('Copperplate Gothic Light',15),
                                                                  bg='black',fg='cyan').grid(row=13,column=9,pady=10)

                                                      Label(relief="sunken",highlightcolor="white",borderwidth=2,text='Question No.7 : Speed Of Light in vacuum is ?',font=('Copperplate Gothic Light',15),
                                                            bg='black',fg='cyan',justify="left").grid(row=14,column=3,padx=100,columnspan=10)
                                                      Radiobutton(text='3*10^8',variable=val7,value=1,font=('Copperplate Gothic Light',15),
                                                                  bg='black',fg='cyan').grid(row=15,column=5,pady=10)
                                                      Radiobutton(text='9*10^12',variable=val7,value=0,font=('Copperplate Gothic Light',15),
                                                                  bg='black',fg='cyan').grid(row=15,column=9,pady=10)

                                                      Label(relief="sunken",highlightcolor="white",borderwidth=2,text='Question No.8 : The natural sattelite of Saturn with Liquid Water on it is ?',font=('Copperplate Gothic Light',15),
                                                            bg='black',fg='cyan',justify="left").grid(row=16,column=3,padx=100,columnspan=10)
                                                      Radiobutton(text='Enceladus',variable=val8,value=1,font=('Copperplate Gothic Light',15),
                                                                  bg='black',fg='cyan').grid(row=17,column=5,pady=10)
                                                      Radiobutton(text='Titan',variable=val8,value=0,font=('Copperplate Gothic Light',15),
                                                                  bg='black',fg='cyan').grid(row=17,column=9,pady=10)
                                                      def perf():
                                                            count=0
                                                            value1 = val1.get()
                                                            value2 = val2.get()
                                                            value3 = val3.get()
                                                            value4 = val4.get()
                                                            value5 = val5.get()
                                                            value6 = val6.get()
                                                            value7 = val7.get()
                                                            value8 = val8.get()
                                                            if int(value1) == 1:
                                                                  count+=1
                                                            if int(value2) == 1:
                                                                  count+=1
                                                            if int(value3) == 1:
                                                                  count+=1
                                                            if int(value4) == 1:
                                                                  count+=1
                                                            if int(value5) == 1:
                                                                  count+=1
                                                            if int(value6) == 1:
                                                                  count+=1
                                                            if int(value7) == 1:
                                                                  count+=1
                                                            if int(value8) == 1:
                                                                  count+=1
                                                                                    
                                                            COUNT.set(count)
                                                            window.destroy()
                                                      Button(window,command=perf,text='Submit',font=('Copperplate Gothic Light',20),bg='black',fg='white',borderwidth=5).place(x=1100,y=6)
                                                      window.mainloop()
                                                      if COUNT.get() <= 5:
                                                            print("\n"+"_"*78+"\n")
                                                            print(' Your score is        : \t'+str(COUNT.get()))
                                                            print(' You are not eligible. Try Again Later ...')
                                                            query = 'update intrstlr set qualify = "0" where mail = "{}"'.format(mail)
                                                            cur.execute(query)
                                                            cur.execute('commit')
                                                            break
                                                            
                                                      else:
                                                            flagt=0
                                                            print(' Your score is        : \t'+str(COUNT.get()))
                                                            print(' Congratulations !!!')
                                                            query = 'update intrstlr set qualify = "1" where mail = "{}"'.format(mail)
                                                            cur.execute(query)
                                                            cur.execute('commit')
                                                            break
