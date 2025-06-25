import numpy as np

weights = np.array([0.5, 0.3, 0.2])
returns = np.array([0.1, 0.05, 0.07])
portfolio_return = np.dot(weights, returns)
print(portfolio_return)
