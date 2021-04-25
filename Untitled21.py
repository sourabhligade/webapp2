#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def search4vowels(phrase:str)->set:  
       """return any vowels found in the supplied phrase"""
       vowels = set('aeiou')   
       return vowels.intersection(set(phrase))  
   
def search4letters(phrase:str,letters:str='aeiou')->set:
   """return a set of letters found in the phrase"""
   return set(letters).intersection(set(phrase))
       

