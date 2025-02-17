import argparse
from PIL import Image

def cargar_imagen (image_path): 
    return Image.open(image_path) 

def ajustar_imagen (image, new_width = 100): 
    width, height = image.size 
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.5)
    return image.resize((new_width, new_height), Image.Resampling.LANCZOS)

def convertir_ascii (image, ascii_chars): 
    """Convertimos la imagen a ASCII"""
    grayscale_image = image.convert('L')
    pixels = grayscale_image.getdata()
    ascii_str = ''
    for i, pixel in enumerate(pixels):
        if i % image.width == 0 and i != 0:
            ascii_str += '\n'
        scaled_pixel = pixel / 255
        index = int(scaled_pixel * (len(ascii_chars) - 1))
        ascii_str += ascii_chars[index]
    return ascii_str

def main(): 
    parser = argparse.ArgumentParser(description="Convierte imágenes a arte ASCII")
    parser.add_argument('--input', required=True, help='Dirección de la imagen')
    parser.add_argument('--output', 'Dirección del output ASCII') 
    parser.add_argument('--width', type=int, default=100, help='Anchura del output ASCII')
    parser.add_argument('--chars', default='@%#*+=-:. ', help='Caracteres ASCII de más oscuro a claro') 
    args = parser.parse_args()

    image = cargar_imagen(args.input) 
    image = ajustar_imagen(image, args.width) 
    arte_ascii = convertir_ascii(image, args.chars)  

    if args.output: 
        with open(args.output, 'w') as f: 
            f.write(arte_ascii) 
    else: 
        print(arte_ascii)

if __name__ == '__name__': 
    main()