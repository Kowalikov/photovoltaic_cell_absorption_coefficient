import os


def param_reader(components, params_file_path, param):
    """Reads parameter from files for given list of components. There need to be path provided (same for all components). Only parameter specified by the "param" will be read.

    Args:
        components (List[str]): List of the components names
        params_file_path (str): path to parameter files
        param (str): name of the parameter in the parameters files

    Returns:
        list: List of the parameter for each componenets
    """
    read_params = []
    for c in components:
        with open(os.path.join(params_file_path, c+".txt")) as f:
            lines = f.readlines()
            for line in lines:
                if line.split("=")[0]==param:
                    read_param_str = line.split("=")[1].split(" ")[0]
                    
                    read_param_float = float(read_param_str)
                    read_params.append(read_param_float)

    return read_params


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