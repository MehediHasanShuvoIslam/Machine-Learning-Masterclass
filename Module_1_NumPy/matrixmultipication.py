import numpy as np

# ইনপুট ম্যাট্রিক্স X (ধরি, ২টি স্যাম্পল, ৩টি ফিচার) -> Shape: (2, 3)
X = np.array([[1, 2, 3], 
              [4, 5, 6]])

# ওয়েট ম্যাট্রিক্স W (৩টি ফিচার, ১টি আউটপুট) -> Shape: (3, 1)
W = np.array([[0.1], 
              [0.2], 
              [0.3]])

# Dot Product Calculation
# X এর কলাম (3) এবং W এর সারি (3) সমান, তাই গুণন সম্ভব।
# আউটপুট ম্যাট্রিক্সের সাইজ হবে (2, 1)
Z = np.dot(X, W) # অথবা আপনি X @ W ও ব্যবহার করতে পারেন

print("Matrix X Shape:", X.shape)
print("Matrix W Shape:", W.shape)
print("Resulting Matrix Z:\n", Z)