from load_image import ft_load
from matplotlib.pyplot import (
    imshow,
    figure,
    xticks,
    yticks,
    tight_layout,
    show
)


def zoom_image(img_array, zoom_size=400):
    """
    Zoom on the center of an image and convert to grayscale.

    Args:
        img_array: numpy array of the image
        zoom_size: size of the square region to extract (default 400)

    Returns:
        numpy array: zoomed and grayscale image
    """
    height, width = img_array.shape[:2]
    start_y = (height - zoom_size) // 2
    start_x = (width - zoom_size) // 2
    end_y = start_y + zoom_size
    end_x = start_x + zoom_size

    zoomed = img_array[start_y:end_y, start_x:end_x]

    zoomed_gray = zoomed[:, :, 0:1]

    return zoomed_gray


def display_image(image_array):
    """
    Display an image with axis scales using matplotlib.

    Args:
        image_array: numpy array of the image to display
        title: title for the plot
    """
    figure(figsize=(10, 8))
    imshow(image_array.squeeze(), cmap="gray")

    xticks(range(0, image_array.shape[1], 50))
    yticks(range(0, image_array.shape[0], 50))
    tight_layout()
    show()


def main():
    """
    Main function that loads an image, displays information about it,
    performs zooming, and displays the result.
    """
    try:
        image_path = "animal.jpeg"
        img_array = ft_load(image_path)

        zoomed_gray = zoom_image(img_array)

        print(
            f"New shape after slicing: {zoomed_gray.shape}"
            f" or {zoomed_gray.shape[:2]}"
            )
        print(zoomed_gray)

        display_image(zoomed_gray)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
