import cv2

# Import image
image = cv2.imread('./images/img2.jpg')

# Apply median filter with kernel size 3x3
filtered_image = cv2.medianBlur(image,3)

# Concat both the images for better visual comparison
concat_image = cv2.hconcat([image,filtered_image])

# Display Image
cv2.imshow('Original VS. Median Filter Image',concat_image)
cv2.waitKey(0)
cv2.destroyAllWindows()