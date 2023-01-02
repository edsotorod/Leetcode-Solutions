def finalValueAfterOperations(self, operations: list[str]) -> int:
  finalVal = 0
  for index in operations:
    if index == "++X" or index == "X++":
      finalVal += 1
    else:
      finalVal -= 1
  
  return finalVal