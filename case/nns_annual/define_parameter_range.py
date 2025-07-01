# This file defines the parameter range and precision (decimal points) used for sensitivity analysis.
#
# Relevant files: fabm.yaml and generate_ensemble_yaml.py
#
# parameter_path: path to the parameter
# parameter_range: name, lower bound, upper bound, and decimal points for rounding

parameter_path = "instances/1p1z/parameters/"

parameter_range = [             
['attCHL',0.006,0.046,3],
['I_thNH4',0.008,0.015,3],
['D_p5NH4',0.05,0.15,2],
['NitriR',0.01,0.5,2],
['K_NO3',0.5,5,1],
['K_NH4',0.5,5,1],
['Vp0',0.1,3.5,1],
['K_Phy',0.5,5.0,1],
#['PhyCN',6.625],
['PhyIS',0.007,0.13,3],
['PhyMR',0.01,0.25,2],
['Chl2C_m',0.005,0.15,3],
['ZooAE_N',0.25,0.95,2],
['ZooBM',0.01,0.35,2],
['ZooER',0.02,0.35,2],
['ZooGR',0.2,4.0,1],
['ZooMR',0.02,0.35,2],  
#['ZooCN',6.625], 
['LDeRRN',0.005,0.6,3], 
['SDeRRN',0.005,0.1,3],   
['CoagR',0.001,1,3], 
['wP',0.05,1.5,2],
['wL',0.5,10,1],
['wS',0.05,1.5,2], 
]
