class User:
    def __init__(self, citizen_id: str, name: str):
        self.__citizen_id = citizen_id
        self.__name = name
        self.__acc_list = []

    def get_name(self):
        return self.__name

    @property
    def acc_list(self):
        return self.__acc_list

    def add_account(self, acc_num):
        self.__acc_list.append(acc_num)
    
    @property
    def account(self):
        return self.__acc_list
    
class Account:
    def __init__(self, account_number: str, owner: User):
        self.__account_number = account_number
        self.__owner = owner
        self.__current_money = 0
        self.__atm_card = None
        self.__reports = []
    
    def show_reports(self):
        print("hello 1")
        for report in self.get_reports():
            print("hello")
            print(report)
            return self.get_reports()
        
    def get_reports(self):
        return self.__reports
    
    def increase_current_money(self,amount):
        self.__current_money = self.__current_money+amount
    
    def decrease_current_money(self,amount):
        self.__current_money = self.__current_money-amount
    
    def set_money(self,money):
        self.__current_money = money
        
    def set_card(self,card_number):
        self.__atm_card = card_number
        
    def get_card(self):
        return self.__atm_card

    def get_account_number(self):
        return self.__account_number

    def get_username(self):
        return self.__owner

    def get_current_money(self):
        return self.__current_money

    def change_money(self,action,amount = 0):
        if(amount <= 0):
            print("Wrong amount")
            return "Error monay naja"
        else:
            if action == "+":
                self.__current_money = self.__current_money + amount
                return self.__current_money
            elif action == "-":
                if(self.__current_money>amount):
                    self.__current_money = self.__current_money - amount
                else:
                    return "Error"

    def report(self,save): ##save transaction
        self.__reports.append(save.report_out())
        print(save.report_out())
    
class ATMCard:
    def __init__(self, card_number: str, account: Account, pin: str):
        self.__card_number = card_number
        self.__account = account
        self.__pin = pin
        
    def get_pin(self):
        return self.__pin
        
    def get_card_number(self):
        return self.__card_number

class ATMMachine:
    def __init__(self, machine_id: str, initial_amount: float = 1000000):
        self.__machine_id = machine_id
        self.__initial_amount = initial_amount
        # pass# Class Code
        
    def get_machine_id(self):
        return self.__machine_id
        
    def input_atm_card(self,bank,card_num,pin):
        for user in bank.get_user_list():
            for acc in user.account:
                if acc.get_card().get_card_number() == card_num:
                    if pin != acc.get_card().get_pin():
                        return "Invalid PIN"
                    else:
                        print(f"{acc.get_card().get_card_number()} , {acc.get_account_number()} , Success")
                        return acc
                else:
                    print("acc dont exist")
        return None
    
    def deposit(self,bank,acc,amount):
        if amount < 1:
            return "Error"
        else:
            for user in bank.get_user_list():
                for account in user.account:
                    if account.get_account_number() == acc:
                        print(f"{account.get_username().get_name()}account before test : {account.get_current_money()}")
                        account.change_money("+",amount)
                        print(f"{account.get_username().get_name()}account before test : {account.get_current_money()}")
                        self.__initial_amount = self.__initial_amount + amount
                        
                        account.report(Transaction(account.get_username().get_name(),"D",self.__machine_id,account.get_current_money()-amount,account.get_current_money()))
                        return "Success"
        return "Error"
    
    def Withdraw(self,bank,acc,amount):
        if amount < 1 or amount > self.__initial_amount:
            return "Error"
        elif amount > 40000:
            print("Exceeds daily withdrawal limit of 40,000 baht")
            return "Error"
        else: 
            for user in bank.get_user_list():
                for account in user.account:
                    if amount > account.get_current_money():
                        print("Error Not enough money")
                        return "Error"
                    elif account.get_account_number() == acc:
                        print(f"{account.get_username().get_name()}account before test : {account.get_current_money()}")
                        account.change_money("-",amount)
                        print(f"{account.get_username().get_name()}account before test : {account.get_current_money()}")
                        self.__initial_amount = self.__initial_amount + amount
                        # def __init__(self,username,status : str,atm_machine,money_before,money_aft
                        account.report(Transaction(account.get_username().get_name(),"W",self.__machine_id,account.get_current_money()+amount,account.get_current_money()))
                        return "Success"
        return "Error"
    
    def Transfer(self,bank,atm_num,acc_self,acc_other,amount,):
        # Status1 = acc_self.change_money("-",amount)
        # Status2 = acc_other.change_money("+",amount)
        # acc_self.report("TW",amount,atm_num,acc_other)
        # acc_other.report("TD",amount,atm_num,acc_self) 
        
        # if Status1 != "Error" and Status2 != "Error":
        #     return "Success"
        # else:
        #     return "Error"
        if amount < 1 or amount > self.__initial_amount  or amount > 40000:
            return "Error"
        # else: 
            # for user in bank.get_user_list():
            #     for account in user.account:
            #         if amount > account.get_current_money():
            #             print("Error Not enough money")
            #             return "Error"
            #         elif account.get_account_number() == acc_self:
            #             count+=1
            #             if count == 2:
                            
                            # Status1 = acc_self.change_money("-",amount)
                            # Status2 = acc_other.change_money("+",amount)
                            
                            
                            
                            # print(f"{account.get_username().get_name()}account before test : {account.get_current_money()}")
                            # account.change_money("-",amount)
                            # print(f"{account.get_username().get_name()}account before test : {account.get_current_money()}")
                            # self.__initial_amount = self.__initial_amount + amount
                            # account.report(Transaction(account.get_username().get_name(),"W",self.__machine_id,account.get_current_money()+amount,account.get_current_money()))
                            # if Status1 != "Error" and Status2 != "Error":
                            #     return "Success"    
        return "Error"
   
class Bank:  
    def __init__(self):
        self.__user_list = []
        self.__atm_list = []
    
    #'1-1101-12345-31-0':['Harry Potter','1234567890','12345',20000]
    def register(self,user_info : dict):
        for i in user_info.keys():
            user = User(i,user_info[i][0])
            acc = Account(user_info[i][1],user)
            card = ATMCard(user_info[i][2],acc,"1234")
            
            user.add_account(acc)
            self.__user_list.append(user)
            acc.set_money(user_info[i][3])
            acc.set_card(card)

    def atm_data(self,atm_info : dict):
        for j in atm_info.keys():
            self.__atm_list.append(ATMMachine(j,atm_info[j]))
    
    @property
    def user_list(self):
        return self.__user_list
    
    @property
    def atm_list(self):
        return self.__atm_list
    
    def get_user_list(self):
        return self.__user_list
    
class Transaction():
    def __init__(self,username,status : str,atm_machine,money_before,money_after):
        self.__username = username
        self.__status = status
        self.__atm_machine = atm_machine
        self.__money_before = money_before
        self.__money_after = money_after
        self.__report = f"{self.__username} transaction : {self.__status}-{self.__atm_machine}-{self.__money_before}-{self.__money_after}"
    #Hermione transaction : D-ATM:1002-1000-2000
    def report_out(self):
        return self.__report
################################################################################################################################################
# กำหนดรูปแบบของ user ดังนี้ {
    #        รหัสประชาชน :       [ชื่อ,       หมายเลขบัญชี, หมายเลข ATM_card ,จำนวนเงิน ]}
a_user ={   '1-1101-12345-31-0':['Harry Potter','1234567890','12345',20000],
            '1-1101-12345-32-0':['Hermione Jean Granger','0987654321','12346',1000]}

a_atm ={'Bangna':1000000,'Ladkrabang':200000}
aBank = Bank()
aBank.register(a_user)
aBank.atm_data(a_atm)

# Test case #1 : ทดสอบ การ insert บัตร โดยค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry    //
# และเรียกใช้ function หรือ method จากเครื่อง ATM
# ผลที่คาดหวัง : พิมพ์ หมายเลข account ของ harry อย่างถูกต้อง และ พิมพ์หมายเลขบัตร ATM อย่างถูกต้อง
# Ans : 12345, 1234567890, Success
# input_atm_card(self,bank,card_num,pin)
aBank.atm_list[0].input_atm_card(aBank,'12345',"1234")
print("-------------------------")

# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท //
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000
#deposit(self,atm_num,acc,amount):
aBank.atm_list[1].deposit(aBank,"0987654321",1000)
print("-------------------------")


# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท //
# ผลที่คาดหวัง : แสดง Error
# def deposit(self,atm_num,acc,amount):
# aBank.atm_list[0].deposit(1234567890,1234567890,-1)
print(aBank.atm_list[1].deposit(aBank,"0987654321",-1))
print("-------------------------")

# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท //
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500
aBank.atm_list[1].Withdraw(aBank,"0987654321",500)
print("-------------------------")


# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท //
# ผลที่คาดหวัง : แสดง Error
aBank.atm_list[1].Withdraw(aBank,"0987654321",2000)
print("-------------------------")

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
print(aBank.user_list[0].acc_list[0].show_reports())
print("-------------------------")

# Test case #8 : ทดสอบการใส่ PIN ไม่ถูกต้อง     //
# ให้เรียกใช้ method ที่ทำการ insert card และตรวจสอบ PIN
# atm_machine = bank.get_atm('1001')
# test_result = atm_machine.insert_card('12345', '9999')  # ใส่ PIN ผิด
# ผลที่คาดหวัง
# Invalid PIN
print(aBank.atm_list[0].input_atm_card(aBank,'12345',"9999"))
print("-------------------------")

# Test case #9 : ทดสอบการถอนเงินเกินวงเงินต่อวัน (40,000 บาท)    //
# atm_machine = bank.get_atm('1001')
# account = atm_machine.insert_card('12345', '1234')  # PIN ถูกต้อง
# harry_balance_before = account.get_balance()
aBank.atm_list[1].Withdraw(aBank,"0987654321",45000)
print("-------------------------")


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

# TODO 1 : จากข้อมูลใน user ให้สร้าง instance โดยมีข้อมูล //
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง


# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 2 ตัว ได้แก่ 1) instance ของธนาคาร //
# TODO     2) atm_card เป็นหมายเลขของ atm_card
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

