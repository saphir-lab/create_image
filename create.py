import cv2
import numpy

# opencv is using BGR for the color notation, so Blue, Green, Red (instead of RGB)
a = numpy.array(
    [
      [
        [255, 0, 0],        # Blue
        [255, 255, 255],    # White
        [187, 41, 160],     # Purple
        [255, 255, 255]     # White
      ],
      [
        [255, 255, 255],    # White
        [0, 0, 255],        # Red
        [255, 255, 255],    # White
        [255, 255, 255]     # White
      ],    
      [
        [0, 0, 0],          # Black
        [47, 255, 173],     # Light Green
        [255, 255, 255],    # White
        [0, 255, 0]         # Green
      ]
    ]
)

cv2.imwrite('image.png', a)