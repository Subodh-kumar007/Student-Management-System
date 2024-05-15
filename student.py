from tkinter import *
from tkinter import ttk,messagebox
import sqlite3
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x750+0+0")
        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="blue")
        title.pack(side=TOP,fill=X)
        #==========variables============>
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_dob=StringVar()
        #===========student Frame========>
        stu_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        stu_frame.place(x=20,y=100,width=450,height=600)
        m_title=Label(stu_frame,text="Manage Students",font=("times new roman",30,"bold"),bg="crimson",fg="white")
        m_title.grid(row=0,columnspan=2,pady=20)
        
        lbl_roll=Label(stu_frame,text="Roll No.",font=("times new roman",20,"bold"),bg="crimson",fg="white")
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txt_roll=Entry(stu_frame,textvariable=self.var_roll,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(stu_frame,text="Name",font=("times new roman",20,"bold"),bg="crimson",fg="white")
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        txt_name=Entry(stu_frame,textvariable=self.var_name,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_email=Label(stu_frame,text="Email",font=("times new roman",20,"bold"),bg="crimson",fg="white")
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        txt_email=Entry(stu_frame,textvariable=self.var_email,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_gender=Label(stu_frame,text="Gender",font=("times new roman",20,"bold"),bg="crimson",fg="white")
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        combo_gender=ttk.Combobox(stu_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly")
        combo_gender["values"]=("Select","Male","Female","Other")
        combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")
        combo_gender.current(0)
        
        lbl_contact=Label(stu_frame,text="Contact",font=("times new roman",20,"bold"),bg="crimson",fg="white")
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        txt_contact=Entry(stu_frame,font=("times new roman",15,"bold"),textvariable=self.var_contact,bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_dob=Label(stu_frame,text="D.O.B",font=("times new roman",20,"bold"),bg="crimson",fg="white")
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        txt_dob=Entry(stu_frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,textvariable=self.var_dob)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_address=Label(stu_frame,text="Address",font=("times new roman",20,"bold"),bg="crimson",fg="white")
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")
        self.txt_address=Text(stu_frame,width=30,height=4,)
        self.txt_address.grid(row=7,column=1,padx=20,pady=10,sticky="w")
        #===========button frame======>
        but_frame=Frame(stu_frame,bd=4,relief=RIDGE,bg="crimson")
        but_frame.place(x=15,y=520,width=420)
        add=Button(but_frame,text="Add",width=10,command=self.add).grid(row=0,column=0,padx=10,pady=10)
        update=Button(but_frame,text="Update",width=10,command=self.update).grid(row=0,column=1,padx=10,pady=10)
        delete=Button(but_frame,text="Delete",width=10,command=self.delete).grid(row=0,column=2,padx=10,pady=10)
        clear=Button(but_frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

        #===========Details Frame========>
        detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        detail_frame.place(x=500,y=100,width=800,height=600)
        lbl_search=Label(detail_frame,text="Search By",font=("times new roman",20,"bold"),bg="crimson",fg="white")
        lbl_search.grid(row=0,column=0,pady=10,padx=10,sticky="w")

        self.search_by=StringVar()
        self.search_txt=StringVar()

        combo_search=ttk.Combobox(detail_frame,font=("times new roman",13,"bold"),state="readonly",width=12,textvariable=self.search_by)
        combo_search["values"]=("roll","name","contact")
        combo_search.grid(row=0,column=1,pady=10,padx=10,sticky="w")
        combo_search.current(0)
        txt_search=Entry(detail_frame,width=20,font=("times new roman",13,"bold"),bd=5,relief=GROOVE,textvariable=self.search_txt)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        search_but=Button(detail_frame,text="Search",width=10,command=self.search).grid(row=0,column=3,padx=10,pady=10)
        show_but=Button(detail_frame,text="Show All",width=10,command=self.show).grid(row=0,column=4,padx=10,pady=10)

        #=============Table Frame===================>
        table_frame=Frame(detail_frame,bd=4,relief=RIDGE,bg="white")
        table_frame.place(x=10,y=70,width=760,height=510)
        
        scrol_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scrol_y=Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("roll","name","email","gender","contact","dob","Address"),xscrollcommand=scrol_x.set,yscrollcommand=scrol_y.set)
        scrol_x.pack(side=BOTTOM,fill=X)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_x.config(command=self.student_table.xview)
        scrol_y.config(command=self.student_table.yview)

        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("dob",text="Date of Birth")
        self.student_table.heading("Address",text="Address")
        self.student_table["show"]="headings"
        self.student_table.column("roll",width=100)
        self.student_table.column("name",width=150)
        self.student_table.column("email",width=200)
        self.student_table.column("gender",width=100)
        self.student_table.column("contact",width=150)
        self.student_table.column("dob",width=100)
        self.student_table.column("Address",width=200)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_data)    #bind the fun() its called event handaling its give 2 argument
        self.show()
#==================functions================>
    def add(self):
        con=sqlite3.connect(database="stm.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.root)
            elif self.var_name.get()=="":
                messagebox.showerror("Error","Student Name should be required",parent=self.root)
            elif self.var_email.get()=="":
                messagebox.showerror("Error","Email should be required",parent=self.root)
            elif self.var_gender.get()=="Select":
                messagebox.showerror("Error","Gender should be required",parent=self.root)
            elif self.var_contact.get()=="":
                messagebox.showerror("Error","Contact No. should be required",parent=self.root)
            elif self.var_dob.get()=="":
                messagebox.showerror("Error","D.O.B should be required",parent=self.root)
            elif self.txt_address.get("1.0",END).strip()=="":
                messagebox.showerror("Error","Address should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                rows=cur.fetchone()
                #print(rows)
                if rows!=None:
                    messagebox.showerror("Error","this roll No is all ready present",parent=self.root)
                else:
                    cur.execute("insert into student(roll,name,email,gender,contact,dob,address) values(?,?,?,?,?,?,?)",
                                (self.var_roll.get(),self.var_name.get(),self.var_email.get(),self.var_gender.get(),
                                self.var_contact.get(),self.var_dob.get(),self.txt_address.get("1.0",END)
                                ))
                    con.commit()
                    con.close()
                    self.show()
                    self.clear()
                    messagebox.showinfo("Success","Record Added Successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def show(self):
        con=sqlite3.connect(database="stm.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student")
            rows=cur.fetchall()
            #if len(rows!=0):
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
                #con.commit()
            con.close()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def clear(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.search_by.set("roll")
        self.search_txt.set("")
        self.txt_address.delete("1.0",END)

    def get_data(self,ev):
        curosor_row=self.student_table.focus()
        data=self.student_table.item(curosor_row)
        row=data["values"]  #it give the list and set through index no.
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])

    def update(self):
        con=sqlite3.connect(database="stm.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.root)
            elif self.var_name.get()=="":
                messagebox.showerror("Error","Student Name should be required",parent=self.root)
            elif self.var_email.get()=="":
                messagebox.showerror("Error","Email should be required",parent=self.root)
            elif self.var_gender.get()=="Select":
                messagebox.showerror("Error","Gender should be required",parent=self.root)
            elif self.var_contact.get()=="":
                messagebox.showerror("Error","Contact No. should be required",parent=self.root)
            elif self.var_dob.get()=="":
                messagebox.showerror("Error","D.O.B should be required",parent=self.root)
            elif self.txt_address.get('1.0',END).strip()=="":
                messagebox.showerror("Error","Address should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                rows=cur.fetchone()
                #print(rows)
                if rows==None:
                    messagebox.showerror("Error","this roll No. is Not present in List",parent=self.root)
                else:
                    cur.execute("update student set name=?,email=?,gender=?,contact=?,dob=?,address=? where roll=?",
                                (self.var_name.get(),self.var_email.get(),self.var_gender.get(),
                                self.var_contact.get(),self.var_dob.get(),self.txt_address.get("1.0",END),self.var_roll.get()
                                ))
                    con.commit()
                    con.close()
                    self.show()
                    self.clear()
                    messagebox.showinfo("Success","Record Update Successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def delete(self):
        con=sqlite3.connect(database="stm.db")
        cur=con.cursor()
        if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.root)
        else:
            cur.execute("delete from student where roll=?",(self.var_roll.get(),))
            con.commit()
            con.close()
            self.show()
            self.clear()

    def search(self):
        con=sqlite3.connect(database="stm.db")
        cur=con.cursor()
        try:
            cur.execute(f"select * from student where {self.search_by.get()} LIKE '%{self.search_txt.get()}%'")
            rows=cur.fetchall()
            if rows==None:
                messagebox.showerror("Error",f"{self.search_by.get()} Not Found",parent=self.root)
            else:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert('',END,values=row)
                    #con.commit()
                con.close()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

root=Tk()
obj=Student(root)
root.mainloop()