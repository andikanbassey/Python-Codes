import sqlite3
import Tkinter
window=Tkinter.Tk()
con=sqlite3.connect('login.db')
cur=con.cursor()
# cur.execute('CREATE TABLE LoginDetails (Name TEXT , Username TEXT , Password TEXT, Account FLOAT)')
# cur.execute("INSERT INTO LoginDetails VALUES('Andikan Bassey ' , 'Lambo' , 'andikan', 20000)")

def search(username, password):
    query= "SELECT name, password FROM LoginDetails WHERE UserName = '"+username+ "' AND Password = '"+password+ "'"
    cur.execute(query)
    ans = cur.fetchall()
    print(ans)

def login():
    window = Tkinter.Tk()
    labe1=Tkinter.Label(window, text='Welcome')
    labe1.pack()

    window.mainloop()

#models
username = Tkinter.StringVar()
password = Tkinter.StringVar()

label1=Tkinter.Label(window, text='Username')
label1.pack()
entry1=Tkinter.Entry(window, textvariable = username)
entry1.pack()
label2=Tkinter.Label(window, text='Password')
label2.pack()
entry2=Tkinter.Entry(window, textvariable = password)
entry2.pack()
button=Tkinter.Button(window,text='Login' , command =login)
button.pack()

window.mainloop()
