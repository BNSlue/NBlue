import cv2
import numpy as np

# Load the input image
image = cv2.imread('road_image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform edge detection using Canny edge detector
edges = cv2.Canny(blurred, 50, 150)

# Define region of interest (ROI) for the lanes
mask = np.zeros_like(edges)
roi = np.array([[(0, 540), (800, 370), (800, 540), (400, 540)]], dtype=np.int32)
cv2.fillPoly(mask, roi, 255)
masked_edges = cv2.bitwise_and(edges, mask)

# Apply Hough Transform to detect lines
lines = cv2.HoughLinesP(masked_edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=50)

# Draw the detected lines on the original image
for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 3)

# Display the output image
cv2.imshow('Detected Lanes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
