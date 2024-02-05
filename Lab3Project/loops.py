#____________________________________________________________________________________________________________
# if and else loop

name = "Tommy"
student = "Tommy"

if name == student:
    print("Hello Tommy!") 
else:
    print("Wrong Student")

print("")
print("")

#____________________________________________________________________________________________________________
# Elif

balance = 400

if balance  >= 300 and balance < 400:
  deposit_bonus = 1000
  balance += deposit_bonus
  print(balance)
elif balance >= 400 and balance <= 500:
  deposit_bonus = 1200
  balance += deposit_bonus
  print(balance)
elif balance >= 500:
  deposit_bonus = 1400
  balance += deposit_bonus
  print(balance)
else:
  print("Does not Qualify for deposit bonus")


print("")
print("")
#____________________________________________________________________________________________________________
# Ternary

liabilities = 10000
asset = 12000

profit = asset - liabilities if asset > liabilities else liabilities
print (f"Tommy has more {profit} dollars in assets than liabilities")

