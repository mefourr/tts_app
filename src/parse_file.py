import pysrt


def get_file_lines(*, path: str) -> list:
    subs: pysrt.SubRipFile = pysrt.open(path)
    lines: list = [sub.text for sub in subs]
    return lines
