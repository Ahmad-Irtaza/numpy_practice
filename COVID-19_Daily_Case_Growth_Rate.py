import numpy as np
cases = np.array([100, 150, 200, 300])
growth = (cases[1:] - cases[:-1]) / cases[:-1] * 100
print(growth)
