#!/usr/bin/env python
# coding: utf-8

# In[7]:


f = open("npython.txt", "r")

print(f.readline())

f.write("Writing to a new file\n")

try:
    f = open("npython.txt")
    
except (io.UnsupportedOperation):
    
    return false
    print("The file doesn't exist")
    
finally:
    f.close()


# In[ ]:




