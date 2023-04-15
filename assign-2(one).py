#!/usr/bin/env python
# coding: utf-8

# In[4]:


tuples_list =   [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

for i in range(len(tuples_list)):
    for j in range(i+1, len(tuples_list)):
        if tuples_list[i][-1] > tuples_list[j][-1]:
            tuples_list[i], tuples_list[j] = tuples_list[j], tuples_list[i]

print(tuples_list)


# In[ ]:




