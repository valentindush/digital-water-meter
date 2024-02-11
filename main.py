import cv2
import pytesseract

# Path to the Tesseract OCR executable (adjust this based on your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load an image using OpenCV
image_path = 'path/to/your/photo.jpg'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use pytesseract to perform OCR on the grayscale image
text = pytesseract.image_to_string(gray_image)

# Print the extracted text
print("Extracted Text:")
print(text)
