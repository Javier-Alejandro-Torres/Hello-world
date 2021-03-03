def main():

    print("\nInventory Profit\n")
    print("1.Use dictionary from example\n")
    print("2.Enter Data to dictionary\n\n")
    x=int(input("You selected: "))

    if(x==1):
        print("You want to enter values")
        static_profit()
    elif(x==2):
        print("You want to use document examples")
        cost = float(input("Give me the cost:"))
        sell = float(input("Give me the sells:"))
        inventory = int(input("Give me the inventory:"))
        dynamic_profit(cost, sell, inventory)

    else:
        print("Please select 1 or 2 only")

def static_profit():

    profit1 = ({"cost_price" : 32.67, "sell_price" : 45.00 , "inventory" :1200  })
    profit2 = ({"cost_price" : 225.89 , "sell_price" : 550.00 , "inventory" : 100 })
    profit3 = ({"cost_price" : 2.77 , "sell_price" : 7.95, "inventory" : 8500 })
    print("These are the examples: \n\n"+"1. ",profit1,"\n2. ",profit2,"\n3. ",profit3,"\n4.  exit ")
    x=input("You selected: ")
    if(x=="1"):
        cost = profit1.get("cost_price")
        sell = profit1.get("sell_price")
        inventory = profit1.get("inventory")
        operaciones(cost, sell, inventory, profit1)
    elif (x == "2"):
        cost = profit2.get("cost_price")
        sell = profit2.get("sell_price")
        inventory = profit2.get("inventory")
        operaciones(cost, sell, inventory, profit2)
    elif (x == "3"):
        cost = profit3.get("cost_price")
        sell = profit3.get("sell_price")
        inventory = profit3.get("inventory")
        operaciones(cost, sell, inventory, profit3)
    elif(x=="4"):
        quit()
    else:
        print("please type a number")

def dynamic_profit(cost, sell, inventory):

    profit1 = ({"cost_price": cost, "sell_price": sell, "inventory": inventory})
    cost = profit1.get("cost_price")
    sell = profit1.get("sell_price")
    inventory = profit1.get("inventory")
    operaciones(cost, sell, inventory, profit1)

def operaciones(cost, sell, inventory, profit1):
    Total_sales = inventory* sell
    Total_cost = inventory * cost
    Profit = round(Total_sales - Total_cost)
    print("\nResult is:\n")
    print(profit1, "->", Profit)


if __name__ == '__main__':
    main()