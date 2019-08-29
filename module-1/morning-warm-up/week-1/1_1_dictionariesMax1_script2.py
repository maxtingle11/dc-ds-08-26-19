#!/usr/bin/env python
# coding: utf-8

# 1. Create a dictionary where each object contains a list of one float (Age) and one string (Family name) (at least 5 objects)
# Example: {Charles: [23.4, "Darwin"], Alan: [42.5, "Turing"]}

# In[33]:


people = {'Sam': [27.45, 'Smith'], 'Beyonce': [37.37, 'Knowles'], 'Lady': [33.21, 'Gaga'], 'Kim': [27.11, 'Petras'], 'Adam': [37.54, 'Lambert']}
print(people)


# 2. Delete one object from the dictionary

# In[34]:


del people["Adam"]
print(people)


# 3. Replace the float number of one of your objects - we are changing a list entry inside a dictionary record! look at Darwin's new age
# Example: {Charles: [99.73, "Darwin"], Alan: [42.5, "Turing"]}

# In[35]:


people['Kim'][0] = 34.33
print(people)


# 4. write a for loop that goes through all records in the dictionary, prints the family name and assigns the float numbers into one merged list (see ages)
# ages = [23.4, 22.9, 552.9]

# In[36]:


ages = []
for person in people:
    print(people[person][1])
    ages.append(people[person][0])

print(ages)


# 5. Download your notebbok as a .py (regular python script) save it somewhere you know

# 6. Go to terminal, navigate to the folder where you have saved the script and execute it through the terminal
# use commands: cd
# python your_script.py
# 
# [optional] Calculate with a for loop the median and mean of the ages list

# In[ ]:




