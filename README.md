# Convertidor de Imágenes a Arte ASCII

> Convierte imágenes a arte ASCII con palestas de grises de 10 o 70 niveles 

## Características
- Compatible con formatos de imagen comunes como JPG y PNG.
- Ancho de salida ajustable (columnas).
- Factor de escala personalizable para controlar la relación de aspecto.
- Dos modos de escala de grises: 10 niveles (básico) y 70 niveles (detallado).

## Instalación

### Requisitos Previos
- Python 3.6 o superior
- Administrador de paquetes `pip`

### Instalación de Dependencias
Se recomienda crear un entorno virtual para evitar conflictos con otras bibliotecas.

#### Clonar el repositorio
```bash
git clone https://github.com/yourusername/image-to-ascii.git
cd image-to-ascii
```

#### Crear y activar un entorno virtual
```bash
# En Windows:
python -m venv .venv
.\.venv\Scripts\activate

# En macOS/Linux:
python -m venv .venv
source .venv/bin/activate
```

#### Instalar dependencias
```bash
pip install pillow numpy
```

## Uso
Para ejecutar el programa, usa el siguiente comando:
```bash
python ascii_art.py --file <ruta-de-la-imagen> [--cols <columnas>] [--scale <factor>] [--more]
```

### Argumentos
#### Obligatorios:
- `--file <ruta-de-la-imagen>`: Ruta al archivo de imagen de entrada.

#### Opcionales:
- `--cols <columnas>`: Número de columnas de ASCII en la salida (por defecto: 80).
- `--scale <factor>`: Factor de escala en altura para ajustar la proporción de aspecto (por defecto: 0.43).
- `--more`: Utiliza la escala de grises de 70 niveles en lugar de 10 niveles.

### Ejemplos
**Conversión básica (10 niveles):**
```bash
python ascii_art.py --file gato.jpg --cols 100
```

**Conversión detallada (70 niveles):**
```bash
python ascii_art.py --file paisaje.png --cols 120 --scale 0.5 --more
```

**Guardar la salida en un archivo:**
```bash
python ascii_art.py --file entrada.jpg --more > salida.txt
```

## Consejos de Configuración
Para obtener mejores resultados:
- Usa `--scale 0.5` para mantener una relación de aspecto cuadrada.
- Prueba con `--cols 80-120` para un tamaño óptimo en terminales estándar.
- Usa `--more` para mejorar la calidad en imágenes con texturas detalladas.
- Las imágenes con alto contraste ofrecen mejores resultados.
- Las imágenes a color se convierten automáticamente a escala de grises.
