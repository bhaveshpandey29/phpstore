from customer import checkLogin,getCustomer,registerCustomer,getCustomerId
from admin import registerAdmin,checkAdminLogin
from product import getAllProduct,registerProduct,getProductId
from buying import buyProduct,getTotalBuyDetail,getTotalBill
from report import generateCustomerCSV
from datetime import datetime
import getpass as p
customer_name = ""
customer_contact_no = "0"

def checkCustomerCredentials():
    customer_name = input("Enter customer name: ")
    customer_contact_no = input("Enter customer contact number: ")
    return checkLogin(customer_name,customer_contact_no)

def checkAdminCredentials():
    #pass
    admin_name = input("Enter your name: ")
    admin_pass = p.getpass("Enter your password: ")
    return checkAdminLogin(admin_name,admin_pass)    

def customerArena(functionality_choice):
    if(functionality_choice == 1):
        product_name = str(input(f"Please enter the product name: "))
        prod_quantity = int(input("Please enter the quantity: ")) 
        customer_contact = str(input("Awesome! Please enter your registered mobile number to continue: "))
        customer_id = getCustomerId(customer_contact)
        prod_id = getProductId(product_name)
        total_bill = getTotalBill(prod_id,prod_quantity)
        if ((buyProduct(customer_id,prod_id,prod_quantity,total_bill))):
            print(f"Wohoo! you have sucessfully purchased the '{product_name}' and your Total Bill is: '{total_bill}'\n\n\n")
                
    elif functionality_choice ==2:
        #ordered product.
        customer_contact = str(input("Please enter your registered mobile number to see your order/s detail/s: "))
        customer_id = getCustomerId(customer_contact)
        getTotalBuyDetail(customer_id) 

    elif functionality_choice == 3:
        run() 
    else:
        print("Please enter correct choice.")
            
def adminArena(functionality_choice):
    if(functionality_choice == 1):
        #add product
        product_name = str(input("Please enter the name of the product: "))
        product_price = int(input("Please enter the price of the product: "))
        product_quantity = int(input("Please enter the quantity: "))
        registerProduct(product_name,product_price,product_quantity)
    
    elif(functionality_choice == 2):
        #Add customer
        name = str(input("Please enter the name of the new customer: "))
        contact_no = str(input("Contact number of the customer: "))
        address = str(input("Please enter the address: "))
        c_type = str(input("Please enter the customer type Individual/Business: "))
        customer_email = str(input("Please enter the email: "))
        registerCustomer(name,contact_no,address,c_type,customer_email)
    
    elif(functionality_choice == 3):
        #Generate report
        generateCustomerCSV()
    
    elif(functionality_choice == 4):
        #total transaction
        customer_id = int(input("Please enter the customer ID whose transaction details you want to see: "))
        getTotalBuyDetail(customer_id)
    
    elif(functionality_choice == 5):
        run()

    else:
        print("Please enter the correct choice.")

def registerCustomerPanel():
    name = str(input("Please enter the name of the new customer: "))
    contact_no = str(input("Contact number of the customer: "))
    address = str(input("Please enter the address: "))
    c_type = str(input("Please enter the customer type Individual/Business: "))
    customer_email = str(input("Please enter the email: "))
    registerCustomer(name,contact_no,address,c_type,customer_email)

def registerAdminPanel():
    access_token = str(input("Please enter the access token: "))
    if(access_token == "password"):
        name = str(input("Please enter your name: "))
        username = str(input("Please enter the username: "))
        password = p.getpass("Please enter the password")
        contact_no = str(input("Please enter the contact number: "))
        registerAdmin(name,username,password,contact_no,access_token)

def run():
    print("Welcome to Milk Management System".center(100,"*"))
    while True:
        print("Choice following options carefully!!")
        user_choice = int(input("1.Customer\n2.Admin\n3.Exit\n"))
        if(user_choice == 1):
            if checkCustomerCredentials():
                functionality_choice = int(input("1.Buy Product\n2.Ordered Product\n3.Logout\n"))
                customerArena(functionality_choice)
            else:
                print("Wrong credentials, try again!!")
                choice = str(input("Do you want to register (Y/N):" ))
                if(choice == "Y"):
                    registerCustomerPanel()
        elif (user_choice == 2):
            if checkAdminCredentials():
                functionality_choice = int(input("1.Add Product\n2.Add Customer\n3.Generate Report\n4.Total Transaction\n5.Logout\n"))
                adminArena(functionality_choice)
            else:
                print("Wrong creds try again!!")
                choice = str(input("Do you want to register (Y/N):" ))
                if(choice == "Y"):
                    registerAdminPanel()
        else:
            print("Thanks for using our service".center(100,"*"))
            break

#this is mentioned to initiate the project.
if __name__ == "__main__":
    run()