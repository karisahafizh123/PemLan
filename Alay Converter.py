#!/usr/bin/env python
# coding: utf-8

# In[9]:


def sys():
    ans = input("type something:")
    ret = ""
    for i in range(len(ans)):
        if (ans[i].lower() == "a"):
            if (i%2 == 0):
                ret = ret + "4"
            else:
                ret = ret + "@"
        elif (ans[i].lower() == "b"):
            ret = ret + "13"
        elif (ans[i].lower() == "e"):
            ret = ret + "3"
        elif (ans[i].lower() == "g"):
            ret = ret + "9"    
        elif (ans[i].lower() == "i"):
            ret = ret + "y"
        elif (ans[i].lower() == "k"):
            ret = ret + "q"
        elif (ans[i].lower() == "o"):
            ret = ret + "0" 
        elif (ans[i].lower() == "r"):
            ret = ret + "12"
        elif (ans[i].lower() == "u"):
            ret = ret + "oe"
        elif (ans[i].lower() == "y"):
            ret = ret + "i"
        elif (i % 3 == 1):
            ret = ret + ans[i].upper()
        else: 
            ret = ret + ans[i]
    print(ret)
    
sys()


# In[ ]:





# In[ ]:




