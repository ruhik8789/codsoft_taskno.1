from tkinter import *
from tkinter import messagebox

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('ToDo List')
        self.root.geometry('650x410+300+150')
        
        self.label = Label(self.root, text='ToDo List',
                           font='Arial, 25 bold', width=10, bd=5, bg='green', fg='black')
        self.label.pack(side='top', fill=BOTH)
        
        self.label2 = Label(self.root, text='Add Tasks',
                            font='Arial, 18 bold', width=10, bd=5, bg='green', fg='black')
        self.label2.place(x=40,y=54)
        
        self.label3 = Label(self.root, text='Tasks',
                            font='Arial, 18 bold', width=10, bd=5, bg='green', fg='black')
        self.label3.place(x=320, y=54)
        
        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font="Arial, 20 italic bold")
        self.main_text.place(x=250, y=100)
        
        self.text = Text(self.root, bd=5, height=2, width=30, font='Arial, 10 bold')
        self.text.place(x=20, y=100)
        
        self.button = Button(self.root, text="Add", font='Arial, 20 bold italic',
                             width=10,bd=5,bg='green',fg='black',command=self.add)
        self.button.place(x=30, y=150)
        
        self.button = Button(self.root, text="Delete", font='Arial, 20 bold italic',
                             width=10,bd=5,bg='green',fg='black',command=self.delete)
        self.button.place(x=30, y=220)
    
    def add(self):
        content = self.text.get(1.0, END)
        self.main_text.insert(END, content)
        with open('data.txt', 'a') as file:
            file.write(content)
            file.seek(0)
            file.close()
        self.text.delete(1.0, END)
    
    def delete(self):
        delete_indices = self.main_text.curselection()
        
        if delete_indices:
            for index in reversed(delete_indices):
                self.main_text.delete(index)
            
            with open('data.txt', 'r') as file:
                lines = file.readlines()
                
            with open('data.txt', 'w') as file:
                for i, line in enumerate(lines):
                    if i not in delete_indices:
                        file.write(line)
        
        else:
            
            messagebox.showinfo("No Selection", "Please select a task to delete.")

def main():
    root = Tk()
    ul = todo(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()        