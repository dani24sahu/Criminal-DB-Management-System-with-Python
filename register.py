from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry('1530x790+0+0')

        # =========== Variables ================== #
        self.var_fname = StringVar()
        self.var_lastname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_sec_quest = StringVar()
        self.var_sec_ans = StringVar()
        self.var_password = StringVar()
        self.var_conf_password = StringVar()
        self.var_check = IntVar()

        #bg_image
        self.bg = ImageTk.PhotoImage(file="images/img4.jpg")
        bg_lbl = Label(self.root,image = self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #leftside_image
        self.bg1 = ImageTk.PhotoImage(file="images/img5.jpg")
        left_lbl = Label(self.root,image = self.bg1)
        left_lbl.place(x=50,y=100,width=440,height=550)

        #creating main frame
        frame = Frame(self.root,bg='white')
        frame.place(x=490,y=100,width=730,height=550)

        register_lbl = Label(frame,text="Register Here",font=("Times New Roman",20,"bold"),fg="dark green",bg="white")
        register_lbl.place(x=20,y=20)

        #label and entries...........
        fname = Label(frame,text="First Name:",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry = ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",13,"bold"))
        fname_entry.place(x=50,y=130,width=200)

        last_name = Label(frame,text="Last Name:",font=("times new roman",15,"bold"),bg="white",fg="black")
        last_name.place(x=370,y=100)

        self.txt_lastname = ttk.Entry(frame,textvariable=self.var_lastname,font=("times new roman",13,"bold"))
        self.txt_lastname.place(x=370,y=130,width=200)

        contact = Label(frame,text="Contact No:",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",13,"bold"))
        self.txt_contact.place(x=50,y=200,width=200)

        email = Label(frame,text="Email ID:",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",13,"bold"))
        self.txt_email.place(x=370,y=200,width=200)

        sec_ques = Label(frame,text="Select Security Question:",font=("times new roman",15,"bold"),bg="white",fg="black")
        sec_ques.place(x=50,y=240)

        self.combo_sec_quest = ttk.Combobox(frame,textvariable=self.var_sec_quest,font=("times new roman",13,"bold"),state="readonly")
        self.combo_sec_quest["values"] = ("Select","Your Birth Place","Your Pet Name","Your Friend's Name")
        self.combo_sec_quest.place(x=50,y=270,width=250)



        sec_ans = Label(frame,text="Security Answer:",font=("times new roman",15,"bold"),bg="white",fg="black")
        sec_ans.place(x=370,y=242)

        self.txt_sec_ans = ttk.Entry(frame,textvariable=self.var_sec_ans,font=("times new roman",13,"bold"))
        self.txt_sec_ans.place(x=370,y=272,width=200)

        password = Label(frame,text="Password:",font=("times new roman",15,"bold"),bg="white",fg="black")
        password.place(x=50,y=320)

        self.txt_password = ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",13,"bold"))
        self.txt_password.place(x=50,y=347,width=200)

        conf_password = Label(frame,text="Confirm Password:",font=("times new roman",15,"bold"),bg="white",fg="black")
        conf_password.place(x=370,y=320)

        self.txt_conpassword = ttk.Entry(frame,textvariable=self.var_conf_password,font=("times new roman",13,"bold"))
        self.txt_conpassword.place(x=370,y=347,width=200)

        #Checkbutton.........
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions", font=("times new roman",13,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=400)


        btn_register=Button(frame,command=self.register_data,text='Register',font=('arial',13,'bold'),width=14,bg='Red',fg='white')
        btn_register.place(x=140,y=440)

        btn_loginNow=Button(frame,text='Login Now',font=('arial',13,'bold'),width=14,bg='light blue',fg='white')
        btn_loginNow.place(x=380,y=440)

    
    # =================== function declaration ===================#

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_sec_quest.get()=="Select":
            messagebox.showerror("Error", "All Fields are required")
        elif self.var_password.get()!=self.var_conf_password.get():    
            messagebox.showerror("Error","Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree Terms & Conditions")    
        else:
            connect = mysql.connector.connect(host='localhost',user='dani',password='root',database='management')   
            my_curs = connect.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_curs.execute(query,value)
            row = my_curs.fetchone()
            if row!=None:
                messagebox.showerror("Error","Username already exist. Please try another email")
            else:
                my_curs.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                       self.var_fname.get(),
                                                                                       self.var_lastname.get(),
                                                                                       self.var_contact.get(),
                                                                                       self.var_email.get(),
                                                                                       self.var_sec_quest.get(),
                                                                                       self.var_sec_ans.get(),
                                                                                       self.var_password.get()
                                                                                     )) 
            connect.commit()
            connect.close()
            messagebox.showinfo("Success","Registered Successfully!")





if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()        