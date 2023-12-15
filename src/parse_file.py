import pysrt


def get_file_lines() -> list:
    
    file_name: str = "script.srt"
    subs: pysrt.SubRipFile = pysrt.open(file_name)
    lines: list = [sub.text for sub in subs]
    
    return lines
