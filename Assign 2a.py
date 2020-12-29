#get the rate of exchange of USD to EUR from the user and get USD dollars to convert it into corresponding Euro value 
'''
Original Currency / New Currency = Exchange Rate. 
By today’s rate of exchange,
1 EUR = 1.22532 USD
1 USD = 0.816116 EUR
'''
ex_rate = float(input("Enter the exchange rate between US Dollars and Euro : "))
print(ex_rate)
US_Dollar = int(input("Enter the value of US Dollars : "))
print(US_Dollar)
Euro =  US_Dollar / ex_rate 
print("The value of Euro for corresponding US Dollar given is : ",Euro)

'''
o/p:
Enter the exchange rate between US Dollars and Euro : 1.22
Enter the value of US Dollars : 10
The value of Euro for corresponding US Dollar given is :  8.19672131147541
'''
