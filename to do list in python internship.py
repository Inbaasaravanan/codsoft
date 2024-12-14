#importing tkinter library form python
import tkinter as tk
from tkinter import  messagebox

#function defined for the adding opeartions on a list
def adding_task():
    task = task_enter.get()
   
   #checking condition if it is false then it will display the output as error occured
    if task !="":
        task_listbox.insert(tk.END,task)
        task_enter.delete(0,tk.END)
    
    
    else:
        messagebox.showwarning("Error occuring in the input section","please enter the valid task")

#function defined for removing the task form the list app created
def removing_task():
    
    try:
         selected_task_index = task_listbox.curselection()
         task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("selecting error has occured please enter a valid task to remove the component form the list application")
#mainchannel variable for the todo list app
mainchannel = tk.Tk()

#display the title of the app as To--Do--List App
mainchannel.title("TO--DO--LIST APP")


task_enter = tk.Entry(mainchannel, width = 75)
task_enter.pack(pady = 50)

#adding button color grading and box creating
adding_button = tk.Button(mainchannel, text="Add task to the list",width = 40,bg='red',command = adding_task)
adding_button.pack(pady = 10)

#removing button color grading and box creating
removing_button =tk.Button(mainchannel,text ="Removing task from the list",bg='orange',width= 30,command= removing_task)
removing_button.pack(pady= 15)

#changing the background colour
mainchannel.configure(bg="light blue")

task_listbox = tk.Listbox(mainchannel, height = 14, width = 64,selectmode= tk.SINGLE)
task_listbox.pack(pady= 50)

mainchannel.mainloop()



         
                            
