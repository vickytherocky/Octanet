import tkinter as tk
from tkinter import messagebox

class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount}")
        return f"${amount} deposited successfully."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        self.transaction_history.append(f"Withdrawn: ${amount}")
        return f"${amount} withdrawn successfully."

    def check_balance(self):
        return f"Your current balance is: ${self.balance}"

    def change_pin(self, old_pin, new_pin):
        if self.pin != old_pin:
            return "Incorrect old PIN."
        self.pin = new_pin
        return "PIN changed successfully."

    def get_transaction_history(self):
        return self.transaction_history if self.transaction_history else ["No transactions yet."]

class ATM:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_number, pin, initial_balance=0):
        if account_number in self.accounts:
            return "Account already exists."
        self.accounts[account_number] = Account(account_number, pin, initial_balance)
        return "Account created successfully."

    def access_account(self, account_number, pin):
        if account_number not in self.accounts:
            return None, "Account not found."
        account = self.accounts[account_number]
        if account.pin != pin:
            return None, "Incorrect PIN."
        return account, "Access granted."

class ATMGUI:
    def __init__(self, root):
        self.atm = ATM()
        self.current_account = None
        self.root = root
        self.root.title("ATM Machine")

        # Set the size of the main GUI window
        self.root.geometry("400x300")

        # Centering the window on the screen
        window_width = 400
        window_height = 300
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Colors
        self.bg_color = "#f0f0f0"
        self.button_bg_color = "#4CAF50"
        self.button_fg_color = "#ffffff"
        self.entry_bg_color = "#ffffff"
        self.header_color = "#333333"

        # Fonts
        self.header_font = ('Helvetica', 16, 'bold')
        self.label_font = ('Helvetica', 14)
        self.entry_font = ('Helvetica', 12)
        self.button_font = ('Helvetica', 14, 'bold')

        self.create_welcome_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_welcome_screen(self):
        self.clear_screen()
        self.root.configure(bg=self.bg_color)

        tk.Label(self.root, text="ATM MACHINE", font=self.header_font, bg=self.bg_color, fg=self.header_color).pack(pady=20)

        tk.Button(self.root, text="Create Account", command=self.create_account_screen, font=self.button_font, bg=self.button_bg_color, fg=self.button_fg_color).pack(pady=10)
        tk.Button(self.root, text="Access Account", command=self.access_account_screen, font=self.button_font, bg=self.button_bg_color, fg=self.button_fg_color).pack(pady=10)

    def create_account_screen(self):
        self.clear_screen()
        self.root.configure(bg=self.bg_color)

        tk.Label(self.root, text="Create Account", font=self.header_font, bg=self.bg_color, fg=self.header_color).pack(pady=20)

        tk.Label(self.root, text="Account Number", font=self.label_font, bg=self.bg_color).pack()
        account_number_entry = tk.Entry(self.root, font=self.entry_font, bg=self.entry_bg_color)
        account_number_entry.pack(pady=5)

        tk.Label(self.root, text="PIN", font=self.label_font, bg=self.bg_color).pack()
        pin_entry = tk.Entry(self.root, show="*", font=self.entry_font, bg=self.entry_bg_color)
        pin_entry.pack(pady=5)

        tk.Label(self.root, text="Initial Balance", font=self.label_font, bg=self.bg_color).pack()
        balance_entry = tk.Entry(self.root, font=self.entry_font, bg=self.entry_bg_color)
        balance_entry.pack(pady=5)

        def create_account():
            account_number = account_number_entry.get()
            pin = pin_entry.get()
            initial_balance = float(balance_entry.get() or 0)
            message = self.atm.add_account(account_number, pin, initial_balance)
            messagebox.showinfo("Info", message)
            self.create_welcome_screen()

        tk.Button(self.root, text="Create", command=create_account, font=self.button_font, bg=self.button_bg_color, fg=self.button_fg_color).pack(pady=20)
        tk.Button(self.root, text="Back", command=self.create_welcome_screen, font=self.button_font, bg=self.button_bg_color, fg=self.button_fg_color).pack(pady=10)

    def access_account_screen(self):
        self.clear_screen()
        self.root.configure(bg=self.bg_color)

        tk.Label(self.root, text="Access Account", font=self.header_font, bg=self.bg_color, fg=self.header_color).pack(pady=20)

        tk.Label(self.root, text="Account Number", font=self.label_font, bg=self.bg_color).pack()
        account_number_entry = tk.Entry(self.root, font=self.entry_font, bg=self.entry_bg_color)
        account_number_entry.pack(pady=5)

        tk.Label(self.root, text="PIN", font=self.label_font, bg=self.bg_color).pack()
        pin_entry = tk.Entry(self.root, show="*", font=self.entry_font, bg=self.entry_bg_color)
        pin_entry.pack(pady=5)

        def access_account():
            account_number = account_number_entry.get()
            pin = pin_entry.get()
            account, message = self.atm.access_account(account_number, pin)
            if account:
                self.current_account = account
                self.account_screen()
            else:
                messagebox.showerror("Error", message)

        tk.Button(self.root, text="Access", command=access_account, font=self.button_font, bg=self.button_bg_color, fg=self.button_fg_color).pack(pady=20)
        tk.Button(self.root, text="Back", command=self.create_welcome_screen, font=self.button_font, bg=self.button_bg_color, fg=self.button_fg_color).pack(pady=10)

    def account_screen(self):
        self.clear_screen()
        self.root.configure(bg=self.bg_color)

        tk.Label(self.root, text="Account Menu", font=self.header_font, bg=self.bg_color, fg=self.header_color).pack(pady=20)

        tk.Button(self.root, text="Check Balance", command=self.check_balance, font=self.button_font, bg=self.button_bg_color, fg=self.button_fg_color).pack(pady=10)
        tk.Button(self.root, text="Deposit Cash", command=self.deposit_cash_screen, font=self.button_font, bg=self.button_bg_color, fg=self.button_fg_color).pack(pady=10)
        tk.Button(self.root, text="Withdraw Cash", command=self.withdraw_cash_screen, font=self.button_font, bg=self.button_bg_color, fg=self.button_fg_color).pack(pady=10)
        tk.Button(self.root, text="Change PIN", command=self.change_pin_screen, font=self.button_font, bg=self.button_bg_color, fg=self.button_fg_color).pack(pady=10)
        tk.Button(self.root, text="Transaction History", command=self.transaction_history_screen, font=self.button_font, bg=self.button_bg_color, fg=self.button_fg_color).pack(pady=10)
        tk.Button(self.root, text="Logout", command=self.create_welcome_screen, font=self.button_font, bg=self.button_bg_color, fg=self.button_fg_color).pack(pady=10)

    def check_balance(self):
        messagebox.showinfo("Balance", self.current_account.check_balance())

    def deposit_cash_screen(self):
        self.clear_screen()
        self.root.configure(bg=self.bg_color)

        tk.Label(self.root, text="Deposit Cash", font=self.header_font, bg=self.bg_color, fg=self.header_color).pack(pady=20)

        tk.Label(self.root, text="Amount", font=self.label_font, bg=self.bg_color).pack()
        amount_entry = tk.Entry(self.root, font=self.entry_font, bg=self.entry_bg_color)
        amount_entry.pack(pady=5)

        def deposit_cash():
            amount = float(amount_entry.get())
            message = self.current_account.deposit(amount)
            messagebox.showinfo("Deposit", message)
            self.account_screen()

        tk.Button(self.root, text="Deposit", command=deposit_cash, font=self.button_font, bg=self.button_bg_color, fg=self.button_fg_color).pack(pady=20)
        tk.Button(self.root, text="Back", command=self.account_screen, font=self.button_font, bg=self.button_bg_color, fg=self.button_fg_color).pack(pady=10)

    def withdraw_cash_screen(self):
        self.clear_screen()
        self.root.configure(bg=self.bg_color)

        tk.Label(self.root, text="Withdraw Cash", font=self.header_font, bg=self.bg_color, fg=self.header_color).pack(pady=20)

        tk.Label(self.root, text="Amount", font=self.label_font, bg=self.bg_color).pack()
        amount_entry = tk.Entry(self.root, font=self.entry_font, bg=self.entry_bg_color)
        amount_entry.pack(pady=5)

        def withdraw_cash():
            amount = float(amount_entry.get())
            message = self.current_account.withdraw(amount)
            messagebox.showinfo("Withdraw", message)
            self.account_screen()

        tk.Button(self.root, text="Withdraw", command=withdraw_cash, font=self.button_font, bg=self.button_bg_color, fg=self.button_fg_color).pack(pady=20)
        tk.Button(self.root, text="Back", command=self.account_screen, font=self.button_font, bg=self.button_bg_color, fg=self.button_fg_color).pack(pady=10)

    def change_pin_screen(self):
        self.clear_screen()
        self.root.configure(bg=self.bg_color)

        tk.Label(self.root, text="Change PIN", font=self.header_font, bg=self.bg_color, fg=self.header_color).pack(pady=20)

        tk.Label(self.root, text="Old PIN", font=self.label_font, bg=self.bg_color).pack()
        old_pin_entry = tk.Entry(self.root, show="*", font=self.entry_font, bg=self.entry_bg_color)
        old_pin_entry.pack(pady=5)

        tk.Label(self.root, text="New PIN", font=self.label_font, bg=self.bg_color).pack()
        new_pin_entry = tk.Entry(self.root, show="*", font=self.entry_font, bg=self.entry_bg_color)
        new_pin_entry.pack(pady=5)

        def change_pin():
            old_pin = old_pin_entry.get()
            new_pin = new_pin_entry.get()
            message = self.current_account.change_pin(old_pin, new_pin)
            messagebox.showinfo("Change PIN", message)
            self.account_screen()

        tk.Button(self.root, text="Change", command=change_pin, font=self.button_font, bg=self.button_bg_color, fg=self.button_fg_color).pack(pady=20)
        tk.Button(self.root, text="Back", command=self.account_screen, font=self.button_font, bg=self.button_bg_color, fg=self.button_fg_color).pack(pady=10)

    def transaction_history_screen(self):
        self.clear_screen()
        self.root.configure(bg=self.bg_color)

        tk.Label(self.root, text="Transaction History", font=self.header_font, bg=self.bg_color, fg=self.header_color).pack(pady=20)

        transaction_listbox = tk.Listbox(self.root, font=self.entry_font, bg=self.entry_bg_color)
        transaction_listbox.pack(pady=5, fill=tk.BOTH, expand=True)

        for transaction in self.current_account.get_transaction_history():
            transaction_listbox.insert(tk.END, transaction)

        tk.Button(self.root, text="Back", command=self.account_screen, font=self.button_font, bg=self.button_bg_color, fg=self.button_fg_color).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = ATMGUI(root)
    root.mainloop()
