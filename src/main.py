from ctypes import alignment
from decimal import Rounded
from turtle import window_height
import flet as ft
from flet_core.types import ThemeMode
from flet import TextField
from flet_core.control_event import ControlEvent
from requests import request


def main(page: ft.Page) -> None:
    page.title = "TTS App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ThemeMode.DARK
    page.window_height = int(200)
    page.window_width = int(400)
    launch_button = ft.Ref[ft.ElevatedButton]()
    file_path = ft.Ref[ft.TextField]()

    def btn_click(e: ControlEvent):
        if not file_path.current.value:
            file_path.current.error_text = "Enter the path"
            page.update()
        else:
            launch_button.current.disabled = True
            file_path.current.disabled = True
            page.update()

            go_request(path=file_path.current.value)
            file_path.current.focus()
            file_path.current.value = ""

            file_path.current.disabled = False
            launch_button.current.disabled = False
            page.update()

    page.add(
        ft.Row(
            [
                ft.TextField(
                    ref=file_path,
                    label="path/to/srt/file",
                    width=200,
                    opacity=50,
                    border_radius=10,
                    border_color="white",
                    autofocus=True,
                ),
                ft.ElevatedButton(ref=launch_button, text="Launch", on_click=btn_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


def go_request(path: str) -> None:
    request(path=path)


if "__main__" == __name__:
    ft.app(target=main)
