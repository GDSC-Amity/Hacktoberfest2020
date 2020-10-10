from tkinter import *
import sqlite3
from tkinter import messagebox
wind= Tk()
wind.title('ADDRESS BOOK')
#wind.geometry("400x600")
# connect to a database
con= sqlite3.connect('address_book.db')
# cursor creator
c = con.cursor()

# Submit function
def submit():
    con= sqlite3.connect('address_book.db')
    c = con.cursor()
    arr= [f_name.get(),l_name.get(),add.get(),city.get(),state.get(),zipc.get()]
    if '' in arr:
        messagebox.showerror('ERROR!!!', '1 or more fields were detected as EMPTY')
    else:
        c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :add, :city,:state, :zipc)",
                 {'f_name' : arr[0],
                  'l_name' : arr[1],
                  'add' : arr[2],
                  'city' : arr[3],
                  'state' : arr[4],
                  'zipc' : arr[5]
                  })
        con.commit()
        con.close()
        messagebox.showinfo('info', 'The record has been added to the database')
    # Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    add.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipc.delete(0, END)

# Delete Function
def delboxg():
    d.grid_forget()
    dellabel= Label(wind, text= 'Enter ID No. : ')
    dellabel.grid(row= 8, column =0)
    frt = Frame(wind)
    frt.grid(row =8, column=1)
    delbox = Entry(frt, width= 25)
    delbox.grid(row = 0, column=0)
    delbu= Button(frt, text = 'delete', command= lambda:delete(delbox.get()))
    delbu.grid(row= 0, column =1)
def delete(e):
    global d
    d= Button(wind, text= 'Delete record', command= delboxg)
    d.grid(row= 8, column= 0, columnspan =2, pady =10, padx= 10, ipadx= 137)
    ID= e
    con = sqlite3.connect('address_book.db')
    c = con.cursor()
    # Delete record
    c.execute(f"SELECT * FROM addresses WHERE oid= {ID}")
    if len( c.fetchall())==0:
        messagebox.showerror('ERROR!!!','ERR ID NOT FOUND')
    else:
        messagebox.showinfo('info','Record Deleted')
    c.execute(f"DELETE FROM addresses WHERE oid= {ID}")

    con.commit()
    con.close()

# update function
def updboxg():
    u.grid_forget()
    ulabel= Label(wind, text= 'Enter ID No. : ')
    ulabel.grid(row= 9, column =0)
    frt = Frame(wind)
    frt.grid(row =9, column=1)
    ubox = Entry(frt, width= 25)
    ubox.grid(row = 0, column=0)
    ubut= Button(frt, text = 'update', command= lambda:update(ubox.get()))
    ubut.grid(row= 0, column =1)
def update(e):
    ID = e
    global u
    u= Button(wind, text= 'Update record', command= updboxg)
    u.grid(row= 9, column= 0, columnspan =2, pady =10, padx= 10, ipadx= 137)

    # SQL connection
    con = sqlite3.connect('address_book.db')
    c = con.cursor()
    # Update record
    c.execute(f"SELECT * FROM addresses WHERE oid= {ID}")
    ents= c.fetchall()
    if len(ents)!=0:
        ents= ents[0]
    else:
        con.commit()
        con.close()
        err= messagebox.showerror('ERROR!!!','ERR: ID NOT FOUND')
        return
    global edwin
    edwin= Tk()
    edwin.title('Update Record: ')
    global f_name_e,l_name_e, add_e, city_e, state_e, zipc_e
    f_name_e= Entry(edwin, width= 30)
    f_name_e.grid(row= 0 , column= 1, padx= 20,pady=(10,0))
    l_name_e= Entry(edwin, width= 30)
    l_name_e.grid(row= 1 , column=1)
    add_e= Entry(edwin, width= 30)
    add_e.grid(row= 2 , column= 1)
    city_e= Entry(edwin, width= 30)
    city_e.grid(row= 3 , column= 1)
    state_e= Entry(edwin, width= 30)
    state_e.grid(row= 4 , column= 1)
    zipc_e= Entry(edwin, width= 30)
    zipc_e.grid(row= 5 , column= 1)
    f_name_e.insert(0, ents[0])
    l_name_e.insert(0, ents[1])
    add_e.insert(0, ents[2])
    city_e.insert(0, ents[3])
    state_e.insert(0, ents[4])
    zipc_e.insert(0, ents[5])
    # Text Labels:
    fnl_e= Label(edwin, text = 'First Name')
    fnl_e.grid(row= 0 , column= 0, padx=20, pady=(10,0))
    lnl_e= Label(edwin, text = 'Last Name')
    lnl_e.grid(row= 1 , column= 0)
    ad_e= Label(edwin, text = 'Address')
    ad_e.grid(row= 2 , column= 0)
    ct_e= Label(edwin, text = 'City')
    ct_e.grid(row= 3 , column= 0)
    st_e= Label(edwin, text = 'State')
    st_e.grid(row= 4 , column= 0)
    zi_e= Label(edwin, text = 'Zipcode')
    zi_e.grid(row= 5 , column= 0)
    # Create Submit Button:
    editb= Button(edwin, text= "Save edits to Database", command= lambda: edit(ID))
    editb.grid(row= 6, column = 0, columnspan =2, pady= 10, padx= 10, ipadx=100)

    con.commit()
    con.close()
def edit(ID):
    con= sqlite3.connect('address_book.db')
    c = con.cursor()
    # query db
    c.execute(f"""UPDATE addresses SET
        first_name= :first,
        last_name= :sec,
        address= :ad,
        city= :ci ,
        state= :st,
        zipcode= :pin
        WHERE oid={ID}""",
              {'first': f_name_e.get(),
               'sec': l_name_e.get(),
               'ad': add_e.get(),
               'ci': city_e.get(),
               'st': state_e.get(),
               'pin': zipc_e.get()})
    f_name_e.delete(0, END)
    l_name_e.delete(0, END)
    add_e.delete(0, END)
    city_e.delete(0, END)
    state_e.delete(0, END)
    zipc_e.delete(0, END)

    con.commit()
    con.close()
    global edwin
    edwin.destroy()
    messagebox.showinfo('info',f'Record with Id-{ID} has been edited.')
# query hide
def qhide():
    global fr
    fr.grid_forget()
    q= Button(wind, text= 'Show records', command= query)
    q.grid(row= 7, column= 0, columnspan =2, pady =10, padx= 10, ipadx= 137)

# query function
def query():
    con= sqlite3.connect('address_book.db')
    c = con.cursor()
    # query db
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    global fr
    fr.grid_forget()
    fr = Frame(wind)
    fr.grid(row= 10, column=0, columnspan =2)
    ls=[]
    for i in range(len(records)):
        p= {"PID": records[i][6],
            "First Name": records[i][0],
            "Second Name": records[i][1],
            "Address": records[i][2],
            "City": records[i][3],
            "State": records[i][4],
            "Zipcode": records[i][5]}
        q=''
        for j in p:
            q+=j+':'+str(p[j])+'\n'
        ls.append(q)
    ls= '\n\n'.join(ls) if len(ls)!=0 else '[Nothing to show]'
    l= Label(fr, text=ls).grid(row=0, column=0)
    con.commit()
    con.close()
    q= Button(wind, text= 'Hide records', command= qhide)
    q.grid(row= 7, column= 0, columnspan =2, pady =10, padx= 10, ipadx= 137)


# create table
'''
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")
'''
# Text Boxes
f_name= Entry(wind, width= 30)
f_name.grid(row= 0 , column= 1, padx= 20,pady=(15,0))

l_name= Entry(wind, width= 30)
l_name.grid(row= 1 , column=1)

add= Entry(wind, width= 30)
add.grid(row= 2 , column= 1)

city= Entry(wind, width= 30)
city.grid(row= 3 , column= 1)

state= Entry(wind, width= 30)
state.grid(row= 4 , column= 1)

zipc= Entry(wind, width= 30)
zipc.grid(row= 5 , column= 1)

# Text Labels:
fnl= Label(wind, text = 'First Name')
fnl.grid(row= 0 , column= 0, padx=20, pady=(15,0))

lnl= Label(wind, text = 'Last Name')
lnl.grid(row= 1 , column= 0)

ad= Label(wind, text = 'Address')
ad.grid(row= 2 , column= 0)

ct= Label(wind, text = 'City')
ct.grid(row= 3 , column= 0)

st= Label(wind, text = 'State')
st.grid(row= 4 , column= 0)

zi= Label(wind, text = 'Zipcode')
zi.grid(row= 5 , column= 0)

# Create Submit Button:
sub= Button(wind, text= "Add Record to Database", command= submit)
sub.grid(row= 6, column = 0, columnspan =2, pady= 10, padx= 10, ipadx=100)

# Query Button
q= Button(wind, text= 'Show records', command= query)
q.grid(row= 7, column= 0, columnspan =2, pady =10, padx= 10, ipadx= 137)

# Frame define
fr = Frame(wind)
fr.grid(row = 10, column=1)

# Delete Button
d= Button(wind, text= 'Delete record', command= delboxg)
d.grid(row= 8, column= 0, columnspan =2, pady =10, padx= 10, ipadx= 137)

# Update Button
u= Button(wind, text= 'Update record', command= updboxg)
u.grid(row= 9, column=0, columnspan =2, pady =10, padx= 10, ipadx= 137)
# commit changes
con.commit()
# close connnection
con.close()
wind.mainloop()
