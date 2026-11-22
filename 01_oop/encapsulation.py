#Encapsulation
class Bank:
    def __init__(self,acc_holder,acc_no):
        self.acc_holder:str=acc_holder
        self.acc_no:int=acc_no
        self.__balance:int=0
    def deposit(self,amo)->None:
        if amo<=0:
            print(f"amount should be a positive nunmber... ")
            return
        else:
            self.__balance+=amo
            print(f"Successfully Deposited Amount {amo} into your Account... ")
    def withdraw(self,amount)->None:
        
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        elif amount>self.__balance:
            print("You can't withdraw more than your Balance... ")
            return   
        else:
            self.__balance-=amount 
            print(f"You Successfully Withdrawn Amount {amount}")
    def balance(self):
            return f"Your Balance is {self.__balance}\n"
    def display_account_details(self):
        return (
            f"Account Details: \n"
            f"Account Holder: {self.acc_holder}\n"
            f"Account Number: {self.acc_no}\n"
            f"Account Balance: {self.balance()}"
        )
c1=Bank("Oggy",419)
c1.deposit(1000)
c1.withdraw(99)
print(c1.balance())
print(c1.display_account_details())
