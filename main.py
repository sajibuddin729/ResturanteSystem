from menu import *
from Resturant import *
from user import *
from Order import *
def main():
    menu = Menu()
    pizza_1 = Pizza('shukti pizza', 100, 'large',['sukti','onion'])
    menu.add_menu_item('pizza',pizza_1)
    pizza_2 = Pizza('shukti pizza1', 200, 'big large',['sukti','oil','onion'])
    menu.add_menu_item('pizza',pizza_2)
    pizza_3 = Pizza('shukti piza2', 300, 'large',['1sukti','5onion','oil'])
    menu.add_menu_item('pizza',pizza_3)
    pizza_4 = Pizza('shukti piza3', 400, 'large',['2sukti','7onion'])
    menu.add_menu_item('pizza',pizza_4)
    
    burger_1= Burger('nega',200,'chiken',['bread', 'milk'])
    menu.add_menu_item('burger',burger_1)
    burger_2= Burger('nega',200,'chiken',['bread', 'milk'])
    menu.add_menu_item('burger',burger_2)
    burger_3= Burger('nega',200,'chiken',['bread', 'milk'])
    menu.add_menu_item('burger',burger_3)
    
    coke = Drinks('coke',30,True)
    menu.add_menu_item('drinks',coke)
    coffee=Drinks('mocha',300,False)
    menu.add_menu_item('drinks',coffee)
    
    menu.show_menu()
    
    restaurant =Restaurant('sai baba resturanent',2000,menu)
    
    manager = Manager('kala chad',4,'kala@chan.com','kalipor',150,'jan 1 2022','core')
    restaurant.add_employee('manager',manager)
    chef = Chef('Rustam',6,'chupa@rustam.com','kolatoli',2330,'feb 1 2009','chef','everything')
    restaurant.add_employee('chef',chef)
    server = Server('chutu sarver',6,'nai@gmail.com','jani na',23234,'Maarch 1 2020','server')
    restaurant.add_employee('server',server)
    
    restaurant.show_employees()
    
    customer_1= Customer('sajib',8,'sajib@gmail.com','chattogram',300)
    #restaurant.add_employee('sajib',customer_1)
    order1 = Order(customer_1,[pizza_3,coffee])
    customer_1.pay_for_order(order1)
    restaurant.add_order(order1)
    
    
    restaurant.receive_payment(order1,2000,customer_1)
    
    print(f'revenue and balance after first customer ' , restaurant.revenue,restaurant.balance)
    
    
    customer_2= Customer('uddin',8,'uddin@gmail.com','chattogram',400)
    
    order2 = Order(customer_1,[pizza_3,burger_1,coffee])
    customer_2.pay_for_order(order2)
    restaurant.add_order(order2)
    restaurant.receive_payment(order2,2000000,customer_2)
    print(f'revenue and balance after 2nd customer ' , restaurant.revenue,restaurant.balance)
    
    restaurant.pay_expense(restaurant.rent,'rent')
    print(f'rent after ' , restaurant.revenue,restaurant.balance,restaurant.expense)
    
    restaurant.pay_salary(chef)
    print(f'after salary ' , restaurant.revenue,restaurant.balance,restaurant.expense)
if __name__== '__main__':
    main()