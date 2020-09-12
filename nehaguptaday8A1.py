#!/usr/bin/env python
# coding: utf-8

# # Decorator function for printing factorial of number

# In[5]:


# A decorator function for function 'f' passed 
# as parameter 
def memoize_factorial(f): 
    memory = {} 
  
    # This inner function has access to memory 
    # and 'f' 
    def inner(num): 
        if num not in memory:          
            memory[num] = f(num) 
        return memory[num] 
  
    return inner 
      
@memoize_factorial
def facto(num): 
    if num == 1: 
        return 1
    else: 
        return num * facto(num-1) 
  
print(facto(6)) 


# # end
