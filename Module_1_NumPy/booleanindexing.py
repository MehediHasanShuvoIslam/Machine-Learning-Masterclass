import numpy as np

# ডেমো ডেটা
sugar_levels = np.array([95, 130, 110, 150, 85, 125])

# ১. কন্ডিশন তৈরি করা (এটি একটি True/False অ্যারে রিটার্ন করবে)
high_sugar_mask = sugar_levels > 120

# ২. মাস্কটি মূল অ্যারেতে পাস করে ফিল্টার করা
diabetic_patients = sugar_levels[high_sugar_mask]

print("Condition Mask:", high_sugar_mask)
print("Filtered Data:", diabetic_patients)