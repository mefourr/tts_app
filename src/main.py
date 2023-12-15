import os
from speechpro.cloud.speech import synthesis
from parse_file import get_file_lines


def main():
    lines: list = get_file_lines()

    сlient = synthesis.SynthesisClient()
    audio: bytes = 0

    make_dir()

    for index, line in enumerate(lines):
        audio = сlient.synthesize(
            synthesis.enums.Voice.CAROL, synthesis.enums.PlaybackProfile.SPEAKER, line
        )
        with open(f"./outputs/{index}_output.wav", "wb") as f:
            f.write(audio)


def make_dir():
    output_directory = "./outputs"
    is_dir_exists(output_directory)


def is_dir_exists(output_directory) -> None:
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)


if __name__ == "__main__":
    main()
