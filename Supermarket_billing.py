from datetime import datetime
name=input("Enter your name: ")
#list of items
lists='''
rice   rs.20pkg
sugar  rs.30pkg
salt   rs.20pkg
oil    rs.50pl
maggie rs.40
'''


#declaration
price=0
totalprice=0
finalprice=0
billlist=[]
itemlist=[]
quantitylist=[]
pricelist=[]

#rates per item
items={'rice':20,
'sugar':30,
'salt':20,
'oil':50,
'maggie': 40,
}
option=int(input("To display the list enter option1: "))
if option==1:
    print(lists) 
    for i in range(len(items)):
        inp1=int(input("Enter 1 to buy or enter 2 to exit: "))
        if inp1==2:
            break
        if inp1==1:
            item=input("Enter the items: ")
            if item in items.keys():
                quantity=int(input("Enter the quantity: "))
                price=quantity*(items[item])
                print("Price:" ,price)
                billlist.append((item,quantity,items,price))
                totalprice+=price
                itemlist.append(item)
                quantitylist.append(quantity)
                pricelist.append(price)
                gst=(totalprice*5)/100
                finalprice=totalprice+gst
                inp2=int(input("press 1 to continue shopping or press 2 to checkout:"))
                if inp2==1:
                    print(lists)
                    continue
                if inp2==2:
                    pass
                    if finalprice!=0:
                        inp3=int(input("Payment mode(Enter 1 for Cash or Enter 2 for Card):"))
                        print(80*'-')
                        print(20*' ',"Supermarket",20*' ')
                        print(21*' ',"@Boduppal",25*'')
                        print(80*'-')
                        print("Customer name:",name,15*' ',"Date:",datetime.now())
                        if inp3==1:
                            print("Payment mode: Cash")
                        if inp3==2:
                            print("Payment mode:Card")
                        print("S.No.",5*' ' ,"Item",8*' ' ,"Quantity",8*' ' ,"Price")
                        print(80*'-')
                        for i in range(len(billlist)):
                            print(i,9*' ' ,itemlist[i],13*' ' ,quantitylist[i],11*' ' ,pricelist[i])
                            print(60*'-')
                        print("GST:",gst)
                        print(60*'-')
                        print("Total price:",totalprice)
                        print(60*'-')
                        print("Final price:",finalprice)
                        print(80*'-')
                        print(18*'*',"Thankyou! Visit Again!",18*'*')
                        print(80*'-')
                        break

                else:
                    print("You have entered the wrong number. Please check and try again!")

            else:
                print("Sorry, the item you have entered is not available!")
        else:
            print("You have entered the wrong number. Please check and try again!")
else:
    print("You have entered the wrong number. Please check and try again!")


        
    