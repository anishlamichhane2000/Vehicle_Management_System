def ShowBikes():#shows the bike in the tabular form
    print("\n")
    print("--------------------------------------------------------------------------------------------------------------------------------")
    print("Bike ID\tBike-Name\tCompany Name\tColour\t   Quantity\tPrice")
    print("--------------------------------------------------------------------------------------------------------------------------------")
    file = open("bikes.txt", "r")
 
    for line in file:
        print( line.replace(",","\t"))
       
    print("--------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    file.close()

def return_2d_list():
    '''generate 2d list form bikes.txt file and store in bike_list'''
    read_file = open("bikes.txt", "r")
    bike_list = []
    for bike in read_file:
        bike = bike.replace("\n", "")
        bike_list.append(bike.split(","))
           
    return bike_list


   

def valid_bike_id_order():
    ''' Validates bikeid  for order form user input.'''
    #Exception handling is used for preventation form unwanted error.
    id = True
    while id == True:
        try:
            validBikeId = int(input("Enter ID of the bike to order: "))
            while validBikeId <= 0 or validBikeId >len(return_2d_list()):
                 print("Please provide a valid bike ID !!!")
                 print("---------------------------------------------------")
                 validBikeId = int(input("Enter ID of the bike to order: "))
                 print("---------------------------------------------------")
            return validBikeId
            
        except :
            print("-----------------------------------------------------------------")
            print("please,Enter a valid information")
            print("-----------------------------------------------------------------")
            continue
def valid_bike_quantity_order(entered_bike_id):
    bike_id = entered_bike_id
    ''' Validates bike quantity for sells form user input.'''
    #Exception handling is used for preventation form unwanted error.
    
    qty = True
    while qty == True:
        try:
            bike_quantity = int(input("\nEnter quantity of bike to order: "))
            while bike_quantity <= 0 or bike_quantity > int(return_2d_list()[bike_id - 1][4]):
                print("\nPlease provide a valid bike quantity!!!\n")
                print("---------------------------------------------------")
                validBikeId = int(input("Enter quantity of the bike to order: "))
                print("---------------------------------------------------")
                ShowBikes()
            return bike_quantity
            break
        except:
            print("-----------------------------------------------------------------")
            print("please,Enter a valid information")
            print("-----------------------------------------------------------------")
        

def total_bike_cost(entered_bike_id,customer_quantity):
    ''' total_cost  for orders of the bike .'''
    bike_list = return_2d_list()
    total_cost = int(bike_list[entered_bike_id-1][5].replace("$",""))* customer_quantity
    return total_cost


def loops():# using loop for the proper functioning of program
    inputdata = input("do you want to order another bike,y/n= ").upper()
    if(inputdata == "Y"):
        counter = False
    else:
        counter = True
    return counter

    
    
def update_stock_order(customer_quantity,entered_bike_id):
    bike_list = return_2d_list()
    ''' Updates the stocks and increase the  stock after ordering of bike.'''
    bike_list[entered_bike_id-1][4] = int(bike_list[entered_bike_id-1][4]) + customer_quantity
    file = open("bikes.txt","w")
    for bike in bike_list:
        file.write(str(bike[0])+","+str(bike[1])+","+str(bike[2])+","+str(bike[3])+","+str(bike[4])+","+str(bike[5])+"\n")
    file.close() 
    ShowBikes()
    
def new_bill(bike_list,entered_bike_id,order_bike,customer_quantity,total_cost):
    bike_list = return_2d_list()
    '''It is used for billing receipt of sells bike'''
    for bike in bike_list:
        if(int(bike[0]) == entered_bike_id):
               bike[4] = customer_quantity
               bike[5] = "$"+str(total_cost)
               order_bike.append(bike)
    return order_bike

def show_date():#defining show_date() for datetime
    import datetime
    year = str(datetime.datetime.now() .year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
    return year + month + day + hour + minute + second
show_date()

def print_bill_order (bike_list,order_bike):#Creating orders receipt in txt and shell.
    import datetime
    company_Name = input("Enter distributors's name: ")
    shiping_company_address = input("Enter shiping company address: ")
    contact_Number = input("Enter your contact number: ")
    file= open(company_Name +""+show_date()+".txt", "a")
    file.write("===============================================================================================================\n")
    file.write("===================================0rder Bike Receipt=========================================================\n")
    file.write("==========================================================================================================\n")
    file.write("===================================Bike Management System=================================================\n")
    print("===============================================================================================================\n")
    print("===================================0rder Bike Receipt=========================================================\n")
    print("=================================================================================================================\n")
    print("===================================Bike Management System======================================================= \n")
    file.write("shiping company  name: " + company_Name + "\n")
    file.write("shiping company address: " + shiping_company_address + "\n")
    file.write("contact Number " +contact_Number + "\n")
    file.write("the bike is order in this Date & Time : " + str(datetime.datetime.now()) + "\n")
    print("shiping company  name: " + company_Name + "\n")
    print("shiping company address: " + shiping_company_address + "\n")
    print("contact Number " +contact_Number + "\n")
    print("the bike is order in this Date & Time : " + str(datetime.datetime.now()) + "\n")
    file.write("=============================================================================================================\n")
    file.write("S.N\t Bike Name\t Company \t   Quantity\tprice\ttotal_amount\n")
    file.write("=============================================================================================================\n")
    print("=============================================================================================================\n")
    print("S.N\t Bike Name\t Company\t    Quantity\tprice\ttotal_amount")
    print("=============================================================================================================\n")
    SNo = 0
    total_amount = 0
    for bike in order_bike:
         SNo = SNo + 1
         bike[5] = bike[5].replace("$","")
         total_amount = total_amount + int(bike[5])
         file.write(str(SNo)+"\t"+(str(bike[1])+"\t"+str(bike[2])+"\t\t"+str(bike[4])+"\t"+str(bike[5])+"\t"+str(total_amount)+"\t\t"))
         file.write("=============================================================================================================\n")
         print(str(SNo)+"\t"+(str(bike[1])+"\t"+str(bike[2])+"\t\t"+str(bike[4])+"\t"+str(bike[5])+"\t"+str(total_amount)+"\t\t"))
         print("=============================================================================================================\n")
    file.close
    
    

    





 
