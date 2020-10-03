import base64
import pathlib
import imghdr
from pathvalidate import sanitize_filename, sanitize_filepath
import base64


def translate_name_to_filename(name: str = None):
    if name is not None:
        filename = name.lower().replace(" ", "_") + ".jpg"
        filename = sanitize_filename(filename)
        print(filename)
    else:
        filename = "error.png"

    return filename


def get_image_as_base64(name: str = None):

    if name is not None:
        filename = translate_name_to_filename(name)
        filepath = str(pathlib.Path.cwd().joinpath("static", "images", filename))
        image_path = pathlib.Path(filepath)
        print(image_path)
        if image_path.is_file() and imghdr.what(image_path) is not None:
            with open(image_path, "rb") as img_file:
                image_base64 = base64.b64encode(img_file.read()).decode("utf-8")
            return image_base64
        else:
            raise ValueError
    else:
        raise ValueError
