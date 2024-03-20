import cv2

image = cv2.imread('galaxy.jpeg')
print(image.shape)

def calculate_size(scale_percentage, widht, height):
    new_widht = int(widht * scale_percentage / 100)
    new_height = int(height * scale_percentage / 100)
    return (new_widht, new_height )

def resize(image_path, scale_percentage, resize_path):
    image = cv2.imread(image_path)
    new_dim = calculate_size(scale_percentage, image.shape[1], image.shape[0])
    resize_image = cv2.resize(image, new_dim)
    cv2.imwrite(resize_path, resize_image)

resize('galaxy.jpeg', 50 , 'resize-galaxy.jpeg')