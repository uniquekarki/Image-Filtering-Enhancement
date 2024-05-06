import cv2

# Import image
img = cv2.imread('./images/taj.jpg')

# Apply bilateral blur to the imported image
bilateral_blur = cv2.bilateralFilter(img, 15, 75, 75)

# Concat orginal and blurred image for better visual comparison
concat_img = cv2.hconcat([img, bilateral_blur])

# Display Image
cv2.imshow('Original Vs. Bilateral Blur Image',concat_img)
cv2.waitKey(0)
cv2.destroyAllWindows()