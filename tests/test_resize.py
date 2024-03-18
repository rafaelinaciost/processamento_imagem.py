import unittest
from imageprocessing import resize

class TestResizeImage(unittest.TestCase):
    def test_resize_image(self):
        # Teste para verificar se a função redimensiona corretamente a imagem
        image_path = "teste_image.png"  # Caminho para a imagem
        width = 100
        height = 100
        resized_img = resize.resize_image(image_path, width, height)
        self.assertIsNotNone(resized_img)
        self.assertEqual(resized_img.size, (width, height))

if __name__ == "__main__":
    unittest.main()
