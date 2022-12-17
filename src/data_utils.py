import os
import numpy as np


def read_binary_compounds_param(components, params_file_path, param):
    """Reads parameter from files for given list of components. There need to be path provided (same for all components). Only parameter specified by the "param" will be read.

    Args:
        components (List[str]): List of the components names
        params_file_path (str): path to parameter files
        param (str): name of the parameter in the parameters files

    Returns:
        List[float]: List of the parameter for each componenets
    """
    read_params = []
    for c in components:
        with open(os.path.join(params_file_path, c+".txt")) as f:
            lines = f.readlines()
            for line in lines:
                if line.split("=")[0]==param:
                    read_param_str = line.split("=")[1].split(" ")[0]
                    #print(read_param_str)
                    if "," in read_param_str:
                        read_param = [float(p) for p in read_param_str.split(",")]
                    else:
                        read_param = float(read_param_str)
                    read_params.append(read_param)

    return read_params


def read_binary_compounds_band_gap(components, params_file_path):
    # read band gaps in Gamma, L and X points in Brillouin zone:
    points_names = ['gamma', 'x', 'l']
    egs_0k = []
    for point in points_names:
        egs_0k.append(read_binary_compounds_param(components, params_file_path, f'Eg_{point}_0K'))
    
    egs_0k = np.asarray(egs_0k)        
    
    min_eg_ids = np.argmin(egs_0k, axis=0)
    min_egs = [egs_0k[ind, i] for i, ind in enumerate(min_eg_ids)]
    min_eg_points = [points_names[ind] for ind in min_eg_ids]
    
    alphas, betas = [], []
    for component, point in zip(components, min_eg_points):
        alphas.append(read_binary_compounds_param([component], params_file_path, f'alpha_{point}')[0])
        betas.append(read_binary_compounds_param([component], params_file_path, f'beta_{point}')[0])
    
    # print(min_eg_points, min_egs)
    # print(f'Alpha param. (Varshni param.):\t', alphas)
    # print(f'Beta param. (Varshni param.):\t', betas)
    
    return min_egs, alphas, betas, min_eg_points

def read_binary_compounds_all_band_gaps(components, params_file_path, points_names=['gamma', 'x', 'l']):
    # read band gaps in Gamma, L and X points in Brillouin zone:
    egs_0k, alphas, betas = [], [], []
    for point in points_names:
        egs_0k.append(read_binary_compounds_param(components, params_file_path, f'Eg_{point}_0K'))
        alphas.append(read_binary_compounds_param(components, params_file_path, f'alpha_{point}'))
        betas.append(read_binary_compounds_param(components, params_file_path, f'beta_{point}'))
    
    egs_0k = np.swapaxes(np.array(egs_0k), 0, 1)
    alphas = np.swapaxes(np.array(alphas), 0, 1)
    betas = np.swapaxes(np.array(betas), 0, 1)
    
    return egs_0k, alphas, betas

def read_alloys_param(alloy, params_file_path, param):
    """Reads parameter from files for given alloy. There need to be path provided. Only parameter specified by the "param" will be read.

    Args:
        alloy (str): alloy name
        params_file_path (str): path to parameter file
        param (str): name of the parameter in the parameters file

    Returns:
        float: parameter if it's number
        List[float]: list of coefficients if it's dependency from some else parameter (first is number, second is linear coefficient, third is quadratic coefficient and so on)
    """
    
    with open(os.path.join(params_file_path, alloy+".txt")) as f:
        lines = f.readlines()
        for line in lines:
            if line.split("=")[0]==param:
                read_param_str = line.split("=")[1].split(" ")[0]
                if "," in read_param_str:
                    read_param = [float(p) for p in read_param_str.split(",")]
                else:
                    read_param = float(read_param_str)

    return read_param