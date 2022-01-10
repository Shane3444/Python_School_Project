from tkinter import *
def clear(windowp):
    windowp.destroy()
def proxima():
    
    windowp=Tk()
    windowp.geometry("650x650")
    windowp.configure(bg="black")
    windowp.title("Proxima Centauri")

    bgimage=PhotoImage(file="\\\srlab\\tcdata\system28\Documents\Shourya_XII-A\\Un bg.png")
    bglabel=Label(windowp,image=bgimage).grid(rowspan=10,columnspan=10)

    Label(windowp,text="PROXIMA CENTAURI",width=33,
          font=("Elephant",20),justify="center",borderwidth=2,relief="groove",highlightbackground="white",highlightcolor="white",
          bg="black",fg="white").grid(row=0,columnspan=2,column=0,padx=10,pady=5)
    image=PhotoImage(file="\\\srlab\\tcdata\system28\Documents\Shourya_XII-A\\proxima.png")
    Label(windowp,image=image).grid(row=1,column=1)


    Label(windowp,text="""• Proxima Centauri is about
    4.244 light-years  from the Sun. 
    Proxima Centauri is a red
    dwarf, because it belongs
    to the main sequence on the
    Hertzsprung–Russell diagram
    and is of spectral class M5.5.
    """,
          bg="black",width=30,justify="left",
          fg="white",
          font=("GillSansMTCondensed",10)).place(x=40,y=100)

    Label(windowp,text="""• Proxima Centauri has been the
    closest star to  the  Sun for
    about 32,000 years and will be
    so for about another 25,000 years.""",
          bg="black",width=30,justify="left",
          fg="white",
          font=("GillSansMTCondensed",10)).grid(row=2,column=0)

    Label(windowp,text="""• Proxima Centauri b is a planet
    orbiting the star at a distance of 7.5
    million km with an orbital period
    of approximately 11.2 Earth days.
    A short visit to it is inclusive.""",
          bg="black",width=30,
          fg="white",
          font=("GillSansMTCondensed",10),justify="left").grid(row=3,column=0)


    LF=LabelFrame(windowp,text="Spacecraft Details",font=("",10,"bold"),bg="black",width=190,height=250,
                  fg="white").grid(row=2,
                  column=1,rowspan=2, sticky='EWNS',
                  padx=10, pady=5, ipadx=5,
                  ipady=5)
    image1=PhotoImage(file="\\\srlab\\tcdata\system28\Documents\Shourya_XII-A\\proxima craft.png")

    L=Label(LF,image=image1).grid(row=2,column=1,pady=40)
    Label(LF,text="Name : ALPHA-450-Z\nTop Speed : 5,793,984,000,000 mph",fg="white",bg="black",font=("Impact",12)).grid(row=3,column=1,ipady=0)

    b1=Button(windowp,text="Continue",font=("Impact",15),bg="grey",width=10,command=lambda:clear(windowp)).grid(row=4,column=1)
    windowp.mainloop()


