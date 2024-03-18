from PIL import Image

def rotate_image(image, angle):
    """
    Rotates the given image by the specified angle (in degrees) and returns the rotated image.
    
    Args:
        image (PIL.Image): The input image to be rotated.
        angle (float): The angle of rotation in degrees.
        
    Returns:
        PIL.Image: The rotated image.
    """
    return image.rotate(angle)
