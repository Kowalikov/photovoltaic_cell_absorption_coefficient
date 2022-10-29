import re
from mendeleev import element
from collections import Counter

def material_type_checker(material):
    component_names = re.findall('[A-Z][^A-Z]*', material) 
    
    components = [element(c_name) for c_name in component_names]

    group_counter = Counter([c.group.symbol for c in components])
    
    material_type_extensive = [f'{group}_{numbers}' for group, numbers in zip(group_counter.keys(), group_counter.values())]
    material_type_extensive = "_".join(material_type_extensive)

    material_type = list(group_counter.keys())
    material_type = "_".join(material_type)
    
    return material_type, material_type_extensive



def roman_to_int(s):
      """
      :type s: str
      :rtype: int
      """
      roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
      i = 0
      num = 0
      while i < len(s):
         if i+1<len(s) and s[i:i+2] in roman:
            num+=roman[s[i:i+2]]
            i+=2
         else:
            num+=roman[s[i]]
            i+=1

      return num