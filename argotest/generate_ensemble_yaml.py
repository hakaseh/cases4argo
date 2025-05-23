# Start of user input
N = 300    # ensemble size
# End of user input

if __name__ == "__main__":
    # your script logic here

    import eatpy
    import numpy as np
    from scipy.stats import qmc
    from define_parameter_range import parameter_range,parameter_path

    name_para = [row[0] for row in parameter_range]
    l_bounds = [row[1] for row in parameter_range]
    u_bounds = [row[2] for row in parameter_range]
    n_decimals = [row[3] for row in parameter_range]

    D = len(name_para)     # parameter size
    sampler = qmc.LatinHypercube(d=D)
    sample = sampler.random(n=N)
    sample_scaled = qmc.scale(sample, l_bounds, u_bounds)
    sample_rounded = np.zeros_like(sample_scaled)
    for i in range(np.shape(sample_scaled)[1]):
        sample_rounded[:,i] = np.round(sample_scaled[:,i],decimals=n_decimals[i])
        
    with eatpy.models.gotm.YAMLEnsemble("gotm.yaml", N) as gotm, eatpy.models.gotm.YAMLEnsemble("fabm.yaml", N) as fabm:
    # Commenting below will generate identical gotm_####.yaml files (do this if you want identical physics).
    #    gotm["surface/u10/scale_factor"] = np.random.lognormal(sigma=0.1, size=N)
    #    gotm["surface/v10/scale_factor"] = np.random.lognormal(sigma=0.1, size=N)
    # Link each gotm_####.yaml to the corresponding fabm_####.yaml
        gotm["fabm/yaml_file"] = fabm.file_paths
    # Set the MEMG model parameters
        #fabm["instances/1p1z/parameters/K_Phy"] *= np.random.lognormal(sigma=0.2, size=N)
        for i in range(len(name_para)):
            fabm[parameter_path+name_para[i]] = sample_rounded[:,i]

    # Save the paramter values
    header = ','.join(name_para)
    np.savetxt("parameter-values-" + str(N) + ".csv",
               sample_rounded,
               delimiter=",",
               header=header,
               comments='')

