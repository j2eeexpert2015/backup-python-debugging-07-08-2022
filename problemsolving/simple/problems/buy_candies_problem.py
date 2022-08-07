price = 0.10 # First candy is 10 cents
budget = 1.00 # I have one dollar
count = 0 # Start with no candies
while budget >= price:
 count += 1 # Buy another candy!
 budget -= price
 price += 0.10 # Price goes up
print('I bought %d candies.' % count)
print('I have $%f left.' % budget)