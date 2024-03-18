from PIL import ImageFilter

def apply_filter(image, filter_type):
    """
    Applies the specified filter to the given image and returns the filtered image.
    
    Args:
        image (PIL.Image): The input image to which the filter will be applied.
        filter_type (str): The type of filter to be applied.
            Possible values: 'BLUR', 'CONTOUR', 'DETAIL', 'EDGE_ENHANCE', 'EDGE_ENHANCE_MORE', 'EMBOSS', 'FIND_EDGES', 'SHARPEN', 'SMOOTH', 'SMOOTH_MORE'.
        
    Returns:
        PIL.Image: The filtered image.
    """
    if filter_type not in ImageFilter.filters:
        raise ValueError(f"Invalid filter type: {filter_type}")
    
    return image.filter(filter_type)
