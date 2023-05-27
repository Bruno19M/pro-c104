import cv2

# Read the image file
img = cv2.imread("solar-system.jpg")

# Display the image
cv2.imshow("Output", img)
cv2.waitKey(0)

# Add text below each planet
cv2.putText(img, "Sol", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
cv2.putText(img, "Mercurio", (70, 213), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
cv2.putText(img, "Venus", (180, 213), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
cv2.putText(img, "Tierra", (270, 213), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
cv2.putText(img, "Marte", (370, 213), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
cv2.putText(img, "Jupiter", (550, 213), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
cv2.putText(img, "Saturno", (750, 213), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
cv2.putText(img, "Urano", (950, 213), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
cv2.putText(img, "Neptuno", (1100,213), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

# Display the image with added text
cv2.imshow("Output", img)
cv2.waitKey(0)

# Save the final image
cv2.imwrite("Solar_system_with_name.jpg", img)

# Execute the code
cv2.destroyAllWindows()