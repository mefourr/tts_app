import os


def make_dir(output_dir: str) -> str:
    is_dir_exists(output_dir)
    return output_dir


def is_dir_exists(output_directory: str) -> None:
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
