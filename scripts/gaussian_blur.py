import cv2
image = cv2.imread('./images/img1.jpg')

# Define the desired width and height for the resized image
desired_width = 600  # Specify your desired width here
desired_height = 800  # Specify your desired height here

resized_image = cv2.resize(image, (desired_width, desired_height))

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(resized_image, (5, 5), 1.5)

# Concatenate images horizontally
concatenated_image = cv2.hconcat([resized_image, blurred_image])

# Display the concatenated image
cv2.imshow('Original and Blurred Images', concatenated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()