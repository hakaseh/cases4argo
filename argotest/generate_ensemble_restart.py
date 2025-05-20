import eatpy
import numpy as np
N = 10    # ensemble size
with eatpy.models.gotm.RestartEnsemble("restart.nc", N) as f:
    for name, values in f.template.items():
        if name not in ("h", "z", "zi", "lon", "lat"):
            scale_factors = np.random.lognormal(sigma=0.1, size=(N,) + values.shape)
            f[name] = values * scale_factors
