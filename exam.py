print("Welcome to the Bill splitter App!\n")

while True:
    bill_amount = float(input("Enter total biil amount: "))
    num_people = int(input("Enter number of people: "))
    tip_Per = int(input("Enter tip percentage (0/5/10/15/20): "))
    print()


    tip_amount = 0
    total_bill = bill_amount
    each_person = total_bill

    if(num_people > 0):
        tip_amount = bill_amount * (tip_Per/100)
        total_bill = bill_amount + tip_amount
        each_person = total_bill / num_people

    if(bill_amount < 0): 
        print("Error: please check again")

    if(tip_Per < 0 ):
        print("Error: please cheak again") 

    print( "Tip Amount:₹", tip_amount)
    print( "Total Bill (with Tip):₹", total_bill)
    print("Each prson should pay:₹",each_person )
    print()

    extra = input("Whould you like to calculate another bill? (y/n): ")
    print("...")    

    if extra != "y":
        break