import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

data=pd.read_csv('company_sales_data.csv')

plt.plot('month_number','total_profit')
plt.xlabel('month')
plt.ylabel('profits')
plt.grid()
plt.show()