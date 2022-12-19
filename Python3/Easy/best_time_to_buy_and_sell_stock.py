def max_profit(prices: list[int]) -> int:  
  maxProfit = 0
  currDay = 0
  futureDay = 1
  size = len(prices)
  
  while futureDay < size:
    profit = prices[futureDay] - prices[currDay] 
    if profit > maxProfit:
      maxProfit = profit
    if prices[currDay] > prices[futureDay]:
      currDay = futureDay
    futureDay += 1
  
  return maxProfit

print(max_profit([7,1,5,3,6,4]))
print(max_profit([7,6,4,3,1]))

'''
  Old bad solution: exceed time limit
  # maxProfit = 0
  # startDay = 1
  # size = len(prices)
  
  # for day in range(size):
  #   for future in range(startDay, size):
  #     profit = prices[future] - prices[day]
  #     if profit > maxProfit:
  #       maxProfit = profit
  #   startDay += 1
'''