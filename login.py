from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

def main():
    win = Tk()
    app = Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry('1530x790+0+0')

        #taking bg image
        self.bg = ImageTk.PhotoImage(file="images/img4.jpg")
        lbl_bg = Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        #login_frame
        frame = Frame(self.root,bg='black')
        frame.place(x=470,y=170,width=340,height=450)

        img1 = Image.open('images/logo1.jpg')
        img1 = img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lbl_img1 = Label(image=self.photoimage1,bg='black',borderwidth=0)
        lbl_img1.place(x=595,y=175,width=100,height=100)

        get_strt =Label(frame,text="Get Started",font=("Times New Romen", 15,'bold'),fg='white',bg='black')
        get_strt.place(x=112,y=100)

        #Labels for entries
        username_lbl = Label(frame,text="Username",font=("Times New Romen", 13,'bold'),fg='green',bg='black')
        username_lbl.place(x=130,y=180)

        self.txtuser= ttk.Entry(frame,font=("Times New Romen", 13,'bold'))
        self.txtuser.place(x=75,y=205,width=200)

        password_lbl = Label(frame,text="Password",font=("Times New Romen", 13,'bold'),fg='green',bg='black')
        password_lbl.place(x=130,y=245)

        self.txtpass= ttk.Entry(frame,font=("Times New Romen", 13,'bold'))
        self.txtpass.place(x=75,y=270,width=200)

        #buttons
        login_btn=Button(frame,command=self.login,text="Login",font=("Times New Romen",13,"bold"),bd=3,relief=RIDGE,activeforeground="white",activebackground="black",bg="black",fg="white")
        login_btn.place(x=125,y=310,width=100,height=25)

        register_btn=Button(frame,text="New Registeration",command=self.register_win,font=("Times New Romen",11,"bold"),borderwidth=0,relief=RIDGE,activeforeground="white",activebackground="black",bg="black",fg="white")
        register_btn.place(x=100,y=350,width=150,height=20)

        forget_btn=Button(frame,text="Forget Password",command=self.forget_pass_win,font=("Times New Romen",11,"bold"),borderwidth=0,relief=RIDGE,activeforeground="white",activebackground="black",bg="black",fg="white")
        forget_btn.place(x=100,y=370,width=150,height=20)

    def register_win(self):   
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)
    
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All fields are required")   
        else:
            connect = mysql.connector.connect(host='localhost',user='dani',password='root',database='management')   
            my_curs = connect.cursor()
            my_curs.execute("Select * from register where email=%s and password=%s",(
                                                                                      self.txtuser.get(),
                                                                                      self.txtpass.get()
                                                                                    ))
            
            row = my_curs.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                open_main = messagebox.askyesno("YesNo","Access Only Admin")    
                if open_main>0:
                    self.new_window = Toplevel(self.root)
                    self.app = Criminal(self.new_window)
                else:
                    if not open_main:
                        return

            connect.commit()
            connect.close()
    

    def forget_pass_win(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the email address to reset password")
        else:
            connect = mysql.connector.connect(host='localhost',user='dani',password='root',database='management')   
            my_curs = connect.cursor()
            query = ("select * from register where email=%s")   
            value = (self.txtuser.get(),)
            my_curs.execute(query,value)
            row = my_curs.fetchone()
            print(row)

            if row == None:
                messagebox.showerror("My Error","Please Enter The Valid Username")
            else:
                connect.close()    
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                lbl = Label(self.root2,text="Forget Password",font=("Times New Romen",20,"bold"),fg="red",bg="white")
                lbl.place(x=0,y=10,relwidth=1)


                sec_ques = Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),bg="white",fg="black")
                sec_ques.place(x=50,y=80)

                self.combo_sec_quest = ttk.Combobox(self.root2,font=("times new roman",13,"bold"),state="readonly")
                self.combo_sec_quest["values"] = ("Select","Your Birth Place","Your Pet Name","Your Friend's Name")
                self.combo_sec_quest.place(x=50,y=115,width=250)



                sec_ans = Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),bg="white",fg="black")
                sec_ans.place(x=50,y=180)

                self.txt_sec_ans = ttk.Entry(self.root2,font=("times new roman",13,"bold"))
                self.txt_sec_ans.place(x=50,y=215,width=200)


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


class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('CRIMINAL DATABASE MANAGEMENT')

        #creating and getting variable data

        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_name=StringVar()
        self.var_nickname=StringVar()
        self.var_arrest_date=StringVar()
        self.var_dateofcrime=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occupation=StringVar()
        self.var_birthmark=StringVar()
        self.var_crime=StringVar()
        self.var_father_name=StringVar()
        self.var_gender=StringVar()
        self.var_wanted=StringVar()

        lbl_title=Label(self.root,text='CRIMINAL DATABASE MANAGEMENT SYSTEM ',font=('times new roman',30,'bold'),bg='black',fg='gold')
        lbl_title.place(x=0,y=0,width=1350,height=70)

        #main_logo
        img_logo=Image.open('images/logo.png')
        img_logo=img_logo.resize((60,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=20,y=5,width=60,height=50)


        #img_Frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=70,width=1350,height=130)

        #img1
        img1=Image.open('images/img1.jpg')
        img1=img1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=520,height=160)

        #img2
        img2=Image.open('images/img2.jpg')
        img2=img2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=540,y=0,width=500,height=160)

        #img3
        img3=Image.open('images/img3.png')
        img3=img3.resize((400,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=980,y=0,width=280,height=150)


        #table_frame
        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=10,y=200,width=1245,height=560)

          #upper_frame
        up_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Criminal Details',font=('times new roman',11,'bold'),bg='silver',fg='green')
        up_frame.place(x=10,y=10,width=1220,height=270) 



          #label-entries

          #case-id
        caseId=Label(up_frame,text='Case-ID:',font=('arial',11,'bold'),bg='silver')  
        caseId.grid(row=0,column=0,padx=2,sticky=W)

        
        caseEntry=ttk.Entry(up_frame,textvariable=self.var_case_id,width=22,font=('arial',11,'bold')) 
        caseEntry.grid(row=0,column=1,padx=2,sticky=W) 

          #criminal-num
        lbl_criminal_num=Label(up_frame,text='Criminal NO:',font=('arial',11,'bold'),bg='silver')  
        lbl_criminal_num.grid(row=0,column=2,padx=2,pady=7,sticky=W) 

        txt_criminal_num=ttk.Entry(up_frame,textvariable=self.var_criminal_no,width=22,font=('arial',11,'bold')) 
        txt_criminal_num.grid(row=0,column=3,padx=2,pady=7,sticky=W)  

          #criminal-name
        lbl_name=Label(up_frame,text='Criminal Name:',font=('arial',11,'bold'),bg='silver')  
        lbl_name.grid(row=1,column=0,padx=2,pady=7,sticky=W) 

        txt_name=ttk.Entry(up_frame,textvariable=self.var_name,width=22,font=('arial',11,'bold')) 
        txt_name.grid(row=1,column=1,padx=2,pady=7,sticky=W)  


          #nickname
        lbl_nickname=Label(up_frame,text='Nickname:',font=('arial',11,'bold'),bg='silver')  
        lbl_nickname.grid(row=1,column=2,padx=2,pady=7,sticky=W) 

        txt_nickname=ttk.Entry(up_frame,textvariable=self.var_nickname,width=22,font=('arial',11,'bold')) 
        txt_nickname.grid(row=1,column=3,padx=2,pady=7,sticky=W)  

          #arrest-date
        lbl_arrestDate=Label(up_frame,text='Arrest Date:',font=('arial',11,'bold'),bg='silver')  
        lbl_arrestDate.grid(row=2,column=0,padx=2,pady=7,sticky=W) 

        txt_arrestDate=ttk.Entry(up_frame,textvariable=self.var_arrest_date,width=22,font=('arial',11,'bold')) 
        txt_arrestDate.grid(row=2,column=1,padx=2,pady=7,sticky=W)

          #dateofcrime
        lbl_dateofcrime=Label(up_frame,text='Date Of Crime:',font=('arial',11,'bold'),bg='silver')  
        lbl_dateofcrime.grid(row=2,column=2,padx=2,pady=7,sticky=W) 

        txt_dateofcrime=ttk.Entry(up_frame,textvariable=self.var_dateofcrime,width=22,font=('arial',11,'bold')) 
        txt_dateofcrime.grid(row=2,column=3,padx=2,pady=7,sticky=W) 

          #address
        lbl_address=Label(up_frame,text='Address:',font=('arial',11,'bold'),bg='silver')  
        lbl_address.grid(row=3,column=0,padx=2,pady=7,sticky=W) 

        txt_address=ttk.Entry(up_frame,textvariable=self.var_address,width=22,font=('arial',11,'bold')) 
        txt_address.grid(row=3,column=1,padx=2,pady=7,sticky=W) 

          #age
        lbl_age=Label(up_frame,text='Age:',font=('arial',11,'bold'),bg='silver')  
        lbl_age.grid(row=3,column=2,padx=2,pady=7,sticky=W) 

        txt_age=ttk.Entry(up_frame,textvariable=self.var_age,width=22,font=('arial',11,'bold')) 
        txt_age.grid(row=3,column=3,padx=2,pady=7,sticky=W) 

          #occupation
        lbl_occupation=Label(up_frame,text='Occupation:',font=('arial',11,'bold'),bg='silver')  
        lbl_occupation.grid(row=4,column=0,padx=2,pady=7,sticky=W) 

        txt_occupation=ttk.Entry(up_frame,textvariable=self.var_occupation,width=22,font=('arial',11,'bold')) 
        txt_occupation.grid(row=4,column=1,padx=2,pady=7,sticky=W) 

          #birthMark
        lbl_birthMark=Label(up_frame,text='Birth Mark:',font=('arial',11,'bold'),bg='silver')  
        lbl_birthMark.grid(row=4,column=2,padx=2,pady=7,sticky=W) 

        txt_birthMark=ttk.Entry(up_frame,textvariable=self.var_birthmark,width=22,font=('arial',11,'bold')) 
        txt_birthMark.grid(row=4,column=3,padx=2,pady=7,sticky=W)

          #crime
        lbl_crime=Label(up_frame,text='Crime:',font=('arial',11,'bold'),bg='silver')  
        lbl_crime.grid(row=0,column=4,padx=2,pady=7,sticky=W) 

        txt_crime=ttk.Entry(up_frame,textvariable=self.var_crime,width=22,font=('arial',11,'bold')) 
        txt_crime.grid(row=0,column=5,padx=2,pady=7,sticky=W) 

          #fatherName
        lbl_fatherName=Label(up_frame,text='Father`s Name:',font=('arial',11,'bold'),bg='silver')  
        lbl_fatherName.grid(row=1,column=4,padx=2,pady=7,sticky=W) 

        txt_fatherName=ttk.Entry(up_frame,textvariable=self.var_father_name,width=22,font=('arial',11,'bold')) 
        txt_fatherName.grid(row=1,column=5,padx=2,pady=7,sticky=W) 


          #gender
        lbl_gender=Label(up_frame,text='Gender:',font=('arial',11,'bold'),bg='silver')  
        lbl_gender.grid(row=2,column=4,padx=2,pady=7,sticky=W) 

        radio_frame_gender=Frame(up_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_gender.place(x=720,y=80,width=198,height=25)

        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='male',font=('arial',10,'bold'),bg='white')
        male.grid(row=0,column=0,pady=0,padx=0,sticky=W)

        female=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Female',value='female',font=('arial',10,'bold'),bg='white')
        female.grid(row=0,column=2,pady=0,padx=0,sticky=W)

        other=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Other',value='other',font=('arial',10,'bold'),bg='white')
        other.grid(row=0,column=3,pady=0,padx=0,sticky=W)

          #wanted
        lbl_wanted=Label(up_frame,text='Wanted:',font=('arial',11,'bold'),bg='silver')  
        lbl_wanted.grid(row=3,column=4,padx=2,pady=7,sticky=W) 

        radio_frame_wanted=Frame(up_frame,bd=2,relief=RIDGE,bg='white')
        radio_frame_wanted.place(x=720,y=120,width=200,height=25)

        yes=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='Yes',value='yes',font=('arial',10,'bold'),bg='white')
        yes.grid(row=3,column=5,pady=0,padx=0,sticky=W)

        no=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='No',value='no',font=('arial',10,'bold'),bg='white')
        no.grid(row=3,column=6,pady=0,padx=0,sticky=W)


        #button
        button_frame=Frame(up_frame,bd=2,relief=RIDGE,bg='silver')
        button_frame.place(x=5,y=200,width=605,height=45)

        #add button
        btn_add=Button(button_frame,command=self.add_data,text='Save Record',font=('arial',13,'bold'),width=14,bg='blue',fg='orange')
        btn_add.grid(row=0,column=0,padx=0,pady=3)

        btn_update=Button(button_frame,command=self.update_data,text='Update',font=('arial',13,'bold'),width=14,bg='blue',fg='orange')
        btn_update.grid(row=0,column=1,padx=0,pady=3)

        btn_delete=Button(button_frame,command=self.delete_data,text='Delete',font=('arial',13,'bold'),width=14,bg='blue',fg='orange')
        btn_delete.grid(row=0,column=2,padx=0,pady=3)

        btn_clear=Button(button_frame,command=self.clear_data,text='Clear',font=('arial',13,'bold'),width=14,bg='blue',fg='orange')
        btn_clear.grid(row=0,column=3,padx=0,pady=3)
 
        
         
          

          #lower_frame
        low_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Criminal Details Table',font=('times new roman',11,'bold'),bg='silver',fg='green')
        low_frame.place(x=10,y=280,width=1220,height=270) 

          #search_frame
        search_frame=LabelFrame(low_frame,bd=2,relief=RIDGE,text='Search Criminal Record',font=('times new roman',11,'bold'),bg='silver',fg='Red')
        search_frame.place(x=8,y=0,width=1205,height=60)

        search_by=Label(low_frame,text='Search By:',font=('arial',11,'bold'),bg='orange',fg='white')  
        search_by.grid(row=0,column=0,padx=14,pady=25,sticky=W) 
        
        self.var_combo_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_combo_search,font=('arial',10,'bold'),width=20,state="readonly")
        combo_search_box['value']=('Select Option','case_id','criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=0,padx=98,pady=0,sticky=W)
        
        self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,textvariable=self.var_search,width=16,font=('arial',11)) 
        search_txt.grid(row=0,column=1,pady=7,padx=0,sticky=N)

         #search button
        btn_search=Button(search_frame,command=self.search_data,text='Search',font=('arial',10,'bold'),width=14,bg='blue',fg='white')
        btn_search.grid(row=0,column=2,padx=8,pady=3) 

         #all button
        btn_all=Button(search_frame,command=self.fetch_data,text='Show All',font=('arial',10,'bold'),width=14,bg='blue',fg='white')
        btn_all.grid(row=0,column=3,padx=0,pady=3)

        lbl_agency=Label(search_frame,text='Federal Department of Investigation',font=('arial',18,'bold'),bg='silver',fg='crimson')  
        lbl_agency.grid(row=0,column=4,padx=10,pady=0,sticky=W)  

         #table frame
        table_frame=LabelFrame(low_frame,bd=2,relief=RIDGE,bg='gray')
        table_frame.place(x=8,y=60,width=1205,height=185) 

         #scrollbar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL) 
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=('1','2','3','4','5','6','7','8','9','10','11','12','13','14'),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1',text='Case ID')
        self.criminal_table.heading('2',text='Criminal NO')
        self.criminal_table.heading('3',text='Criminal Name')
        self.criminal_table.heading('4',text='Nickname')
        self.criminal_table.heading('5',text='Arrest Date')
        self.criminal_table.heading('6',text='Date of Crime')
        self.criminal_table.heading('7',text='Address')
        self.criminal_table.heading('8',text='Age')
        self.criminal_table.heading('9',text='Occupation')
        self.criminal_table.heading('10',text='Birth Mark')
        self.criminal_table.heading('11',text='Crime')
        self.criminal_table.heading('12',text='Father Name')
        self.criminal_table.heading('13',text='Gender')
        self.criminal_table.heading('14',text='Wanted')

        self.criminal_table['show']='headings'

        self.criminal_table.column('1',width=80)
        self.criminal_table.column('2',width=100)
        self.criminal_table.column('3',width=100)
        self.criminal_table.column('4',width=100)
        self.criminal_table.column('5',width=100)
        self.criminal_table.column('6',width=100)
        self.criminal_table.column('7',width=100)
        self.criminal_table.column('8',width=50)
        self.criminal_table.column('9',width=100)
        self.criminal_table.column('10',width=100)
        self.criminal_table.column('11',width=80)
        self.criminal_table.column('12',width=100)
        self.criminal_table.column('13',width=100)
        self.criminal_table.column('14',width=80)

        self.criminal_table.pack(fill=BOTH,expand=1)

        #binding table data
        self.criminal_table.bind('<ButtonRelease>',self.get_cursor)

        #showing data on table
        self.fetch_data()


     #adding function 
    def add_data(self):
       if self.var_case_id.get()=="":
         messagebox.showerror('Error','All Fields are required',parent=self.root)
       else:
         try:
           connect=mysql.connector.connect(host='localhost',username='dani',password='root',database='management')  
           my_cursor=connect.cursor()
           my_cursor.execute('insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                      self.var_case_id.get(),
                                                                                                      self.var_criminal_no.get(),
                                                                                                      self.var_name.get(),
                                                                                                      self.var_nickname.get(),
                                                                                                      self.var_arrest_date.get(),
                                                                                                      self.var_dateofcrime.get(),
                                                                                                      self.var_address.get(),
                                                                                                      self.var_age.get(),
                                                                                                      self.var_occupation.get(),
                                                                                                      self.var_birthmark.get(),
                                                                                                      self.var_crime.get(),
                                                                                                      self.var_father_name.get(),
                                                                                                      self.var_gender.get(),
                                                                                                      self.var_wanted.get()                                               
                                                                                                      ))

           connect.commit() 
           self.fetch_data()
           self.clear_data()                                                                                          
           connect.close()
           messagebox.showinfo('Success','Criminal Record has been added')
         except Exception as es:
          messagebox.showerror('Error',f'Due To{str(es)}')
    

    #fetching data
    def fetch_data(self):
      connect=mysql.connector.connect(host='localhost',username='dani',password='root',database='management')  
      my_cursor=connect.cursor()
      my_cursor.execute('select*from criminal')
      data=my_cursor.fetchall()
      if len(data)!=0:
        self.criminal_table.delete(*self.criminal_table.get_children())
        for i in data:
          self.criminal_table.insert('',END,values=i)
        connect.commit()
      connect.close() 


    #get cursor
    def get_cursor(self,event=''):
      cursor_row=self.criminal_table.focus()  
      content=self.criminal_table.item(cursor_row)
      data=content['values']

      self.var_case_id.set(data[0])
      self.var_criminal_no.set(data[1])
      self.var_name.set(data[2])
      self.var_nickname.set(data[3])
      self.var_arrest_date.set(data[4])
      self.var_dateofcrime.set(data[5])
      self.var_address.set(data[6])
      self.var_age.set(data[7])
      self.var_occupation.set(data[8])
      self.var_birthmark.set(data[9])
      self.var_crime.set(data[10])
      self.var_father_name.set(data[11])
      self.var_gender.set(data[12])
      self.var_wanted.set(data[13])
    

    #updation

    def update_data(self):
      if self.var_case_id.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
      else:
        try:

           update=messagebox.askyesno('update','Are You Sure To Update This Criminal Record')  
           if update>0:
            connect=mysql.connector.connect(host='localhost',username='dani',password='root',database='management')  
            my_cursor=connect.cursor()
            my_cursor.execute('update criminal set criminal_no=%s,criminal_name=%s,nick_name=%s,arrest_date=%s,dateofcrime=%s,address=%s,age=%s,occupation=%s,birthmark=%s,crime=%s,father_name=%s,gender=%s,wanted=%s where case_id=%s',(
                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                         self.var_criminal_no.get(),
                                                                                                                                                                                                                                         self.var_name.get(),
                                                                                                                                                                                                                                         self.var_nickname.get(),
                                                                                                                                                                                                                                         self.var_arrest_date.get(),
                                                                                                                                                                                                                                         self.var_dateofcrime.get(),
                                                                                                                                                                                                                                         self.var_address.get(),
                                                                                                                                                                                                                                         self.var_age.get(),
                                                                                                                                                                                                                                         self.var_occupation.get(),
                                                                                                                                                                                                                                         self.var_birthmark.get(),
                                                                                                                                                                                                                                         self.var_crime.get(),
                                                                                                                                                                                                                                         self.var_father_name.get(),
                                                                                                                                                                                                                                         self.var_gender.get(),
                                                                                                                                                                                                                                         self.var_wanted.get(), 
                                                                                                                                                                                                                                         self.var_case_id.get(),


                                                                                                                                                                                                                                       ))
           else:
              if not update:
                return
           connect.commit()
           self.fetch_data() 
           self.clear_data()                                                                                                                                                                                                                                  
           connect.close()
           messagebox.showinfo('Success','Criminal Record has been successfully updated')
        except Exception as es:
          messagebox.showerror('Error',f'Due to{str(es)}')

    #deletion
    def delete_data(self):
      if self.var_case_id.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
      else:
        try:
          delete=messagebox.askyesno('update','Are You Sure To Delete This Criminal Record')  
          if delete>0:
            connect=mysql.connector.connect(host='localhost',username='dani',password='root',database='management')  
            my_cursor=connect.cursor()
            sql='delete from criminal where case_id=%s'
            value=(self.var_case_id.get(),)
            my_cursor.execute(sql,value)
          else:
            if not delete:
              return  
          connect.commit()    
          self.fetch_data()
          self.clear_data()
          connect.close()
          messagebox.showinfo('Success','Criminal Record has been successfully Deleted')
        except Exception as es:
          messagebox.showerror('Error',f'Due to{str(es)}')

    #clearing
    def clear_data(self):
      self.var_case_id.set('')
      self.var_criminal_no.set('')
      self.var_name.set('')
      self.var_nickname.set('')
      self.var_arrest_date.set('')
      self.var_dateofcrime.set('')
      self.var_address.set('')
      self.var_age.set('')
      self.var_occupation.set('')
      self.var_birthmark.set('')
      self.var_crime.set('')
      self.var_father_name.set('')
      self.var_gender.set('')
      self.var_wanted.set('')

    #search
    def search_data(self):
      if self.var_combo_search.get()=='':
        messagebox.showerror('Error','All fields are required')
      else:
        try:
          connect=mysql.connector.connect(host='localhost',username='dani',password='root',database='management')  
          my_cursor=connect.cursor()
          my_cursor.execute(' select * from criminal where ' +str(self.var_combo_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
          rows=my_cursor.fetchall()
          if len(rows)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in rows:
              self.criminal_table.insert('',END,values=i)
          connect.commit()
          connect.close() 
        except Exception as es:
          messagebox.showerror('Error',f'Due to{str(es)}')


if __name__ == "__main__":
    main()