from tkinter import *
from tkinter import messagebox
import sqlite3
con=sqlite3.connect('library.db')
cur=con.cursor()

class Book(Toplevel):
    try:
        def __init__(self):
            Toplevel.__init__(self)
            self.geometry("650x750+550+200")
            #self.geometry("1920×1200+150+100")
            self.title("Add Book")
            self.resizable(False,False)

            #Frames
            #Top Frame
            self.topFrame=Frame(self,height=150,bg='white')
            self.topFrame.pack(fill=X)

            #Bottom Frame
            self.bottomFrame=Frame(self,height=600,bg='#fcc324')
            self.bottomFrame.pack(fill=X)

            #heading
            heading=Label(self.topFrame,text=' Add Book ', font='arial 22 bold',fg='#003f8a',bg='white')
            heading.place(x=290,y=60)

            #Entries and label
            #Title
            self.lbl_Title=Label(self.bottomFrame,text='Title',font='arial 15 bold',fg='white',bg='#fcc324')
            self.lbl_Title.place(x=40,y=40)
            self.ent_Title=Entry(self.bottomFrame,width=30,bd=4)
            self.ent_Title.insert(0,'please enter a book Title')
            self.ent_Title.place(x=150,y=45)

            # Author
            self.lbl_Author = Label(self.bottomFrame, text='Author', font='arial 15 bold', fg='white', bg='#fcc324')
            self.lbl_Author.place(x=40, y=80)
            self.ent_Author = Entry(self.bottomFrame, width=30, bd=4)
            self.ent_Author.insert(0, 'please enter a Author name')
            self.ent_Author.place(x=150, y=85)

            # ISBN(International Standard Book Number)
            self.lbl_ISBN = Label(self.bottomFrame, text='ISBN', font='arial 15 bold', fg='white', bg='#fcc324')
            self.lbl_ISBN.place(x=40, y=120)
            self.ent_ISBN = Entry(self.bottomFrame, width=30, bd=4)
            self.ent_ISBN.insert(0, 'please enter ISBN number')
            self.ent_ISBN.place(x=150, y=125)


            #Button
            button=Button(self.bottomFrame,text='Add Book',command=self.addBook)
            button.place(x=270,y=200)


        def addBook(self):
            Title = self.ent_Title.get()
            Author = self.ent_Author.get()
            ISBN = self.ent_ISBN.get()

            if (Title and Author and ISBN !=""):
                try:
                    query="INSERT INTO 'books' (Book_Title,Book_Author,Book_ISBN) VALUES(?,?,?)"
                    cur.execute(query,(Title,Author,ISBN))
                    con.commit()
                    messagebox.showinfo("Success","Successfully added to database",icon='info')
                except:
                    messagebox.showinfo("Error", "Cant add book to the database", icon='warning')
            else:
                messagebox.showinfo("Error", "Field cant be empty", icon='warning')
    except:
        messagebox.showinfo("Erroe","Something went wrong")

class Ebook(Book):
    try:
        def addBook(self):
           pass

    except:
        messagebox.showinfo("Error","Something went wrong")