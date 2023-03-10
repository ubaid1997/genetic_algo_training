import numpy as np
import matplotlib.pyplot as plt
from ypstruct import structure
import ga

# Cost Function (Sphere test function)
def sphere(x):
    return sum(x**2)

# Problem Definition
problem = structure()
problem.costfunc = sphere
problem.nvar = 5
problem.varmin = -10
problem.varmax = 10

# GA Parameters
params = structure()
params.maxit = 100
params.npop = 20
params.pc = 1
params.gamma = 0.1
params.sigma = 0.1
params.mu = 0.1

# Run GA
out = ga.run(problem,params)
print(0)

# Results
plt.semilogy(out.bestcost)
plt.xlim(0,params.maxit)
plt.xlabel('Iterations')
plt.ylabel('Best Cost')
plt.title('Genetic Algo (GA)')
plt.grid(True)
plt.show()