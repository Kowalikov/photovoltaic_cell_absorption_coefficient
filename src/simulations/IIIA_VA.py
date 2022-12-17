import numpy as np

def band_gap_from_mole_fraction(band_gaps, material_type, method="VCA", calc_params=None, points=20):

     if material_type=="IIIA_2_VA_1":
          
          ## Reference: Properties of Semiconductor Alloys - Sadao Adachi.pdf
          if method=="VCA":
               x = np.linspace(0, 1, points) # fraction mole
               p_A = band_gaps[0] # band gap of first component
               p_B = band_gaps[1] # band gap of second component
               
               if calc_params is None:
                    p_AxB1_x = x*p_A+(1-x)*p_B
               elif "bowing_parameters" in calc_params:
                    c = calc_params["bowing_parameters"]
                    if type(calc_params["bowing_parameters"]) is float:
                         p_AxB1_x = x*p_A+(1-x)*p_B-x*(1-x)*c
                    elif type(calc_params["bowing_parameters"]) is list:
                         p_AxB1_x = x*p_A+(1-x)*p_B-x*(1-x)*(c[0]+c[1]*x)
                         
               return x, p_AxB1_x


def calculating_bandgaps_from_varshni_relation(eg_0k, a, b, t=300):
     """
     Reference: Band parameters for III–V compound semiconductors and their alloys - Vurgaftman et al. (2001)
     """
     eg_t = eg_0k-(a*t**2)/(t+b)
     return eg_t 

def calculating_lattice_constant_from_vegard_law(a_lc, points=20):
     x = np.linspace(0, 1, points) # fraction mole
     a_A = a_lc[0]
     a_B = a_lc[1]
     
     a_AxB1_x = x*a_A+(1-x)*a_B
               
     return x, a_AxB1_x
     