import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd

seed=int(input("Enter the seed"))
np.random.seed(seed)
data=np.random.randint(0,100,50)

print(data)
