from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import Book

con=sqlite3.connect('library.db')
cur=con.cursor()
class Library(object):
    try:
        def __init__(self,master):
            self.master = master

            def displayBooks(self):
                books = cur.execute("SELECT * FROM books").fetchall()
                count = 0
                for book in books:
                    print(book)
                    self.list_books.insert(count, str(book[0])+ "-" +book[1])
                    count +=1

                def bookInfo(evt):
                    value=str(self.list_books.get(self.list_books.curselection()))
                    Id=value.split('-')[0]
                    book = cur.execute("SELECT * FROM books WHERE Book_Id=?",(Id,))
                    book_info=book.fetchall()
                    print(book_info)
                    self.list_details.delete(0,'end')
                    self.list_details.insert(0," Title:"+book_info[0][1])
                    self.list_details.insert(1, "Author:" + book_info[0][2])
                    self.list_details.insert(2, "ISBN:" + book_info[0][3])
                    if book_info[0][4] == 0:
                        self.list_details.insert(3,"Status:Avaiable")
                    else:
                        self.list_details.insert(3, "Status: Not Avaiable")

                self.list_books.bind('<<ListboxSelect>>',bookInfo)

            #frames
            mainFrame = Frame(self.master)
            mainFrame.pack()
            #Top Frame
            topFrame= Frame(mainFrame, width=1350,height=70,bg='#f8f8f8',padx=20,relief=SUNKEN, borderwidth=2)
            topFrame.pack(side=TOP,fill=X)
            #center frame
            centerFrame = Frame(mainFrame,width=1350,relief=RIDGE,bg='#e0f0f0',height=680)
            centerFrame.pack(side=TOP)
            #center left frame
            centerLeftFrame= Frame(centerFrame,width=900,height=700,bg='#e0f0f0',borderwidth=2,relief='sunken')
            centerLeftFrame.pack(side=LEFT)
            #center right frame
            centerRightFrame=Frame(centerFrame,width=450,height=700,bg='#e0f0f0',borderwidth=2,relief='sunken')
            centerRightFrame.pack()

            #search bar
            search_bar=LabelFrame(centerRightFrame,width=440,height=75,text='Search Box',bg='#9bc9ff')
            search_bar.pack(fill=BOTH)
            self.lbl_search=Label(search_bar,text='Search :',font='arial 12 bold', bg='#9bc9ff',fg='white')
            self.lbl_search.grid(row=0,column=0,padx=20,pady=10)
            self.ent_search=Entry(search_bar,width=30,bd=10)
            self.ent_search.grid(row=0,column=1,columnspan=3,padx=10,pady=10)
            self.btn_search=Button(search_bar,text='Search',font='arial 12',bg='#fcc324',fg='white',command=self.searchBooks)
            self.btn_search.grid(row=0,column=4,padx=20,pady=10)

            #list bar
            list_bar =LabelFrame(centerRightFrame, width=440,height=175,text='List Box',bg='#fcc324')
            list_bar.pack(fill=BOTH)
            lbl_list=Label(list_bar,text='Sort By',font='time 16 bold',fg='#2488ff',bg='#fcc324')
            lbl_list.grid(row=0,column=2)
            self.listChoice=IntVar()
            rb1 = Radiobutton(list_bar, text='All Books',var=self.listChoice,value=1,bg='#fcc324')
            rb2 = Radiobutton(list_bar, text='In Library', var=self.listChoice, value=2, bg='#fcc324')
            rb3 = Radiobutton(list_bar, text='Borrowed Books', var=self.listChoice, value=3, bg='#fcc324')
            rb1.grid(row=1,column=0)
            rb2.grid(row=1, column=1)
            rb3.grid(row=1, column=2)
            btn_list= Button(list_bar,text='List Books',bg='#2488ff',fg='white',font='arial 12',command=self.listBooks)
            btn_list.grid(row=1,column=3,padx=40,pady=10)

            #Tool Bar
            #Add book
            #self.iconbook = PhotoImage(file='icons/add_book.png')
            self.btnbook = Button(topFrame, text='Add Book', compound=LEFT, font='arial 12 bold',command=self.addBook)
            self.btnbook.pack(side=LEFT, padx=10)

            #Tabs
            self.tabs=ttk.Notebook(centerLeftFrame,width=900,height=600)
            self.tabs.pack()
            self.tab1=ttk.Frame(self.tabs)
            self.tab2=ttk.Frame(self.tabs)
            self.tabs.add(self.tab1,text='Library Books')

            #list books
            self.list_books=Listbox(self.tab1,width=40,height=30,bd=5,font='time 12 bold')
            self.sb=Scrollbar(self.tab1,orient=VERTICAL)
            self.list_books.grid(row=0,column=0,padx=(10,0),pady=10,sticky=N)
            self.sb.config(command=self.list_books.yview)
            self.list_books.config(yscrollcommand=self.sb.set)
            self.sb.grid(row=0,column=0,sticky=N+S+E)

            #list details
            self.list_details=Listbox(self.tab1,width=80,height=30,bd=5,font='time 12 bold')
            self.list_details.grid(row=0,column=1,padx=(10,0),pady=10,sticky=N)

            #functions
            displayBooks(self)

        def addBook(self):
            add=Book.Book()

        def searchBooks(self):
            value = self.ent_search.get()
            search = cur.execute("SELECT * FROM books WHERE Book_Title LIKE ?",('%'+value+'%',)).fetchall()
            print(search)
            self.list_books.delete(0,END)
            count=0
            for book in search:
                self.list_books.insert(count,str(book[0])+ "-"+book[1])
                count +=1

        def listBooks(self):
            value=self.listChoice.get()
            if value ==1:
                allbooks=cur.execute("SELECT * FROM books").fetchall()
                self.list_books.delete(0,END)

                count=0
                for book in allbooks:
                    self.list_books.insert(count,str(book[0]) + "-"+book[1])
                    count +=1

            elif value ==2:
                books_in_library = cur.execute("SELECT * FROM books WHERE Book_Status=?",(0,)).fetchall()
                self.list_books.delete(0, END)

                count = 0
                for book in books_in_library:
                    self.list_books.insert(count, str(book[0]) + "-" + book[1])
                    count += 1

            else:
                taken_books=cur.execute("SELECT * FROM books WHERE Book_Status=?",(1,)).fetchall()
                self.list_books.delete(0, END)

                count = 0
                for book in taken_books:
                    self.list_books.insert(count, str(book[0]) + "-" + book[1])
                    count += 1

    except:
         messagebox.showinfo("Error", "Something went wrong")

def main():
    root = Tk()
    app = Library(root)
    root.title("Library System")
    root.geometry("1400x1200+150+100")
    #root.iconbitmap('icons/icon.png')
    root.mainloop()

if __name__ == '__main__':
    main()
