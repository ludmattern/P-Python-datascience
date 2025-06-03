from numpy import array
from matplotlib.pyplot import show, figure, imshow, title, axis


def _display_image(image_array: array, filter_title: str):
    """
    Utility function to display an image with a title.

    Args:
        image_array: numpy array representing the image
        filter_title: title to display above the image
    """
    figure(figsize=(8, 6))
    imshow(image_array)
    title(filter_title)
    axis("off")
    show()


def ft_invert(image_array: array) -> array:
    """
    Inverts the color of the image received.

    Args:
        image_array: numpy array representing the image

    Returns:
        array: inverted image array
    """
    inverted = 255 - image_array
    _display_image(inverted, "Inverted Filter")
    return inverted


def ft_red(image_array: array) -> array:
    """
    Applies a red filter to the image.

    Args:
        image_array: numpy array representing the image

    Returns:
        array: red filtered image array
    """
    red_filter = image_array.copy()
    red_filter[:, :, 1] = 0
    red_filter[:, :, 2] = 0
    _display_image(red_filter, "Red Filter")
    return red_filter


def ft_green(image_array: array) -> array:
    """
    Applies a green filter to the image.

    Args:
        image_array: numpy array representing the image

    Returns:
        array: green filtered image array
    """
    green_filter = image_array.copy()
    green_filter[:, :, 0] = 0
    green_filter[:, :, 2] = 0
    _display_image(green_filter, "Green Filter")
    return green_filter


def ft_blue(image_array: array) -> array:
    """
    Applies a blue filter to the image.

    Args:
        image_array: numpy array representing the image

    Returns:
        array: blue filtered image array
    """
    blue_filter = image_array.copy()
    blue_filter[:, :, 0] = 0
    blue_filter[:, :, 1] = 0
    _display_image(blue_filter, "Blue Filter")
    return blue_filter


def ft_grey(image_array: array) -> array:
    """
    Converts the image to grayscale.

    Args:
        image_array: numpy array representing the image

    Returns:
        array: grayscale image array
    """
    grey_filter = image_array.copy()
    grey_value = image_array[:, :, 1]
    grey_filter[:, :, 0] = grey_value
    grey_filter[:, :, 1] = grey_value
    grey_filter[:, :, 2] = grey_value
    _display_image(grey_filter, "Grey Filter")
    return grey_filter
