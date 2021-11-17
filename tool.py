from tkinter import *
import os
from tkinter import messagebox
import re



def clear():
        entry_fname.delete(0,END)
        entry_mname.delete(0,END)
        entry_sname.delete(0,END)
        entry_contact.delete(0,END)
        entry_email.delete(0,END)
        entry_age.delete(0,END)
        entry_cgpa.delete(0,END)
        entry_mis.delete(0,END)
        entry_branch.delete(0,END)
        entry_name.delete(0,END)
        entry_backlog.delete(0,END)
        entry_branch.delete(0,END)
        entry_address.delete(0,END)
        tfws.set(0)
        vaccinated.set(0)
        country.set('Select your Country')
        year.set('Year of Studying')
        gender.set(0)

    

def get_seqNo(fileName):
    f = open(fileName,'r')
    data = f.read()
    data_list = data.split('\n')
    #print(data_list)
    seq_no  = len(data_list)
    return seq_no


#Callback functions

def checkfname(fname):
    if fname.isalnum():
        return True
    if fname == "":
            return True
    else:
        messagebox.showwarning("Invalid","Not allowed "+ fname[-1])
        return False

def checkmname(mname):
    if mname.isalnum():
        return True
    if mname == "":
            return True
    else:
        messagebox.showwarning("Invalid","Not allowed "+ mname[-1])
        return False

def checksname(sname):
    if sname.isalnum():
        return True
    if sname == "":
            return True
    else:
        messagebox.showwarning("Invalid","Not allowed "+ sname[-1])
        return False


def checkcontact(con):
        if con.isdigit():
            return True
        if len(str(con))== 0:
            return True
        
        
        else:
            messagebox.showwarning("Invalid","Invalid Entry")
            return False
        
def checkmis(mis):
        if mis.isdigit():
            return True
        if len(str(mis))== 0:
            return True

        else:
            messagebox.showwarning("Invalid","Invalid Entry")
            return False        
        
def checkemail(email):
        if len(email)>7:
                if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
                    return True
                    
                
                else:
                    messagebox.showwarning("Alert","Invalid E-mail enter by user")
                    return False
        else:
            messagebox.showwarning("Alert","Email length is too small")

def checkcgpa(cgpa):
    if (cgpa.isdigit() and 4 <= int(cgpa) <= 10):
        return True
    if len(str(cgpa))== 0:
        return True        
    else:
        messagebox.showwarning("Invalid","Invalid Entry")
        return False


def checkbranch(branch):
    if branch.isalnum():
        return True
    if branch == "":
            return True
    else:
        messagebox.showwarning("Invalid","Not allowed "+ branch[-1])
        return False

def checkbacklog(backlog):
    if backlog.isalnum():
        return True
    if backlog == "":
            return True
    else:
        messagebox.showwarning("Invalid","Not allowed "+ backlog[-1])
        return False

def checkaddress(address):
    if address.isalnum():
        return True
    if address == "":
            return True
    else:
        messagebox.showwarning("Invalid","Not allowed "+ address[-1])
        return False








 #validate all field at submit time
def validations():
    x =y = 0
    if fname.get() == "":
        messagebox.showinfo("Alert","Enter your name first")
    elif mname.get() == "":
        messagebox.showinfo("Alert","Enter your middle name")
    elif sname.get() == "":
        messagebox.showinfo("Alert","Enter your surname")
    elif contact.get() == "" or len(contact.get())!=10:
        messagebox.showinfo("Alert","Enter valid Contact ")
    elif email.get() =="":
        messagebox.showinfo("Alert","Enter Email")
    elif age.get() == "": 
        messagebox.showinfo("Alert","Enter Age")
    elif gender.get() ==0:
        messagebox.showinfo("Alert","Select Gender")
    elif country.get() == "" or country.get() == "Select your country":
        messagebox.showinfo("Alert","Select country")
    elif cgpa.get() == "":
        messagebox.showinfo("Alert","Enter your  CGPA")
    elif mis.get() == "":
        messagebox.showinfo("Alert","Enter your  MIS")
    elif year.get() == "":
        messagebox.showinfo("Alert","Enter year of studying")
    elif address.get() == "":
        messagebox.showinfo("Alert","Enter your permanant addresss")
    elif tfws.get() == "":
        messagebox.showinfo("Alert","Please Select whether you belong to TFWS or NOT")
    elif branch.get() == "":
        messagebox.showinfo("Alert","Please enter your branch")
    elif vaccinated.get() == "":
        messagebox.showinfo("Alert","Please Select whether you are vaccinated or not .")
    elif backlog.get() == "":
        messagebox.showinfo("Alert","Please enter no of backlog you currently have.")
    elif name.get() == "":
        messagebox.showinfo("Alert","Please enter local Guardian name.")
    elif email.get()!=None :
        x = checkemail(email.get())
    if (x == True):
        fname1=fname.get()
        mname1=mname.get()
        sname1=sname.get()
        mis1 = mis.get()
        cont1=contact.get()
        email1=email.get()
        age1=age.get()
        gvar=gender.get()
        cgpa1 = cgpa.get()
        year1 = year.get()
        address1 = address.get()
        tfws1 = tfws.get()
        branch1 = branch.get()
        vaccinated1 = vaccinated.get()
        backlog1 = backlog.get()
        name1 = name.get()
        cnt = country.get()
        seqNo = 1
        if(os.path.isfile('students.txt')):
            seqNo = get_seqNo('students.txt')
        f = open('students.txt','a')
        details = f"Student {seqNo} : first_name = {fname1}, middle_name =  {mname1}, surname = {sname1}, mis = {mis1}, cgpa = {cgpa1}, branch = {branch1}, year = {year1}, address = {address1}, contact_no = {cont1}, email = {email1}, age =  {age1}, backlog = {backlog1}, Guardian-name = {name1},  vaccinated = {vaccinated1}, tfws = {tfws1}, gender = {gvar}, country = {cnt}\n"
        f.write(details)
        f.close()
        
        

               
def view():
        lx = [fname.get(),"\n",mname.get(),"\n",sname.get(),"\n",contact.get(),"\n",email.get(),"\n",
              age.get(),"\n",gender.get(),"\n",cgpa.get(),"\n",country.get(),"\n",name.get(),"\n",mis.get(),"\n",year.get(),"\n",vaccinated.get(),"\n",address.get(),"\n",branch.get(),"\n",vaccinated.get(),"\n",tfws.get(),"\n"]
        messagebox.showinfo("Details",lx)
                                        
#GUI
   
win = Tk()
win.geometry("1200x650")
win.title("Registration Form")                        
win["bg"] = "sky blue"                     
        
        
#creating data selection variable on gui
fname  = StringVar()
mname  = StringVar()
sname  = StringVar()
name = StringVar()
contact =StringVar()
email = StringVar()
age = StringVar()
gender = IntVar()
mis = StringVar()
year = StringVar()
cgpa = StringVar()
branch = StringVar()
tfws = IntVar() 
country = StringVar()
backlog = StringVar()
vaccinated = IntVar()
address = StringVar()

#Form Title
label_title = Label(win,text ="Hostel Admission Form",width = 60,font = ("bold",20)).place(x=70,y=53)


#Create fields
label_fname = Label(win,text = "First Name",width = 20).place(x = 70,y = 130)
entry_fname = Entry(win,width = 25,textvariable = fname)
entry_fname.place(x = 270,y = 130)
validate_fname = win.register(checkfname)  #validation register
entry_fname.config(validate = "key",validatecommand = (validate_fname,"%P")) #validation configure



label_mname = Label(win,text = "Middle Name",width = 20).place(x = 70,y = 180)
entry_mname = Entry(win,width = 25,textvariable = mname)
entry_mname.place(x = 270,y = 180)
validate_mname = win.register(checkmname)  #validation register
entry_mname.config(validate = "key",validatecommand = (validate_fname,"%P")) #validation configure

label_sname = Label(win,text = "Surname",width = 20).place(x = 70,y = 230)
entry_sname = Entry(win,width = 25,textvariable = sname)
entry_sname.place(x = 270,y = 230)
validate_sname = win.register(checksname)  #validation register
entry_sname.config(validate = "key",validatecommand = (validate_fname,"%P")) #validation configure



label_mis = Label(win,text = "mis",width = 20).place(x = 70,y = 280)
entry_mis = Entry(win,width = 25,textvariable = mis)
entry_mis.place(x = 270,y = 280)
validate_mis = win.register(checkmis)  #validation register
entry_mis.config(validate = "key",validatecommand = (validate_mis,"%P")) 




label_contact = Label(win,text ="Contact",width = 20).place(x = 70,y = 330)
entry_contact = Entry(win,textvariable = contact,width = 25)
entry_contact.place(x = 270,y = 330)
validate_contact= win.register(checkcontact)  #validation register
entry_contact.config(validate = "key",validatecommand = (validate_contact,"%P"))

label_email = Label(win,text ="Email Id",width = 20).place(x = 70,y = 380)
entry_email = Entry(win,textvariable = email,width = 25)
entry_email.place(x = 270,y = 380)

label_age = Label(win,text = "Your Age",width = 20).place(x = 70,y = 430)
entry_age = Spinbox(win,textvariable = age,from_ = 1,to_ = 150 ,width = 24)
entry_age.place(x = 270,y = 430)

label_gender = Label(win,text = "Gender",width = 20).place(x = 70,y = 480)
g_radio_male = Radiobutton(win, text="Male",padx = 10, variable=gender ,value= 1).place(x=270,y=480)
g_radio_female =  Radiobutton(win, text="Female",padx = 10, variable=gender, value= 2 ).place(x=380,y=480)

label_cgpa = Label(win, text = "CGPA", width = 20).place(x = 70, y = 530)
entry_cgpa = Entry(win, textvariable = cgpa, width = 25)
entry_cgpa.place(x = 270, y = 530)

label_country = Label(win,text = "Your Country",width = 20).place(x = 70,y = 580)
list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];
droplist=OptionMenu(win,country, *list1)
droplist.config(width=20)
country.set('Select your country') 
droplist.place(x=270,y=580)


# second column

label_branch = Label(win,text = "Branch",width = 20).place(x = 680,y = 130)
entry_branch = Entry(win,width = 25,textvariable = branch)
entry_branch.place(x = 890,y = 130)
validate_branch = win.register(checkbranch)  #validation register
entry_branch.config(validate = "key",validatecommand = (validate_branch,"%P")) #validation configure


label_Year = Label(win,text = "Current-Year",width = 20).place(x = 680,y = 180)
list1 = ['First-Year','Second-Year','Third-Year','Fourth-Year'];
droplist=OptionMenu(win,year, *list1)
droplist.config(width=20)
year.set('Year of Studying')
droplist.place(x=890,y=180)

label_backlog = Label(win,text = "Total-Backlog",width = 20).place(x = 680,y = 230)
entry_backlog = Entry(win,width = 25,textvariable = backlog)
entry_backlog.place(x = 890,y = 230)
validate_backlog = win.register(checkbacklog)  #validation register
entry_backlog.config(validate = "key",validatecommand = (validate_backlog,"%P"))


label_address = Label(win,text = "Permanent Address",width = 20).place(x = 680,y = 280)
entry_address = Entry(win,width = 25,textvariable = address)
entry_address.place(x = 890,y = 280)
validate_address = win.register(checkaddress)  #validation register
entry_address.config(validate = "key",validatecommand = (validate_address,"%P"))

label_name = Label(win,text = "Local Guardian Name",width = 20).place(x = 680,y = 330)
entry_name = Entry(win,width = 25,textvariable = name)
entry_name.place(x = 890,y = 330)
validate_name = win.register(checkfname)  #validation register
entry_name.config(validate = "key",validatecommand = (validate_name,"%P")) #validation configure


label_vacinated = Label(win,text = "Are you vaccinated?",width = 20).place(x = 680,y = 380)
g_radio_male = Radiobutton(win, text="Yes",padx = 25, variable=vaccinated ,value= 1).place(x=900,y=380)
g_radio_female =  Radiobutton(win, text="No",padx = 25, variable=vaccinated, value= 2 ).place(x=1000,y=380)



label_vacinated = Label(win,text = "TFWS category ?",width = 20).place(x = 680,y = 430)
g_radio_male = Radiobutton(win, text="Yes",padx = 25, variable=tfws ,value= 1).place(x=900,y=430)
g_radio_female =  Radiobutton(win, text="No",padx = 25, variable=tfws, value= 2 ).place(x=1000,y=430)




Button(win, text='Submit',width=50,bg='blue',fg='white',command  = validations).place(x=680,y=480)
Button(win, text='Clear Data',width=50,bg='blue',fg='white',command = clear).place(x=680,y=530)
Button(win, text='Check',width=50,bg='blue',fg='white',command = view).place(x=680,y=580)

win.mainloop()     
            
            
            
        
        

        
        
        
        

        
        
        
        
        

        
    
