class User:
    def __init__(self, citizen_id: str, name: str):
        self.__citizen_id = citizen_id
        self.__name = name
        self.__accounts = []

    @property
    def citizen_id(self):
        return self.__citizen_id

    @property
    def name(self):
        return self.__name

    @property
    def accounts(self):
        return self.__accounts

    def add_account(self, account):
        if isinstance(account, Account):
            self.__accounts.append(account)


class Account:
    def __init__(self, account_number: str, owner: User, initial_balance: float):
        self.__account_number = account_number
        self.__owner = owner
        self.__balance = initial_balance


    @property
    def account_number(self):
        return self.__account_number

    @property
    def owner(self):
        return self.__owner

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value: float):
        self.__balance = value
    
    


class ATMCard:
    def __init__(self, card_number: str, account: Account, pin: str):
        self.__card_number = card_number
        self.__account = account
        self.__pin = pin

    @property
    def card_number(self):
        return self.__card_number

    @property
    def account(self):
        return self.__account

    @property
    def pin(self):
        return self.__pin


class ATMMachine:
    def __init__(self, machine_id: str, initial_amount: float):
        self.__machine_id = machine_id
        self.__cash_available = initial_amount

    @property
    def machine_id(self):
        return self.__machine_id
    @property
    def cash_available(self):
        return self.__cash_available

    def input_atm_card(self, bank: "Bank", card_number: str, entered_pin: str):
        # ค้นหาบัตร ATM
        for user in bank.user_list:
            for account in user.accounts:
                card = account.card
                if card and card.card_number == card_number:
                    if card.pin == entered_pin:
                        print(f"{card.card_number}, {card.account.account_number}, Success")
                        return
                    else:
                        print("Invalid PIN")
                        return
        print("Card Not Found")

    def deposit(self,bank : "Bank", acc : str,amount : float):
        if amount < 0:
            return print("Error")

        else:
            for user in bank.user_list:
                for account in user.accounts:
                    if account.account_number == acc:
                        print(f"{user.name} account before deposit: {account.balance}")
                        account.balance += amount
                        print(f"{user.name} account after deposit: {account.balance}")
                        return "Success"
            return print("Error: Account not found")

    def withdraw(self,bank : "Bank", acc : str,amount : float):
        for user in bank.user_list:
                for account in user.accounts:
                    if account.account_number == acc:
                        if amount > account.balance:
                            return print("Error")
                        else:
                            print(f"{user.name} account before deposit: {account.balance}")
                            account.balance -= amount
                            print(f"{user.name} account after deposit: {account.balance}")
                            return "Success"
        return print("Error: Account not found")
        


class Bank:
    def __init__(self):
        self.__user_list = []
        self.__atm_list = []

    def register(self, user_info: dict):
        for citizen_id, data in user_info.items():
            name, account_number, card_number, initial_balance = data
            user = User(citizen_id, name)
            account = Account(account_number, user, initial_balance)
            card = ATMCard(card_number, account, "1234")
            account.card = card
            user.add_account(account)
            self.__user_list.append(user)

    def atm_data(self, atm_info: dict):
        for machine_id, initial_cash in atm_info.items():
            self.__atm_list.append(ATMMachine(machine_id, initial_cash))

    @property
    def user_list(self):
        return self.__user_list

    @property
    def atm_list(self):
        return self.__atm_list

    

##################################################################################

# กำหนดให้ ชื่อคลาส (Class Name) ต้องเป็น Pascal case เช่น BankAccount
# กำหนดให้ ชื่อ instance และ variables ใดๆ ต้องเป็น snake case เช่น my_book
# กำหนดให้ เมื่อรับพารามิเตอร์เข้าใน method ต้องทำ validate data type และกรอบของค่า parameter ก่อนใช้เสมอ
# กำหนดให้ method ที่จัดการข้อมูลใด ต้องอยู่ในคลาสนั้น และพยายามอย่า access attribute นอกคลาส

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, หมายเลข ATM , จำนวนเงิน]}
user_data = {'1-1101-12345-12-0':['Harry Potter','1234567890','12345',20000],
       '1-1101-12345-13-0':['Hermione Jean Granger','0987654321','12346',1000]}
   
atm_dict ={'1001':1000000,'1002':200000}

bank = Bank()
bank.register(user_data)
bank.atm_data(atm_dict)



# Test case #1 : ทดสอบ การ insert บัตร โดยค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method จากเครื่อง ATM
# ผลที่คาดหวัง : พิมพ์ หมายเลข account ของ harry อย่างถูกต้อง และ พิมพ์หมายเลขบัตร ATM อย่างถูกต้อง
print("Test case #1\n")
bank.atm_list[0].input_atm_card(bank, '12345', '1234')
print("\n-----------------------\n")
# Ans : 12345, 1234567890, Success


# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
print("Test case #2\n")
bank.atm_list[1].deposit(bank,"0987654321",1000)
print("\n-----------------------\n")
# Hermione account before test : 1000
# Hermione account after test : 2000


# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
print("Test case #3\n")
bank.atm_list[1].deposit(bank,"0987654321",-1)
print("\n-----------------------\n")
# ผลที่คาดหวัง : แสดง Error


# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
print("Test case #4\n")
bank.atm_list[1].withdraw(bank,"0987654321",500)
print("\n-----------------------\n")
# Hermione account before test : 2000
# Hermione account after test : 1500


# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
print("Test case #5\n")
bank.atm_list[1].withdraw(bank,"0987654321",2000)
print("\n-----------------------\n")
# ผลที่คาดหวัง : แสดง Error

# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500


# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : TD-ATM:1002-10000-11500

# Test case #8 : ทดสอบการใส่ PIN ไม่ถูกต้อง 
# ให้เรียกใช้ method ที่ทำการ insert card และตรวจสอบ PIN
# atm_machine = bank.get_atm('1001')
# test_result = atm_machine.insert_card('12345', '9999')  # ใส่ PIN ผิด
# ผลที่คาดหวัง
# Invalid PIN

# Test case #9 : ทดสอบการถอนเงินเกินวงเงินต่อวัน (40,000 บาท)
# atm_machine = bank.get_atm('1001')
# account = atm_machine.insert_card('12345', '1234')  # PIN ถูกต้อง
# harry_balance_before = account.get_balance()

# print(f"Harry account before test: {harry_balance_before}")
# print("Attempting to withdraw 45,000 baht...")
# result = atm_machine.withdraw(account, 45000)
# print(f"Expected result: Exceeds daily withdrawal limit of 40,000 baht")
# print(f"Actual result: {result}")
# print(f"Harry account after test: {account.get_balance()}")
# print("-------------------------")

# Test case #10 : ทดสอบการถอนเงินเมื่อเงินในตู้ ATM ไม่พอ
# atm_machine = bank.get_atm('1002')  # สมมติว่าตู้ที่ 2 มีเงินเหลือ 200,000 บาท
# account = atm_machine.insert_card('12345', '1234')

# print("Test case #10 : Test withdrawal when ATM has insufficient funds")
# print(f"ATM machine balance before: {atm_machine.get_balance()}")
# print("Attempting to withdraw 250,000 baht...")
# result = atm_machine.withdraw(account, 250000)
# print(f"Expected result: ATM has insufficient funds")
# print(f"Actual result: {result}")
# print(f"ATM machine balance after: {atm_machine.get_balance()}")
# print("-------------------------")



# TODO 1 : จากข้อมูลใน user ให้สร้าง instance ของผู้ใช้ โดยมีข้อมูล
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง
# TODO :   ต้อง validate ข้อมุลทุกอย่าง ก่อนสร้าง instance ใดๆ


# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 2 ตัว ได้แก่ 1) instance ของธนาคาร
# TODO     2) instance ของ atm_card
# TODO     return ถ้าบัตรถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
# TODO     ควรเป็น method ของเครื่อง ATM


# TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0


#TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


#TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 4 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account ตนเอง 3) instance ของ account ที่โอนไป 4) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี
