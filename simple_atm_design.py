balance = 500
def main():
    while True:
        print("1.Withdrawal")
        print("2.Deposit")
        print("3.Balance Enquiries")
        print("Other to exit")
        option = int(input("Enter your choice: "))

        if option == 1:
            withdrawal()
        elif option == 2:
            deposit()
        elif option == 3:
            balance_enquiry()
        else:
            break 
    
def withdrawal():
    global balance
    withdrawl_amt=int(input("Enter the amout to withdraw "))
    if withdrawl_amt > balance:
        print("Insufficient Balance")
    else:
        balance-=withdrawl_amt
        print(f"Available balance {balance}rs")

def deposit():
    global balance
    deposit_amt=int(input("Enter the amout to be deposit"))
    balance+=deposit_amt
    print(f"Available Balance is {balance}rs")

def balance_enquiry():
    global balance
    print(f"Available Balance {balance}rs")

main()