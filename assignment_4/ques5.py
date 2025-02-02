import numpy as ny

ucs420_Ansh=ny.array([[10,20,30,40],[50,60,70,80],[90,15,20,35]])
print(ny.mean(ucs420_Ansh))
print(ny.median(ucs420_Ansh))
print(ny.max(ucs420_Ansh))
print(ny.min(ucs420_Ansh))
print(ny.unique(ucs420_Ansh))

reshaped_ucs420_ansh= ucs420_Ansh.reshape(4,3)
print(reshaped_ucs420_ansh)

resized_usc420_ansh=ny.resize(ucs420_Ansh, (2,3))
print("\n\n",resized_usc420_ansh)