from load_image import ft_load
from matplotlib.pyplot import (
    imshow,
    figure,
    xticks,
    yticks,
    tight_layout,
    show
)
from numpy import array


def rotate_image(img_array, crop_size=400):
    """
    Cut a square part from the center of an image, convert to grayscale and
    transpose it.

    Args:
        img_array: numpy array of the image
        crop_size: size of the square region to extract (default 400)

    Returns:
        numpy array: cropped, grayscale and transposed image
    """
    height, width = img_array.shape[:2]
    start_y = (height - crop_size) // 2
    start_x = (width - crop_size) // 2
    end_y = start_y + crop_size
    end_x = start_x + crop_size

    cropped = img_array[start_y:end_y, start_x:end_x]

    cropped_gray = cropped[:, :, 0:1]

    gray_2d = cropped_gray.squeeze()

    rows, cols = gray_2d.shape
    transposed = [[gray_2d[j][i] for j in range(rows)] for i in range(cols)]

    transposed = array(transposed)

    return transposed


def display_image(image_array):
    """
    Display an image with axis scales using matplotlib.

    Args:
        image_array: numpy array of the image to display
    """
    figure(figsize=(10, 8))
    imshow(image_array, cmap="gray")

    xticks(range(0, image_array.shape[1], 50))
    yticks(range(0, image_array.shape[0], 50))
    tight_layout()
    show()


def main():
    """
    Main function that loads an image, crops it, converts to grayscale,
    transposes it and displays the result.
    """
    try:
        image_path = "animal.jpeg"
        img_array = ft_load(image_path)
        print(img_array)

        rotated_gray = rotate_image(img_array)

        print(f"New shape after Transpose: {rotated_gray.shape}")
        print(rotated_gray)

        display_image(rotated_gray)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
