from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import *
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import os
import sqlite3

class RMS:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #********* icon *********
        self.logo_dash = ImageTk.PhotoImage(file="Images/logo_p.png")
        #********* title *********
        title = Label(self.root,text="Student Result Management System",padx=10,compound=LEFT,image=self.logo_dash,font = ("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1) 

        #********* Menue *********
        M_Frame = LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=20,y=70,width=1320,height=70)

        btn_course = Button(M_Frame,text="Course",font=("gooudy old style",12,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=90,y=5,width=170,height=35)
        btn_Student = Button(M_Frame,text="Student",font=("gooudy old style",12,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=280,y=5,width=170,height=35)
        btn_Result = Button(M_Frame,text="Result",font=("gooudy old style",12,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=470,y=5,width=170,height=35)
        btn_View = Button(M_Frame,text="View Student Result",font=("gooudy old style",12,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=660,y=5,width=170,height=35)
        btn_Logout = Button(M_Frame,text="Logout",font=("gooudy old style",12,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=850,y=5,width=170,height=35)
        btn_Exit = Button(M_Frame,text="Exit",font=("gooudy old style",12,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_).place(x=1040,y=5,width=170,height=35)

        #********* Content Window *********
        self.bg_img=Image.open("images/bg.png")
        self.bg_img=self.bg_img.resize((920,350),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)

        #********* Update Details Label *********
        self.lbl_course=Label(self.root,text="Total Course's\n [ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=530,width=300,height=100)

        self.lbl_student=Label(self.root,text="Total Student's\n [ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=710,y=530,width=300,height=100)

        self.lbl_result=Label(self.root,text="Total Result's\n [ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=1020,y=530,width=300,height=100)
        
        #******* clock ********

        self.lbl=Label(self.root,text="\n Webcode Clock",font=("Book Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=10,y=180,height=450,width=350)
       
        self.working()

        #********* footer *********
        footer = Label(self.root,text="SRMS--Student Result Management System        Contact No :- 8554039117 / 9325210736        Made By :- Omkar & Shreyash",font = ("goudy old style",13),bg="#262626",fg="white").pack(side=BOTTOM,fill=X) 
        self.update_details()
    
    def update_details(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses \n[{str(len(cr))}]")

            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Student's \n[{str(len(cr))}]")

            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Result's \n[{str(len(cr))}]")

            self.lbl_course.after(200,self.update_details)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    
    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)

        bg=Image.open("images/c.png")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))

        #****** Hr Line ******
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
        #****** Min Line Image ******
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="white",width=3)
        #****** Min Line Image ******
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="yellow",width=2)
        draw.ellipse((195,195,210,210),fill="#1AD5D5")
        clock.save("images/clock_new.png")
    
    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second

        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360

        self.clock_image(hr, min_, sec_)
        self.img=ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)    
        self.lbl.after(200,self.working)
    
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)
    
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)

    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)

    def logout(self):
        op=messagebox.askyesno("Confirm","Do you want to logout.?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")

    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you want to Exit.?",parent=self.root)
        if op==True:
            self.root.destroy()
            

if __name__=="__main__":
    root = Tk()
    obj=RMS(root)
    root.mainloop()