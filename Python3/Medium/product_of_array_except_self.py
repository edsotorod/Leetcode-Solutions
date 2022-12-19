def product_except_self(nums: list[int]) -> list[int]:
  size = len(nums)
  finalProducts = []
  
  prod = 1
  for l in range(size):
    finalProducts.append(prod)
    prod *= nums[l]
  
  prod = 1
  for r in range(size-1, -1, -1):
    finalProducts[r] = finalProducts[r] * prod
    prod *= nums[r]
  
  return finalProducts

print(product_except_self([1,2,3,4]))
print(product_except_self([-1,1,0,-3,3]))
print(product_except_self([1,2]))

'''
# Old Solution: My attempt, prefer the cleaner version on top
def product_except_self(nums: list[int]) -> list[int]:
  size = len(nums)
  leftProduct = [1]
  rightProduct = [1]
  
  for l in range(size-1):
    leftProduct.append(leftProduct[l] * nums[l])
  
  rightIndex = 0
  for r in range(size-1, 0, -1):
    rightProduct.append(rightProduct[rightIndex] * nums[r])
    rightIndex += 1
  
  finalProducts = []
  for f in range(size):
    finalProducts.append(leftProduct[f] * rightProduct[size-f-1])
  
  return finalProducts
'''