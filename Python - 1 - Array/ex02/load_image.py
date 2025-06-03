from numpy import array
from PIL import Image


def ft_load(path: str) -> array:
    """
    Load an image and return its pixel content in RGB format.

    Args:
        path (str): Path to the image file

    Returns:
        array: Image data as numpy array

    Raises:
        Exception: If file doesn't exist, is not an image, or format not
        supported
    """
    try:
        if not path or not isinstance(path, str):
            raise Exception("Error: Invalid path provided")

        if "." not in path:
            raise Exception("Error: File has no extension")

        valid_extensions = [".jpg", ".jpeg", ".JPG", ".JPEG"]
        file_extension = path.lower().split(".")[-1]
        valid_lower = [ext.lower() for ext in valid_extensions]
        if f".{file_extension}" not in valid_lower:
            raise Exception("Error: Unsupported format. Only JPG and JPEG are supported")

        with Image.open(path) as img:
            if img.mode != "RGB":
                img = img.convert("RGB")

            image_array = array(img)

            print(f"The shape of image is: {image_array.shape}")

            return image_array

    except FileNotFoundError:
        raise Exception(f"Error: File '{path}' not found")
    except Exception as e:
        if "Error:" in str(e):
            raise e
        else:
            raise Exception(f"Error: Could not load image '{path}'. {str(e)}")
