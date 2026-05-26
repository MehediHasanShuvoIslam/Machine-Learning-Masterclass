import numpy as np
# ক্লাসিফিকেশন মডেলের আউটপুট প্রবাবিলিটি (৩টি ক্লাস: Cat, Dog, Bird)
probabilities = np.array([0.1, 0.8, 0.1])

# কোন ক্লাসের প্রবাবিলিটি সবচেয়ে বেশি?
predicted_class_index = np.argmax(probabilities)

print(f"মডেল প্রেডিক্ট করেছে ক্লাস ইনডেক্স: {predicted_class_index}") # আউটপুট হবে 1 (Dog)