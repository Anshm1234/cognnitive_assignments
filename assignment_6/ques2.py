import pandas as pd
import numpy  as np
# import matplotlib.pyplot as plt

subjects=('ML','Prob','Cognitive','AI','DSA')
marks=list(np.random.randint(0,100,5))
data=pd.DataFrame({'Subjects':subjects, 'Marks':marks})
print(data)
