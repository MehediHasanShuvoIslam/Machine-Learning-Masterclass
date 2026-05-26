import numpy as np

house_prices = np.array([10000, 25000, 30000]) # 1D Array
bonus = 500 # Scalar (0D)

# NumPy নিজ থেকেই 500 কে ৩ বার স্ট্রেচ করে প্রতিটি ভ্যালুর সাথে যোগ করে দেবে
updated_prices = house_prices + bonus 
print("Updated Prices:", updated_prices)