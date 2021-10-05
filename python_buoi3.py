#Thay đổi các thuộc tính account_number, account_name, balance trong class BankAccount thành thuộc tính ẩn, và triển khai thêm các phương thức:
#get_account_number()
##get_balance()
#set_balance() - balance phải lớn hơn hoặc bằng 0
#Thay đổi các phương thức display(), withdraw() và deposit() sử dụng các phương thức getter và setter trên.
#Chú ý:
#Với withdraw(), amount phải lớn hơn 0 và nhỏ hơn balance
#Với deposit(), amount phải lớn hơn 0
#Nếu giá trị không phù hợp thì thông báo ra console

class BankAccount:

   def __init__(self,account_number, Customer,balance=0):
        self.account_number = account_number
        self.account_name = Customer
        self.set_balance=balance

   @property
   def get_account_number(self):
       return self.account_number

   @property
   def get_account_name(self):
       return self.account_name
   @property
   def get_account_balance(self):
       return self.balance
   @get_account_balance.setter
   def set_balance(self,balance):
       if balance>=0:
           self.balance=balance
       else:
           print("số dư tài khoản phải lớn hơn hoặc bằng 0")
   def withdraw(self,amount):
       if amount>0 and amount<self.get_account_balance:
           self.set_balance=self.get_account_balance-amount
       else:
           print("amount nhập vào không hợp lệ")
   def deposit(self,amount):
       if amount>0:
           self.set_balance=self.get_account_balance+amount
       else:
           print("amount nhập vào không hợp lệ")
   def display(self):
       print(f'account_number: {self.get_account_number}')
       self.account_name.get_info()
       print(f'account_balance: {self.get_account_balance}')
class SavingAccount (BankAccount):
    def monthly_interest_rate(self):
        self.monthly_interest_rate = 0.005
        return  super.get_account_balance*self.monthly_interest_rate
class Customer :
    def __init__(self,name, date_of_birth, email, phone):
        self.name=name
        self.date_of_birth= date_of_birth
        self.email=email
        self.phone=phone
    def get_info(self):
        print(f'họ tên: {self.name}, ngày sinh: {self.date_of_birth}, email: {self.email}, phone: {self.phone}')




cus= Customer("lan","02-02-1997","lelan2297@gmail.com","0987654321")
bl=BankAccount("123",cus,9)
bl.display()

