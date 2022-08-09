from tkinter import *
import pyscreenrec

root=Tk()
root.geometry('400x600')
root.title("screen recorder")
root.config(bg="#fff")
root.resizable(False,False)

def start_rec():
    file=Filename.get()
    rec.start_recording(str(file+".mp4"),20)
    win = Tk()
    win.config(bg="white")
    win.geometry("750x95")
    Label(win, text="RECORDING HAS BEEN STARTED",
          font=('Helvetica 22 bold'), fg='black', bg='white').place(x=145, y=20)
    win.after(1200, lambda: win.destroy())
    win.mainloop()

def pause_rec():
    rec.pause_recording()
    win = Tk()

    win.config(bg="white")
    win.geometry("750x95")
    Label(win, text="RECORDING HAS BEEN PAUSED",
          font=('Helvetica 22 bold'), fg='black', bg='white').place(x=145, y=20)
    win.after(1200, lambda: win.destroy())
    win.mainloop()

def resume_rec():
    rec.resume_recording()
    win = Tk()

    win.config(bg="white")
    win.geometry("750x95")
    Label(win, text="RECORDING HAS BEEN RESUME",
          font=('Helvetica 22 bold'), fg='black', bg='white').place(x=145, y=20)
    win.after(1200, lambda: win.destroy())
    win.mainloop()

def stop_rec():
    rec.stop_recording()
    win = Tk()

    win.config(bg="white")
    win.geometry("750x95")
    Label(win, text="RECORDING HAS BEEN STOPPED",
          font=('Helvetica 22 bold'), fg='black', bg='white').place(x=145, y=20)
    win.after(1200, lambda: win.destroy())
    win.mainloop()


rec=pyscreenrec.ScreenRecorder()

#icon
image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)

#background images
image1=PhotoImage(file="yelllow.png")
Label(root,image=image1,bg="#fff").place(x=2,y=35)
image2=PhotoImage(file="blue.png")
Label(root,image=image2,bg="#fff").place(x=223,y=260)

#heading
lb1=Label(root,text='Screen Recorder',bg="#fff",font="arial 15 bold")
lb1.pack(pady=20)

image3=PhotoImage(file="recording.png")
Label(root,image=image3,bd=0).pack(pady=30)


#entry
Filename=StringVar()
entry=Entry(root,textvariable=Filename,width=17,bd=4,font="arial 15")
entry.place(x=100,y=352)
Filename.set("-----untitled name-----")

#buttons:-
start=Button(root,text="PLAY",font="bold 21",bd=1,command=start_rec)
start.place(x=137,y=249)


#PAUSE BUTTON
image4=PhotoImage(file="pause copy.png")
pause=Button(root,image=image4,bd=0,bg="#fff",command=pause_rec)
pause.place(x=50,y=450)
pause_label =Label(root,text="PAUSE", fg='Black',bg='#fff')
pause_label.place(x=65,y=530)


#RESUME BUTTON
image5=PhotoImage(file="resume copy.png")
resume=Button(root,image=image5,bd=0,bg="#fff",command=resume_rec)
resume .place(x=150,y=450)
resume_label =Label(root,text="RESUME", fg='Black',bg='#fff')
resume_label.place(x=163,y=530)

#STOP BUTTON
image6=PhotoImage(file="stop copy.png")
stop=Button(root,image=image6,bd=0,bg="#fff",command=stop_rec)
stop.place(x=250,y=450)
stop_label =Label(root,text="STOP", fg='Black',bg='#fff')
stop_label.place(x=269,y=530)
root.mainloop()
