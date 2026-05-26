import numpy as np

Z = np.array([[83.0], [72.5], [90.9]])

np.mean(Z)
np.std(Z)
np.max(Z)
np.min(Z)
np.argmax(Z)

print("Mean:", np.mean(Z))
print("Standard Deviation:", np.std(Z))
print("Maximum:", np.max(Z))
print("Minimum:", np.min(Z))
print("Index of Maximum:", np.argmax(Z))   
