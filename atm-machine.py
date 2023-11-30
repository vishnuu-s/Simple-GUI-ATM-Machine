import os
import time
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

try:
    f = open('Accounts.txt', 'r')
    f.close()
except FileNotFoundError:
    f = open('Accounts.txt', 'w')
    f.close()

'''----------------------------------------------------------------------------'''


def clear_screen():
    os.system('clear')
    print()  


def read_file(file_name):
    opened_file = open(file_name, 'r')
    lines_list = []
    for line in opened_file:
        line = line.split()
        lines_list.append(line)
    return lines_list


def print_process(process):
    date = '{}'.format(process[2:7])
    print('{0}\t{1}\t{2}{3: ^10} {4: ^10}'.format(
        process[0],
        process[1].center(len('change_password')),
        date.center(len(date)),
        process[7],
        process[8]
    )
    )


def withdraw(ls, acc_list):
    def witClicked(current_balance, ls):
        withdraw_amount = int(witAmountEntry.get())
        if withdraw_amount > current_balance:
            messagebox.showerror("withdraw","You can't withdraw more than your current balance")
        else:
            current_balance -= abs(withdraw_amount)  

        file_name = ls[0] + '.txt'
        process_list = read_file(file_name)
        id_file = open(file_name, 'a')

        if len(process_list) == 0:
            last_id = 1
        else:
            last_id = int(process_list[len(process_list) - 1][0]) + 1

        id_file.write(
            '{0}\twithdraw\t\t\t{1}\t{2}\t{3}\n'.format(str(last_id), str(time.ctime()), ls[3], str(current_balance)))
        id_file.close()
        ls[3] = str(current_balance)
        bal = "Your current balance: " + ls[3]
        tk.Label(witTop, text=bal, font=("ubuntu", 12), fg="#4267B2").grid(column=0, row=3,columnspan=2, padx=(0, 10), pady=(10, 10))
        acc_file = open('Accounts.txt', 'w')
        for acc in acc_list:
            for elements in acc:
                acc_file.write("%s\t" % elements)
            acc_file.write('\n')
        return ls


    witTop = tk.Toplevel()
    center_window((300,250), witTop)
    current_balance = int(ls[3])
    cBalance = "Current Balance: "+ls[3]
    tk.Label(witTop, text=cBalance, font=("ubuntu", 12), fg="#4267B2").grid(column=0, row=0, pady=(10,10), padx=(10,10))
    tk.Label(witTop, text="Withdraw Amount ", font=("ubuntu", 12), fg="#4267B2").grid(column=0, row=1, pady=(10,10), padx=(10,10))
    witAmountEntry = tk.Entry(witTop, font=("ubuntu", 12), fg="red" ,width = 5)
    witAmountEntry.grid(column=1, row=1, padx=(10,10), pady=(10,10))

    tk.Button(witTop, text="Withdraw", font=("ubuntu", 12), fg="white", bg="#4267B2",
              command=lambda: witClicked(current_balance, ls)).grid(column=0, row=2, columnspan=2)

def deposit(ls, acc_list):
    def confirmClicked(current_balance, ls):
        deposit_amount = int(depositAmountEntry.get())
        current_balance += abs(deposit_amount) 
        file_name = ls[0] + '.txt'

        process_list = read_file(file_name)
        id_file = open(file_name, 'a')

        if len(process_list) == 0:
            last_id = 1
        else:
            last_id = int(process_list[len(process_list) - 1][0]) + 1 

        id_file.write(
            '{0}\tdeposit\t\t\t\t{1}\t{2}\t{3}\n'.format(str(last_id), str(time.ctime()), ls[3], str(current_balance)))
        id_file.close()
        ls[3] = str(current_balance)
        bal = "Your current balance: " + ls[3]
        tk.Label(depositTop, text=bal, font=("ubuntu", 12), fg="#4267B2").grid(column=0, row=3,columnspan=2, padx=(0, 10), pady=(10, 10))
        acc_file = open('Accounts.txt', 'w')
        for acc in acc_list:
            for elements in acc:
                acc_file.write("%s\t" % elements)
            acc_file.write('\n')
        return ls

    depositTop = tk.Toplevel()
    center_window((300,250), depositTop)
    current_balance = int(ls[3])
    cBalance = 'Current balance: ' + ls[3]
    tk.Label(depositTop, text=cBalance, font=("ubuntu", 12), fg="#4267B2").grid(column=0, row=0, pady=(10,10), padx=(10,10))
    tk.Label(depositTop, text="Deposit Amount ", font=("ubuntu", 12), fg="#4267B2").grid(column=0, row=1, pady=(10,10), padx=(10,10))
    depositAmountEntry = tk.Entry(depositTop, font=("ubuntu", 12), fg="red" ,width = 5)
    depositAmountEntry.grid(column=1, row=1, padx=(10,10), pady=(10,10))

    tk.Button(depositTop, text="Confirm", font=("ubuntu", 12), fg="white", bg="#4267B2",
              command=lambda: confirmClicked(current_balance, ls)).grid(column=0, row=2, columnspan=2)

    

def show_history(ls):
    hisTop = tk.Toplevel()
    label = tk.Label(hisTop, text="History", font=("ubuntu", 33), bg="#4267B2", fg="#FFFFFF", width=100)
    label.place(relx=0.5, rely=0.08, anchor="center")

    file_name = ls[0] + '.txt'
    id_list = read_file(file_name)
    top_line = '\nID\t   ' + 'Type'.center(len('change_password')+4) + 'Date and Time'.center(40+7) + 'before'.center(
        15) + 'after'.center(20)

    linet = ('-' * (len(top_line)+10))
    depline=""
    tk.Label(hisTop, text=top_line, font=("ubuntu", 10), fg="#4267B2").grid(column=0, row=0, pady=(60, 0))
    tk.Label(hisTop, text=linet, font=("ubuntu", 10), fg="#4267B2").grid(column=0, row=1)

    for line in id_list:
        date = '{}'.format(line[2:7])
        hline = ('{0}\t{1}\t{2}{3: ^10} {4: ^10}'.format(line[0],line[1].center(len('change_password')), date.center(len(date)),line[7],line[8]))
        depline = depline + "\n\n "+hline

    tk.Label(hisTop, text=depline, font=("ubuntu", 10), fg="#4267B2").grid(column=0, row=2, pady=(0,20))


def login(acc_list, loginWindow, LoginButton):
    def loginButtonClicked():
        Id = entryid.get()
        password = entryPass.get()
        login_id = Id
        login_password = password
        found = False
        for account in acc_list:
            if account[0] == login_id and account[2] == login_password:
                found = True
                LoginButton['text'] = "Log Out"
                menu2(account, acc_list, loginWindow)
                break
            else:
                continue

        if not found:
            messagebox.showerror("ATM Machine", "Wrong ID or Password")

        else:
            acc_file = open('Accounts.txt', 'w')
            print('Saving changes...')

            for acc in acc_list:
                for elements in acc:
                    acc_file.write("%s\t" % elements)
                acc_file.write('\n')

    frame = tk.Frame(loginWindow, bg="#4267B2")
    labelId = tk.Label(frame, text="Enter ID", font=("ubuntu", 14), bg="#4267B2", fg="white")
    labelPass = tk.Label(frame, text="Password", font=("ubuntu", 14), bg="#4267B2", fg="white")
    entryid = tk.Entry(frame, font=("ubuntu", 14), fg="#4267B2", width=8)
    entryPass = tk.Entry(frame, font=("ubuntu", 14), fg="#4267B2", width=15)
    loginButton = tk.Button(frame, text="login", font=("ubuntu", 14), bg="white", fg="#4267B2",
                            command=loginButtonClicked)

    labelId.grid(column=0, row=1, padx=(10, 10), pady=(10, 10))
    labelPass.grid(column=0, row=2, padx=(10, 10), pady=(10, 10))
    entryid.grid(column=1, row=1, padx=(10, 10), pady=(10, 10))
    entryPass.grid(column=1, row=2, padx=(10, 10), pady=(10, 10))
    loginButton.grid(column=1, row=3, columnspan=2, padx=(10, 10), pady=(10, 10))

    frame.grid(column=0, row=0, padx=(0, 0), pady=(60, 0))


def create_account(ls, CreatedWindow):
    def createdClicked():
        name = entryName.get()
        password = entryPass.get()
        account_name = name
        account_password = password

        accounts_file = open('Accounts.txt', 'a')

        if len(ls) == 0:
            new_last_id = 1
        else:
            new_last_id = int(ls[len(ls) - 1][0]) + 1

        line = '{0}\t{1}\t{2}\t0\n'.format(str(new_last_id), account_name, account_password)

        accounts_file.write(line)
        id_file_name = str(new_last_id) + '.txt'
        id_file = open(id_file_name, 'w')

        accountConf = ("Your Account Has Been Created \n Your Id is")
        tk.Label(CreatedWindow, text=accountConf, font=("ubuntu", 12), bg="#D9D9D9", fg="#4267B2").grid(column=0, row=1,
                                                                                                        padx=(20, 20),
                                                                                                        pady=(10, 10),
                                                                                                        columnspan=2)
        tk.Label(CreatedWindow, text=str(new_last_id), font=("ubuntu", 40), bg="#D9D9D9", fg="#4267B2").grid(column=0,
                                                                                                             row=2,
                                                                                                             padx=(
                                                                                                             20, 20),
                                                                                                             pady=(
                                                                                                             10, 10),
                                                                                                             columnspan=2)

        id_file.close()
        accounts_file.close()
        ls.append([str(new_last_id), account_name, account_password, '0'])

    frame = tk.Frame(CreatedWindow, bg="#4267B2")
    labelName = tk.Label(frame, text="Enter Name", font=("ubuntu", 14), bg="#4267B2", fg="white")
    labelPass = tk.Label(frame, text="Password", font=("ubuntu", 14), bg="#4267B2", fg="white")
    entryName = tk.Entry(frame, font=("ubuntu", 14), fg="#4267B2", width=11)
    entryPass = tk.Entry(frame, font=("ubuntu", 14), fg="#4267B2", width=13)
    CreatedButton = tk.Button(frame, text="Create Account", font=("ubuntu", 14), bg="white", fg="#4267B2",
                              command=createdClicked)

    labelName.grid(column=0, row=1, padx=(10, 10), pady=(10, 10))
    labelPass.grid(column=0, row=2, padx=(10, 10), pady=(10, 10))
    entryName.grid(column=1, row=1, padx=(10, 10), pady=(10, 10))
    entryPass.grid(column=1, row=2, padx=(10, 20), pady=(10, 10))
    CreatedButton.grid(column=0, row=3, columnspan=2, padx=(10, 10), pady=(10, 10))

    frame.grid(column=0, row=0, padx=(0, 0), pady=(60, 0))


def menu2(account,acc_list, loginWindow):
    def infoClicked():
        infoTop = tk.Toplevel(loginWindow)

        info = ("ID: {}\nName: {}\nBalance: {}\n".format(account[0], account[1], account[3]))
        tk.Label(infoTop, text=info, font=("ubuntu", 14), bg="#D9D9D9", fg="#4267B2").grid(column=0, row=0)
        center_window((200, 100), infoTop)

    def hisClicked():
        show_history(account)

    def depClicked():
        deposit(account, acc_list)

    def witClicked():
        withdraw(account, acc_list)

    wel = ("\nHello, {0}".format(account[1]))
    manu2Frame = tk.Frame(loginWindow, bg="white")

    labelWelcome = tk.Label(loginWindow, text=wel, font=("ubuntu", 20), bg="#D9D9D9", fg="#4267B2")
    labelWelcome.grid(column=0, row=1)

    tk.Button(manu2Frame, text="InFo", font=("ubuntu", 12), bg="#4267B2", fg="white", width=8, height=1,
              command=infoClicked).grid(column=0, row=0)
    tk.Button(manu2Frame, text="History", font=("ubuntu", 12), bg="#4267B2", fg="white", width=8, height=1,
              command=hisClicked).grid(column=0, row=1)
    tk.Button(manu2Frame, text="Deposit", font=("ubuntu", 12), bg="#4267B2", fg="white", width=8, height=1,
              command=depClicked).grid(column=0, row=2)
    tk.Button(manu2Frame, text="Withdraw", font=("ubuntu", 12), bg="#4267B2", fg="white", width=8, height=1,
              command=witClicked).grid(column=0, row=3)

    manu2Frame.grid(column=0, row=2, padx=(0, 0), pady=(0, 0))

accounts_list = read_file('Accounts.txt')


def center_window(size, window):
    window_width = size[
        0]  
    window_height = size[
        1]  
    window_x = int(
        (window.winfo_screenwidth() / 2) - (window_width / 2)) 
    window_y = int(
        (window.winfo_screenheight() / 2) - (window_height / 2))

    window_geometry = str(window_width) + 'x' + str(window_height) + '+' + str(window_x) + '+' + str(
        window_y)  
    window.geometry(window_geometry) 
    return


def mainWindow():
    def loginClicked():

        window.destroy()
        loginWindow = tk.Tk()
        height = 500
        width = 300
        center_window((width, height), loginWindow)

        def backLoginClicked(*args):
            loginWindow.destroy()

            mainWindow()

        label = tk.Label(loginWindow, text="ATM Machine", font=("ubuntu", 33), bg="#4267B2", fg="#FFFFFF", width=100)
        label.place(relx=0.5, rely=0.05, anchor="center")
        backLogout = "Back"
        LoginButton = tk.Button(loginWindow, text=backLogout, font=("ubuntu", 33), bg="#4267B2", width=100, fg="#FFFFFF",
                                command=backLoginClicked)
        LoginButton.place(relx=0.5, rely=0.95, anchor="center")

        login(accounts_list, loginWindow, LoginButton)


        loginWindow.mainloop()

    def createAccountClicked():
        window.destroy()
        CreatedWindow = tk.Tk()
        height = 500
        width = 300
        center_window((width, height), CreatedWindow)

        def backCreatedClicked():
            CreatedWindow.destroy()
            mainWindow()

        label = tk.Label(CreatedWindow, text="ATM Machine", font=("ubuntu", 33), bg="#4267B2", fg="#FFFFFF", width=100)
        label.place(relx=0.5, rely=0.05, anchor="center")

        CreatedButton = tk.Button(CreatedWindow, text="Back", font=("ubuntu", 33), bg="#4267B2", width=100,
                                  fg="#FFFFFF", command=backCreatedClicked)
        CreatedButton.place(relx=0.5, rely=0.95, anchor="center")

        create_account(accounts_list, CreatedWindow)

        CreatedWindow.mainloop()

    def exitClicked():
        res = messagebox.askyesnocancel("ATM machine", "Do You want to EXIT!")

        if (res == True):
            os.system('clear')
            window.destroy()
        else:
            pass

    window = tk.Tk()
    height = 500
    width = 300
    center_window((width, height), window)

    label = tk.Label(window, text="ATM Machine", font=("ubuntu", 33), bg="#4267B2", fg="#FFFFFF", width=100)
    label.place(relx=0.5, rely=0.05, anchor="center")

    loginButton = tk.Button(window, text="Login", font=("ubuntu", 33), bg="#4267B2", fg="#FFFFFF", command=loginClicked)
    loginButton.place(relx=0.5, rely=0.2, anchor="center")

    createAccountButton = tk.Button(window, text="Create\nAccount", font=("ubuntu", 33), bg="#4267B2",
                                    command=createAccountClicked, fg="#FFFFFF")
    createAccountButton.place(relx=0.5, rely=0.5, anchor="center")

    exitButton = tk.Button(window, text="Exit", font=("ubuntu", 33), bg="#4267B2", command=exitClicked, fg="#FFFFFF")
    exitButton.place(relx=0.5, rely=0.8, anchor="center")

    window.mainloop()

mainWindow()