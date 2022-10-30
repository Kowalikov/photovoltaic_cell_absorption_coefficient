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


def binary_compounds_decomposition(alloy):
    component_names = re.findall('[A-Z][^A-Z]*', alloy) 

    components = [element(c_name) for c_name in component_names]
    group_symbols = [c.group.symbol for c in components]
    group_ids = [c.group_id for c in components]

    group_counter = Counter(group_ids)
    # go through all groups counter if there is more than 1 component from the same group. 
    # That mean we have mixture of a two components in semiconductor
    for group, n in group_counter.items():
        if n>1:
            # if there is, we need to collect all components from same group
            base_compounds = []
            for (comp, comp_group) in zip(component_names, group_ids):
                if comp_group==group:
                    base_compounds.append(comp)
            
            # then we need to assign to them rest of the elements from other groups
            binary_compounds = []
            for (comp, comp_group) in zip(component_names, group_ids):
                if comp_group!=group:
                    for base in base_compounds:
                        # if the base element is from earlier group we need to assign it first in the name:
                        if group<=comp_group:
                            binary_compounds.append(base+comp)
                        # if otherwise, we need to assign it at the end:
                        if group>comp_group:
                            binary_compounds.append(comp+base)
    
    return binary_compounds