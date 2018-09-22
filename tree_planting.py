from tkinter import *

def init(data):
    # load data.xyz as appropriate
    data.started=False
    data.oneHour=False

    data.tree1=PhotoImage(file="/Users/vicky/Desktop/tree1.gif")
    data.tree2=PhotoImage(file="/Users/vicky/Desktop/tree2.gif")
    data.tree3=PhotoImage(file="/Users/vicky/Desktop/tree3.gif")
    data.deadline=PhotoImage(file="/Users/vicky/Desktop/deadline.gif")
    data.goodjob=PhotoImage(file="/Users/vicky/Desktop/goodjob.gif")

    data.level=1
    data.timer=0
    data.hour=0
    data.minute=0

    data.rectangleOne=False
    data.rectangleTwo=False
    
def mousePressed(event,data):
    # use event.x and event.y
    if (event.x>=100 and event.x<=500 and event.y>=120 and event.y<=260) and data.oneHour==True:
        data.level+=1
        data.rectangleOne=True
    if (event.x>=100 and event.x<=500 and event.y>=340 and event.y<=480) and data.oneHour==True:
        data.rectangleTwo=True
        
def keyPressed(event,data):
    # use event.char and event.keysym
    data.started=True
    if data.rectangleOne == True or data.rectangleTwo==True:
        data.rectangleOne=False
        data.rectangleTwo=False
        data.timer=0
        data.hour=0
        data.minute=0
        data.oneHour=False
def timerFired(data):
    if data.started==True:
        data.timer+=1
    if data.timer==60:
        data.minute+=1
        data.timer=0
    if data.minute==60:
        data.minute=0
        data.hour+=1
        data.oneHour=True

def redrawAll(canvas, data):
    # draw in canvas
    if data.started==False:
        canvas.create_text(300,100,text="Welcome to the procrastination warning! Here are the basic instructions.")
        canvas.create_text(300,180,text="1. Once the timer starts, you should concentrate on your own work and")
        canvas.create_text(300,200,text="get rid of those distracting or entertaining softwares.")
        canvas.create_text(300,260,text="2. After an hour, you will be facing with two options: one is that you:")
        canvas.create_text(300,280,text="keep on track for the entire hour, the other is that you procrastinate again. ")
        canvas.create_text(300,340,text="3. If you choose the first one, the tree will grow automatically; ")
        canvas.create_text(300,360,text="if your answer is the second one, it won’t grow :(")
        canvas.create_text(300,420,text="4. Also, there will some special BONUS effects after each choice.")
        canvas.create_text(300,500,text="5. Start your trip! Become a self-disciplined IB student! ")
        canvas.create_text(300,550,text="Press any key to start!",fill="red")
 
    else:
        if data.level==1:
            canvas.create_image(300,300,anchor=NW,image=data.tree1)
        if data.level==2:
            canvas.create_image(300,300,anchor=NW,image=data.tree2)
        if data.level==3:
            canvas.create_image(300,300,anchor=NW,image=data.tree3)
       
        canvas.create_text(300,50,text="%d : %d : %d"%(data.hour,data.minute,data.timer))
    if data.oneHour==True:
        canvas.create_rectangle(100,120,500,260,fill="orange",outline="black")
        canvas.create_rectangle(100,340,500,480,fill="orange",outline="black")
        canvas.create_text(300,190,text="I have concentrated on my work for an hour")
        canvas.create_text(300,410,text="I procrastinated again.")
    if data.rectangleOne == True:
        canvas.create_image(10,100,anchor=NW,image=data.goodjob)
        canvas.create_text(300,200,text="Press any key to continue.")
    if data.rectangleTwo==True:
        canvas.create_image(100,300,anchor=NW,image=data.deadline)
        canvas.create_text(300,300,text="DEADLINE IS NEAR",fill="red",font=("Comic Sans MS", 36))
        canvas.create_text(300,200,text="Press any key to continue.")
    if data.level==3:
        canvas.create_text(300,200,text="Congratulations!",fill="red")
        canvas.create_text(300,300,text="You have continuted working for three hours!")
        canvas.create_text(300,400,text="Take a rest!",fill="blue")       
        
def run(width=600, height=600):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event,canvas,data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas,data)

    def timerFiredWrapper(canvas,data):
        timerFired(data)
        redrawAllWrapper(canvas,data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 10 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(600,600)

