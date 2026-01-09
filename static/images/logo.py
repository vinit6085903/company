import cv2
import numpy as np
import os

IMAGE_PATH = r"C:\Users\Dell\OneDrive\Desktop\sidhu\company\logo_clean.png"

# Check file exists
if not os.path.exists(IMAGE_PATH):
    raise FileNotFoundError("❌ Image file not found. Check path & name.")

# Load image
img = cv2.imread(IMAGE_PATH)

if img is None:
    raise ValueError("❌ Image could not be loaded. Corrupt or unsupported format.")

# Resize
img = cv2.resize(img, (800, 800))

# Convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Edge detection
edges = cv2.Canny(blur, 50, 150)

# Threshold
_, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV)

# Combine
mask = cv2.bitwise_or(edges, thresh)

# Morphology
kernel = np.ones((3, 3), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# Create transparent logo
b, g, r = cv2.split(img)
alpha = mask
logo = cv2.merge([b, g, r, alpha])

# Save output
cv2.imwrite("logo_output.png", logo)

print("✅ Logo converted successfully")
