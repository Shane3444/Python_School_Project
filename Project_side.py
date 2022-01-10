from tkinter import messagebox
import mysql.connector,matplotlib.pyplot as polo
def admin():
      a=0
      while a==0:
            print("_"*78)
            print('-'*78)
            print('\t\t\t\tWELCOME ADMIN !')
            print("\t\t\t\t SALES~REPORT")
            print('-'*78)       
            print('\t\t      +---------------------------------+')
            print('\t\t      |     S NO.    |     OPTIONS      |')
            print('\t\t      +---------------------------------+')
            print('\t\t      |       1      | TCODE-WISE SALES |')
            print('\t\t      |       2      |  MONTHLY SALES   |')
            print('\t\t      |       3      |    EXIT MENU     |')
            print('\t\t      +---------------------------------+')
            c5=int(input(" ENTER YOUR CHOICE              : "))
            conn=mysql.connector.connect(
                  host="localhost",
                  user="root",
                  passwd="tiger",
                  database="system28")
            cur=conn.cursor()
            if c5==1:
                  print("~"*78)
                  x1="select * from saletable"
                  cur.execute(x1)
                  tsales=cur.fetchall()
                  tc=['Mars\ntc1','Proxima Centauri\ntc2','Alpha Centauri\ntc3','Keplar 452-B\ntc4']
                  polo.xticks([1,2,3,4],labels=tc)
                  totsales=[]
                  for i in tsales:
                        totsales.append(i[1])
                        '''"#FFFF00","#0000FF","#80FF00","#7F00FF","#00FF00","#FF00FF","#00FF80","#FF007F"]'''
                  polo.ylabel("Total Sales")
                  polo.title("T-CODE Wise SALES REPORT")
                  polo.xlabel("T-Code")            
                  polo.bar([1,2,3,4],totsales,width=0.5,
                           color=["#FF0000","#00FFFF","#FF8000","#0080FF"])
                  polo.show()
                  print("""\n\n\t\t           +-------------+------------+
\t\t           | Ticket Code | Total Sale |
\t\t           +-------------+------------+""")
                  for i in tsales:
                        print("\t\t           |   {}|{}  |".format(i[0].ljust(10),str(i[1]).rjust(10)))
                  print("\t\t           +-------------+------------+\n\n")
                  print("~"*78)   
            elif c5==2:
                  print("~"*78)
                  x1="select * from monthsale"
                  cur.execute(x1)
                  tsales=cur.fetchall()
                  totsales=[]
                  mn1=[]
                  mn=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
                  polo.xticks([1,2,3,4,5,6,7,8,9,10,11,12],labels=mn)
                  for i in tsales:
                        totsales.append(i[1])
                  polo.ylabel("Total Sales")
                  polo.title("MONTHLY SALES REPORT ")
                  polo.xlabel("Month")            
                  polo.bar([1,2,3,4,5,6,7,8,9,10,11,12],totsales,width=0.3
                           ,color=["#FF0000","#00FFFF","#FF8000","#0080FF","#FFFF00","#0000FF","#80FF00","#7F00FF","#00FF00","#FF00FF","#00FF80","#FF007F"])
                  polo.show()
                  print("""\n\n\t\t           +-------------+------------+
\t\t           |    Month    | Total Sale |
\t\t           +-------------+------------+""")
                  for i in tsales:
                        print("\t\t           |   {}|{}  |".format(str(i[0]).ljust(10),str(i[1]).rjust(10)))
                  print("\t\t           +-------------+------------+\n\n")
                  print("~"*78)
            elif c5==3:
                  print("~"*78)
                  a=1
                  print(" Exiting\n Visit again ! ")
                  print("~"*78)
            else:
                  tk=Tk()
                  messagebox.showerror("CHOICE ERROR","Invalid Choice\nPlease Try Again.")
                  tk.destroy()
