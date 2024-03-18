from PIL import Image

def resize_image(image_path, width, height):
    """
    Redimensiona uma imagem para as dimensões especificadas.

    Args:
        image_path (str): O caminho para a imagem.
        width (int): A largura desejada da imagem redimensionada.
        height (int): A altura desejada da imagem redimensionada.

    Returns:
        Image: A imagem redimensionada.
    """
    try:
        # Abrir a imagem
        img = Image.open(image_path)
        # Redimensionar a imagem
        resized_img = img.resize((width, height))
        return resized_img
    except Exception as e:
        print(f"Erro ao redimensionar a imagem: {e}")
        return None
