import numpy as np
import time

# ১টি বিশাল ডেটাসেট তৈরি (১ কোটি উপাদান)
size = 10_000_000

# Standard Python List
list1 = list(range(size))
list2 = list(range(size))

# NumPy Array
array1 = np.arange(size)
array2 = np.arange(size)

# ১. পাইথন লিস্টের মাধ্যমে যোগ করার সময় নির্ধারণ
start_time = time.time()
result_list = [x + y for x, y in zip(list1, list2)]
python_time = time.time() - start_time
print(f"Python List এর সময় লেগেছে: {python_time:.4f} সেকেন্ড")

# ২. NumPy Vectorization এর মাধ্যমে যোগ করার সময় নির্ধারণ (কোনো লুপ ছাড়া)
start_time = time.time()
result_array = array1 + array2
numpy_time = time.time() - start_time
print(f"NumPy Array এর সময় লেগেছে: {numpy_time:.4f} সেকেন্ড")

print(f"NumPy এই অপারেশনে {python_time / numpy_time:.2f} গুণ দ্রুত কাজ করেছে!")