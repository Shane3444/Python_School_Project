from tkinter import *
def clear(window):
    window.destroy()

def kepler():
    window=Tk()
    window.geometry("690x660")
    window.configure(bg="black")
    window.title("Kepler 452B")

    bgimage=PhotoImage(file="\\\srlab\\tcdata\system28\Documents\Shourya_XII-A\\Un bg.png")
    bglabel=Label(window,image=bgimage).grid(rowspan=10,columnspan=10,pady=50)

    Label(window,text="KEPLAR 452B",width=33,
          font=("Elephant",20),justify="center",borderwidth=2,relief="groove",highlightbackground="white",highlightcolor="white",
          bg="black",fg="white").grid(row=0,columnspan=2,column=0)
    image=PhotoImage(file="\\\srlab\\tcdata\system28\Documents\Shourya_XII-A\\kepler.png")
    Label(window,image=image).grid(row=1,column=1)


    Label(window,text="""• Kepler-452b is an exoplanet orbiting
    the Sun-like star Kepler-452 about
    1,402 light-years from Earth in the
    constellation Cygnus.  It is the
    first potentially rocky super-Earth
    planet discovered orbiting
    within the habitable zone of a star
    very similar to the Sun.""",
          bg="black",width=35,justify="left",
          fg="white",
          font=("GillSansMTCondensed",10)).grid(row=1,column=0)

    Label(window,text="""• It is a terrestrial planet, a
    super-Earth with many active volcanoes
    due to its higher mass and density.
    The clouds on the planet would be
    thick and misty, covering much of
    the surface as viewed from space.
    All of the planets components would
    be the same if it is as we predicted
    it to be.""",
          bg="black",width=35,justify="left",
          fg="white",
          font=("GillSansMTCondensed",10)).grid(row=2,column=0)

    Label(window,text="""• The planet takes 385 Earth days to
    orbit its star. Its radius is 50%
    bigger than Earth's. It has an
    equilibrium temperature of 265 K (−8 °C)
    a little warmer than Earth.""",
          bg="black",width=35,
          fg="white",
          font=("GillSansMTCondensed",10),justify="left").grid(row=3,column=0)

    LF=LabelFrame(window,text="Spacecraft Details",font=("",10,"bold"),bg="black",width=190,height=130,
                  fg="white").grid(row=2,
                  column=1,rowspan=2, sticky='EWNS',
                  padx=10, pady=5, ipadx=5,
                  ipady=5)
    image1=PhotoImage(file="\\\srlab\\tcdata\system28\Documents\Shourya_XII-A\\kepler craft.png")

    L=Label(LF,image=image1).grid(row=2,column=1,pady=40)
    Label(LF,text="Name : PSLV-Vol-2\nTop Speed : 5,800,500,000,000 mph",fg="white",bg="black",font=("Impact",12)).grid(row=3,column=1,ipady=0)

    b1=Button(window,text="Continue",font=("Impact",15),bg="grey",width=10,command=lambda:clear(window)).grid(row=4,column=1)
    window.mainloop()



