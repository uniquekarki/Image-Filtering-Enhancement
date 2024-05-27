import cv2

image = cv2.imread('./images/img3.jpg')

bw_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equilized_image = cv2.equalizeHist(bw_image)


# Concat orginal and blurred image for better visual comparison
concat_img = cv2.hconcat([bw_image, equilized_image])

#Save Image
# cv2.imwrite('./images/histogram_equilization_output.jpg' ,concat_img)

# Display Image
cv2.imshow('Original Vs. Bilateral Blur Image',concat_img)
cv2.waitKey(0)
cv2.destroyAllWindows()