from PIL import Image
import os, random
import json

# image configurations
sizes = [(128, 128), (256, 256), (512, 512), (1024, 1024), (2000, 2000), (3000, 3000)]
formats = ['jpg', 'jpeg', 'png']
qualities = [30, 50, 70, 90]

# image directories
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(ROOT_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
for fmt in formats:
    os.makedirs(os.path.join(DATA_DIR, fmt), exist_ok=True)

# file paths configuration
file_paths = {"jpeg": [], "png": [], "jpg": []}
FILE_PATHS_JSON = os.path.join(DATA_DIR, "file_paths.json")
print(f"File paths will be saved to: {FILE_PATHS_JSON}")


def create_random_image(width, height):
    """
    Create a random noise image with the given width and height    
    """
    image = Image.new("RGB", (width, height))
    pixels = image.load()
    for i in range(width):
        for j in range(height):
            pixels[i, j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return image


def check_file_size(filepath):
    """
    Check the file size of the given file path\n
    Return the file size in MB
    """
    size_in_mb = os.path.getsize(filepath) / (1024 * 1024)
    return size_in_mb


def main() -> None:
    for size in sizes:
        for fmt in formats:
            img = create_random_image(size[0], size[1])
            filename = f"image_{size[0]}x{size[1]}"
            if fmt in ['jpg', 'jpeg']:
                for quality in qualities:
                    file_path = f"{DATA_DIR}/{fmt}/{filename}_{quality}.{fmt}"
                    img.save(file_path, quality=quality)
                    relative_file_path = file_path.replace(DATA_DIR + "/", "")
                    print(f"File: {relative_file_path} - Size: {check_file_size(file_path)} MB")
                    file_paths[fmt].append(file_path)
            else:
                file_path = f"{DATA_DIR}/{fmt}/{filename}.{fmt}"
                img.save(file_path)
                relative_file_path = file_path.replace(DATA_DIR + "/", "")
                print(f"File: {relative_file_path} - Size: {check_file_size(file_path)} MB")
                file_paths[fmt].append(relative_file_path)

    with open(FILE_PATHS_JSON, "w") as file:
        json.dump(file_paths, file)


if __name__ == "__main__":
    main()
