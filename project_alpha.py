from tkinter import *
def clear(window):
    window.destroy()

def alpha():
    
    window=Tk()
    window.geometry("680x650")
    window.configure(bg="black")
    window.title("Alpha Centauri")

    bgimage=PhotoImage(file="\\\srlab\\tcdata\system28\Documents\Shourya_XII-A\\Un bg.png")
    bglabel=Label(window,image=bgimage).grid(rowspan=10,columnspan=10,pady=50)

    Label(window,text="ALPHA CENTAURI",width=33,
          font=("Elephant",20),justify="center",borderwidth=2,relief="groove",highlightbackground="white",highlightcolor="white",
          bg="black",fg="white").grid(row=0,columnspan=2,column=0)
    image=PhotoImage(file="\\\srlab\\tcdata\system28\Documents\Shourya_XII-A\\alpha.png")
    Label(window,image=image).grid(row=1,column=1)


    Label(window,text="""• Alpha Centauri is the closest
    planetary system to the Solar System
    at 4.37 light-years from the Sun.
    It is a triple star system, consisting of
    three stars:""",
          bg="black",width=35,justify="left",
          fg="white",
          font=("GillSansMTCondensed",10)).grid(row=1,column=0)

    Label(window,text="""• ALPHA CENTAURI A (Rigil
    Kentaurus): It is the principal
    member, or primary, of the binary
    system.  Alpha Centauri A is about
    10 percent more massive than the
    Sun,[7] with a radius about 22 percent
    larger.""",
          bg="black",width=35,justify="left",
          fg="white",
          font=("GillSansMTCondensed",10)).place(x=40,y=220)

    Label(window,text="""• ALPHA CENTAURI B (Toliman): It
    is the secondary star of the binary
    system. It is a main-sequence star
    of spectral type K1 V, making it more
    an orange colour than Alpha Centauri
    A; it has around 90 percent the mass
    of the Sun and a 14 percent smaller
    diameter.""",
          bg="black",width=35,
          fg="white",
          font=("GillSansMTCondensed",10),justify="left").place(x=40,y=350)

    Label(window,text="""• ALPHA CENTAURI C( Proxima
    Centauri): It is a small main-sequence
    red dwarf of spectral class M6 Ve.""",
          bg="black",width=35,
          fg="white",
          font=("GillSansMTCondensed",10),justify="left").grid(row=3,column=0)

    LF=LabelFrame(window,text="Spacecraft Details",font=("",10,"bold"),bg="black",width=190,height=150,
                  fg="white").grid(row=2,
                  column=1,rowspan=2, sticky='EWNS',
                  padx=10, pady=5, ipadx=5,
                  ipady=5)
    image1=PhotoImage(file="\\\srlab\\tcdata\system28\Documents\Shourya_XII-A\\proxima craft.png")

    L=Label(LF,image=image1).grid(row=2,column=1,pady=40)
    Label(LF,text="Name : ALPHA-450-Z\nTop Speed : 5,793,984,000,000 mph",fg="white",bg="black",font=("Impact",12)).grid(row=3,column=1,ipady=0)

    b1=Button(window,text="Continue",font=("Impact",15),bg="grey",width=10,command=lambda:clear(window)).grid(row=4,column=1)
    window.mainloop()



