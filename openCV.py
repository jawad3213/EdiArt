import cv2
import numpy as np

def grayscale(img):
    """Convert image to grayscale."""
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def blur(img, kernel_size=(15,15)):
    """Apply Gaussian blur to image."""
    return cv2.GaussianBlur(img, kernel_size, 0)

def edge_detection(img, thresholds=[100,200]):
    """Detect edges using Canny algorithm."""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.Canny(gray, thresholds[0], thresholds[1])

def pixelation(img, pixel_size=10):
    """Pixelate the image."""
    h, w = img.shape[:2]
    # Reduce image size
    small = cv2.resize(img, (w//pixel_size, h//pixel_size), 
                       interpolation=cv2.INTER_LINEAR)
    # Scale back up
    return cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)

def cartoon(img):
    """Create a cartoon-like effect."""
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply median blur
    gray = cv2.medianBlur(gray, 5)
    
    # Detect edges
    edges = cv2.adaptiveThreshold(gray, 255, 
                                  cv2.ADAPTIVE_THRESH_MEAN_C, 
                                  cv2.THRESH_BINARY, 9, 9)
    
    # Color quantization
    color = cv2.pyrMeanShiftFiltering(img, 9, 50)
    
    # Combine color image with edges
    return cv2.bitwise_and(color, color, mask=edges)

def oil_painting(img, mask_size=3):
    """Simulate an oil painting effect."""
    # Convert to float for processing
    img_float = img.astype(np.float32) / 255.0
    
    # Apply bilateral filter for smooth effect
    filtered = cv2.bilateralFilter(img, 9, 75, 75)
    
    return (filtered * 255).astype(np.uint8)

def emboss(img):
    """Create an emboss effect."""
    # Kernel for emboss effect
    kernel = np.array([
        [-2, -1, 0],
        [-1,  1, 1],
        [ 0,  1, 2]
    ])
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply convolution
    embossed = cv2.filter2D(gray, -1, kernel)
    
    return embossed

def invert(img):
    """Invert image colors."""
    return 255 - img

def sepia(img):
    """Apply sepia tone to image."""
    # Sepia kernel
    kernel = np.array([
        [0.272, 0.534, 0.131],
        [0.349, 0.686, 0.168], 
        [0.393, 0.769, 0.189]
    ])
    
    # Convert image to float
    img_float = img.astype(np.float32) / 255.0
    
    # Apply sepia transformation
    sepia_img = cv2.transform(img_float, kernel)
    
    # Clip values and convert back to uint8
    sepia_img = np.clip(sepia_img * 255, 0, 255).astype(np.uint8)
    
    return sepia_img