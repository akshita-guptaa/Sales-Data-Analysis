import pandas as pd
import matplotlib.pyplot as plt

def main_menu():
    ch=0
    print("                                                       ")
    print("                                Main Menu")
    print("                                                       ")
    while ch!=9:
        print("""
          1. Show sales
          2. Show sales without index
          3. Show profit in Ascending order of each quantity
          4. Add New record into CSV
          5. Edit a record
          6. Delete a record
          7. Line Graph
          8. Bar Graph
          9. Exit
          """)
        ch=int(input("Enter your choice:"))
        if ch ==1:
            cd=pd.read_csv("sales.csv")
            print(cd)
            input("Press any key to continue.") 
        elif ch==2:
            cd=pd.read_csv("sales.csv",index_col=0)
            print(cd)
            input("Press any key to continue.")
        elif ch==3:
            cd=pd.read_csv("sales.csv")
            print(cd.sort_values(by=['Quantity']))
            input("Press any key to continue.")
        elif ch==4:
            cd=pd.read_csv("sales.csv")
            print("Insert data of particular Product in list form")
            pro= input("Enter Product name:")
            sa=int(input("Enter Sales of the product :"))
            qu=int(input("Enter Quantity of the product :"))
            dis= float(input("Enter Discount offered from this product:"))
            po=int(input("Enter Profit we get from this product:"))
            d={'Product':pro,'Sales':sa,'Quantity':qu,'Discount':dis,'Profit':po}
            cd=pd.Dataframe(d)
            cd.to_csv('sales.csv',mode='a',index =False , header= False)
            print("Data has been added.")
            input("Press any key to continue.")
        elif ch==5:
            cd=pd.read_csv("sales.csv")
            pro=input("Enter Product name to edit:")
            col=input("Enter column name to update:")
            val=input("Enter new value:")
            cd.loc[cd[cd['Product']== pro].index.values,col]=val
            cd.to_csv("sales.csv",index=False)
            print("Record has been updated...")
            input("Press any key to continue.")
        elif ch==6:
            cd=pd.read_csv("sales.csv")
            pro=input("Enter Product name to delete data:")
            cd=cd[cd.Product!=pro]
            cd.to_csv("sales.csv",index=False)
            print("Record deleted...")
            input("Press any key to continue...")
        elif ch==7:
            cd=pd.read_csv("sales.csv")
            PRODUCTS=cd["Product"]
            SALES=cd["Sales"]
            QUANTITY=cd["Quantity"]
            DISCOUNT=cd["Discount"]
            PROFIT=cd["Profit"]
            Y=0
            while Y!=7:
                print("                                                       ")
                print("                                Line Graph Menu")
                print("                                                       ")
                print("1. Product wise sales")
                print("2. Product wise quantity")
                print("3. Product wise discount")
                print("4. Product wise profit")
                print("5. All graphs separately")
                print("6. Combined data")
                print("7. Return to Main menu")
                Y = int(input("Enter your choice to get line graph: "))
                if Y == 1:
                    cd.plot(kind='line', x='Product',y='Sales', color='b')
                    plt.ylabel("Sales")
                    plt.title("Product wise sales")
                    plt.show()
                elif Y == 2:
                    cd.plot(kind='line',x='Product', y='Quantity', color='g')
                    plt.ylabel("Quantity of each product")
                    plt.title("Product wise quantity")
                    plt.show()
                elif Y == 3:
                    cd.plot(kind='line',x='Product',y = 'Discount', color='r')
                    plt.ylabel("discount given on each product")
                    plt.title("Product wise discount ")
                    plt.show()
                elif Y == 4:
                    cd.plot(kind='line',x='Product',y='Profit', color='c')
                    plt.ylabel("profit on each product")
                    plt.title("Product wise profit")
                    plt.show()
                elif Y == 5:
                    cd.plot(kind='line',x='Product',y='Sales', color='b', label="Product wise sales")
                    cd.plot(kind='line',x='Product', y='Quantity', color='g', label = "Product wise quantity")
                    cd.plot(kind='line',x='Product',y = 'Discount', color='r', label ="Product wise discount given")
                    cd.plot(kind='line',x='Product',y='Profit', color='c', label= "Product wise profit")
                    plt.legend()
                    plt.ylabel("market")
                    plt.show()
                elif Y == 6:
                    cd.plot(kind='line',color=['red','blue','black','green' ], x = 'Product',)
                    plt.title('sales of company')
                    plt.xlabel('product')
                    plt.show()   
                elif Y == 7:
                    print("line graph closed. ")
                    main_menu()
                else:
                    print("sorry!! invalid option! try again!!!")
                    main_menu()
        elif ch==8:
            cd=pd.read_csv("sales.csv")
            PRODUCTS=cd["Product"]
            SALES=cd["Sales"]
            QUANTITY=cd["Quantity"]
            DISCOUNT=cd["Discount"]
            PROFIT=cd["Profit"]
            Y=0
            while Y!=7:
                print("                                                       ")
                print("                                Bar Graph Menu")
                print("                                                       ")
                print("1. Product wise sales")
                print("2. Product wise quantity")
                print("3. Product wise discount")
                print("4. Product wise profit")
                print("5. All data")
                print("6. Combine bar graph")
                print("7. Return to Main menu")
                Y = int(input("Enter your choice to get bar graph: "))
                if Y == 1:
                    cd.plot( kind = 'bar', x='Product', y= 'Sales',color='b',width=0.5)
                    plt.ylabel("Sales")
                    plt.title("Product wise sales")
                    plt.show()
                elif Y == 2:
                    cd.plot(kind = 'bar', x='Product', y= 'Quantity', color='g',width=0.5)
                    plt.ylabel("Quantity of each product")
                    plt.title("Product wise quantity")
                    plt.show()
                elif Y == 3:
                    cd.plot(kind = 'bar',x='Product',y = 'Discount', color='r',width=0.5)
                    plt.ylabel("discount given on each product")
                    plt.title("Product wise discount given")
                    plt.show()
                elif Y == 4:
                    cd.plot(kind = 'bar',x='Product',y='Sales', color='c',width=0.5)
                    plt.ylabel("profit on each product")
                    plt.title("Product wise profit")
                    plt.show()
                elif Y == 5:
                    cd.plot(kind = 'bar', x='Product',y ='Sales', color='b',width = 0.5 ,label="Product wise sales")
                    cd.plot(kind = 'bar', x='Product', y= 'Quantity', color='g',width = 0.5 , label = "Product wise quantity")
                    cd.plot(kind = 'bar',x='Product',y = 'Discount', color='r',width = 0.5 , label ="Product wise discount given")
                    cd.plot(kind = 'bar',x='Product',y='Sales', color='c',width = 0.5 , label= "Product wise profit")
                    plt.legend()
                    plt.show()
                elif Y == 6:
                    cd.plot(kind='bar',x= 'Product')
                    plt.title('Sales of company')
                    plt.xlabel('Products')
                    plt.legend()
                    plt.show()
                elif Y == 7:
                    print("bar graph is closed .")
                    main_menu()
                else:
                    print("sorry!! invalid option! try again!!!")
                    main_menu()
        elif ch==9:
            print("Thank you for using our App, See you again")
            break
main_menu()




   

       


