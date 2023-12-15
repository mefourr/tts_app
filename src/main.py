import os
from speechpro.cloud.speech import synthesis
from parse_file import get_file_lines
from make_dir import make_dir 

def main() -> None:
    lines: list = get_file_lines()

    сlient: synthesis.SynthesisClient = synthesis.SynthesisClient()
    audio: bytes = 0

    dir: str = make_dir("./outputs")

    make_requests(lines, сlient, dir)

    os.system(f'explorer "{os.path.abspath(dir)}"')


def make_requests(lines: list, сlient: synthesis.SynthesisClient, dir: str) -> None:
    for index, line in enumerate(lines):
        audio = сlient.synthesize(
            synthesis.enums.Voice.CAROL, synthesis.enums.PlaybackProfile.SPEAKER, line
        )
        with open(f"{dir}/{index}_output.wav", "wb") as f:
            f.write(audio)


if __name__ == "__main__":
    main()
