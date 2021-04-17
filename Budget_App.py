class Budget:
    # Class initialization
    def __init__(self):
        self.balance = 0
        print("Hello!, This is the Budget App!")

#   Class Methods
    def deposit(self):
        print("*********Welcome to the Deposit method**********")
        category = input("Kindly enter budget category :\n")
        amount = int(input("Enter amount to be deposited: \n"))
        self.balance += amount
        print(f"\n You just deposited: #{amount} into {category} category, Your new total balance is : #{self.balance}")

    def withdraw(self):
        print("***********Welcome to the Withdraw method*************")
        category = input("Kindly enter budget category :\n")
        amount = int(input("Enter amount to be withdrawn:\n"))
        if self.balance >= amount:
            self.balance -= amount
            print(f"\n You withdrew: #{amount} from the {category} category, Your remaining balance is #{self.balance}")
        else: 
            print("\n Insufficient balance ")
    
    def transfer(self, amount) :
        print("***********Welcome to the transfer method**********")
        amount = int(input("How much do you want to transfer?"))
        category = input("Which budget category are you transferring funds to ?\n")
        if self.balance >= amount:
            self.balance -= amount
            print(f"You successfully transferred #{amount} to {category} category!")
        else:
            print("\n Insufficient balance")

    def get_balance(self):
        print("*********You can view you balance here***********")
        balance= input("Kindly press the enter key to view balance \n")
        print(f"Your total balance is #{self.balance} ")

 
 
# instance object of class
inst = Budget()

#Calling methods using the instance created
inst.deposit()
inst.withdraw()
inst.transfer(2000)
inst.get_balance()

