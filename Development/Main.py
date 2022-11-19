# Importing all the modules.
import datetime  # Importing date from datetime.
import sellfunction
import orderfunction

def our_message():
    """ Main function of the program."""
    print("------------------------------------------------------------------------")
    print("                 Welcome to Bike management System            ")
    print("------------------------------------------------------------------------")    
def show_options():#Its help for selecting task in program for better performation of program
    print("1. Sell Bikes")
    print("2. Order Bikes")
    print("3. Exit")

def sells_bikes():#This function is used to sell of bikes
        print("Let's sell  Bikes")
        print("------------------------------------------------------")

def order_bikes():#This function is used to order of bikes
        print("Let's order Bikes")
        print("------------------------------------------------------")
def let_exit():#This function is used to close the program
        print("------------------------------------------------------")
        print("Thank you for using Bike management System")
        print("------------------------------------------------------")
def invalid_input():#This function is used to provide invalid input which value doesnot exixt in program
        print("------------------------------------------------------")
        print("INVALID Input. Please enter the number of the options provided in the screen")
        print("------------------------------------------------------")
        



counter = True
our_message()
while counter :
    print("---------------------------------------------------------------------")   
    show_options()
    #Exception handling is used for preventation form unwanted error.
    try:
        user_input = int(input("Choose an option: "))
    
        if user_input == 1:
            counter = False
            Sold_bike = []
            while counter == False:
                sells_bikes()
                sellfunction.ShowBikes()
                entered_bike_id = sellfunction.valid_bike_id()
                customer_quantity = sellfunction.valid_bike_quantity(entered_bike_id)
                bike_list = sellfunction.return_2d_list()
                total_cost = sellfunction.total_bike_cost(entered_bike_id,customer_quantity)
                sellfunction.update_stock(customer_quantity,entered_bike_id)
                Sold_bike = sellfunction.new_bill(bike_list,entered_bike_id,Sold_bike,customer_quantity,total_cost)
                total_cost = int(bike_list[entered_bike_id-1][5].replace("$",""))* customer_quantity
                print("The total price of the bike is: ","$",total_cost)
            
                counter = sellfunction.loop()
            sellfunction.print_bill_sell(bike_list,Sold_bike)
            
        elif user_input == 2:
            order_bikes()
            counter = False
            order_bike = []
            while counter == False:
                orderfunction.ShowBikes()
                entered_bike_id =orderfunction.valid_bike_id_order()
                customer_quantity = orderfunction.valid_bike_quantity_order(entered_bike_id)
                bike_list = orderfunction.return_2d_list()
                total_cost= orderfunction.total_bike_cost(entered_bike_id,customer_quantity)
                order_bike = orderfunction.new_bill(bike_list,entered_bike_id,order_bike,customer_quantity,total_cost)
                orderfunction.update_stock_order(customer_quantity,entered_bike_id)
                print("The total price of the bike is: ","$",total_cost)
                counter = orderfunction.loops()
            orderfunction.print_bill_order(bike_list,order_bike )
        elif user_input == 3:
                let_exit()
                # Exit logic.
                counter = False
                print("-------------------Have a nice day,bye------------------------------------")
                print("--------------------------------------------------------------------------")
            
        else:
            invalid_input()
    except:
        print("-----------------------------------------------------------------")
        print("please,Enter a valid information")
        print("-----------------------------------------------------------------")
        
