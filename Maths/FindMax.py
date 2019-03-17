# NguyenU

def find_max(nums): # returns the highest integer form given list of integers
    max = nums[0]
    for x in nums:
      if x > max:
        max = x
    
    return max


