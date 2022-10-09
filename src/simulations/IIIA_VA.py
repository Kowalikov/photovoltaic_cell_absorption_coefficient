import numpy as np

def band_gap_from_mole_fraction(band_gaps, material_type, method="VCA", points=20):
     """

     compounds (List[string]): names of compounds
     methods: "VCA" - Virtual Crystal Approximation
     """

     if material_type=="IIIA_2_VA_1":
          
          ## Reference: to add: file:///C:/Users/majus/Desktop/Dane/IKW/in%C5%BCynierka/W11_213626_2019_praca_in%C5%BCynierska%20(1).pdf
          if method=="VCA":
               x = np.linspace(0, 1, points) # fraction mole
               p_A = band_gaps[0] # band gap of first component
               p_B = band_gaps[1] # band gap of second component

               p_AxB1_x = x*p_A+(1-x)*p_B
               
               return x, p_AxB1_x
