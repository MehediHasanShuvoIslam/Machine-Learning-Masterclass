import numpy as np

# ইনপুট ম্যাট্রিক্স X
X = np.array([[80, 90, 70],
              [60, 75, 85],
              [95, 88, 92]])
# ওয়েট ম্যাট্রিক্স W
W = np.array([[0.3],
              [0.5],
              [0.2]])
# Dot Product Calculation
Z = np.dot(X, W)
print("Matrix X Shape:", X.shape)
print("Matrix W Shape:", W.shape)
print("Resulting Matrix Z:\n", Z)