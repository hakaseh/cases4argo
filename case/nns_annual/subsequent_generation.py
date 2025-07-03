# Start of user input
N = 10    # population/ensemble size
# End of user input

if __name__ == "__main__":
    # your script logic here

    import eatpy
    import numpy as np
    from scipy.stats import qmc
    from define_parameter_range import parameter_range,parameter_path
    import random

    name_para = [row[0] for row in parameter_range]
    l_bounds = [row[1] for row in parameter_range]
    u_bounds = [row[2] for row in parameter_range]
    n_decimals = [row[3] for row in parameter_range]


#    with eatpy.models.gotm.YAMLEnsemble("gotm.yaml", N) as gotm, eatpy.models.gotm.YAMLEnsemble("fabm.yaml", N) as fabm:
#    # Link each gotm_####.yaml to the corresponding fabm_####.yaml
#        gotm["fabm/yaml_file"] = fabm.file_paths
#    # Set the MEMG model parameters
#        #fabm["instances/1p1z/parameters/K_Phy"] *= np.random.lognormal(sigma=0.2, size=N)
#        for i in range(len(name_para)):
#            fabm[parameter_path+name_para[i]] = sample_rounded[:,i]

# replace the first individual with the randomly generated indiviual below
# there must be a better way but i am unfamiliar with yaml or eatpy tool so do this way for now.
    with eatpy.models.gotm.YAMLEnsemble("fabm.yaml", 1) as fabm:
    # Set the MEMG model parameters
        for i in range(len(name_para)):
            fabm[parameter_path+name_para[i]] = np.round(random.uniform(l_bounds[i],u_bounds[i]),decimals=n_decimals[i])

#DELETE???
    # Save the paramter values
#    header = ','.join(name_para)
#    np.savetxt("parameter-values-" + str(N) + ".csv",
#               sample_rounded,
#               delimiter=",",
#               header=header,
#               comments='')