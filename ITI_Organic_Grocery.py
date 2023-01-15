
grocery_list =["Banana","Cherry","Apple"]

prices={
"Banana":40,
"Cherry":25,
"Apple":30
}

quantity={
"Banana":15,
"Cherry":40,
"Apple":25
}

while True:
	print("Welcome ITI Organic Grocery shop")
	ch = int(input("0.to exit press 0\n1.Customer Interface press 1\n2.Adminsration Interface press 2\nEnter your choice : "))
	if ch == 1:	
		print ("Welcome to ITI Organic Grocery Client Interface ")
		c_input = int(input("1.To show our products press 1\n2.To Buy from our products press 2\n3.to print the bill press 3\nEnter your choice : "))
		if c_input == 1:
		
			print("ITI Organic Grocery list is ")
			print(grocery_list)
			print("ITI Organic Grocery prices list is ")
			print(prices.items())
			print("ITI Organic Grocery quantity list is ")
			print(quantity.items())
			
		elif c_input==2:
		
			print ("Buy from our products ")
			print("Enter quantity  that you need")
			q_b=int(input("enter quantity of Banana"))
			q_c=int(input("enter quantity of Cherry"))
			q_a=int(input("enter quantity of Apple"))
			quantity["Banana"] = 40-q_b
			quantity["Cherry"] = 70-q_c
			quantity["Apple"] =  30-q_a
			total_b=prices["Banana"] = 15*q_b
			total_c=prices["Cherry"] = 30*q_c
			total_a=prices["Apple"] =  20*q_a
			total=total_a+total_b+total_c
			
		elif c_input==3:
		
			print("#############Bill#########")
			print("Item    Quantity    Total")
			print(grocery_list[0] , quantity["Banana"]  ,prices["Banana"]  )
			print(grocery_list[1] , quantity["Cherry"] , prices["Cherry"]  )
			print(grocery_list[2] , quantity["Apple"]  , prices["Apple"]  )
			print("Total")
			print(total)
			print("***********Thank You********")
			print("Hope to see you back soon!")
			
		else:
		
			print("\nERROR: Choose only digits from the given option")
			
	if ch == 2:
	
		print ("Welcome to ITI Organic Grocery Adminstration,\n\t Nice to See you ,Sir. ")
		o_input = int(input("1.To Add new products press 1\n2.To Show Products press 2\n3.To Add Cost press 3\n4.To Change cost press 4\t"))
		
		if o_input==1:
		
			print("{'new product',quantity}")
			product_name = input("write product ")
			product_quantity=int(input("product quantity"))
			quantity.update({product_name:product_quantity})
		
		elif o_input==2:
		
			print("ITI Organic Grocery list is ")
			print(grocery_list)
			print("ITI Organic Grocery prices list is ")
			print(prices.items())
			print("ITI Organic Grocery quantity list is ")
			print(quantity.items())
		elif o_input == 3:
		
			print("{'New product',price}")
			product_name_= input("Write product ")
			product_price=int(input("Product price "))
			prices.update({product_name_:product_price})
		elif o_input == 4:
		
			product_name_1= input("Write product ")
			product_price1=int(input("Product price "))
			prices[product_name_1]=product_price1
			print("ITI Organic Grocery prices list is ")
			print(prices.items())
			
	elif ch == 0:
		break
		
	else:
		print("\nERROR: Choose only digits from the given option")