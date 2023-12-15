from ctypes import alignment
from decimal import Rounded
from turtle import window_height
import flet as ft
from flet import TextField
from flet_core.control_event import ControlEvent
from requests import request


def main(page: ft.Page) -> None:
    page.title = "TTS App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = "Dark"

    page.window_height = 200
    page.window_width = 400

    file_path = TextField(
        hint_text="path/to/srt/file",
        text_align=ft.TextAlign.CENTER,
        width=200,
        opacity=50,
        border_radius=50,
        border_color="white",
    )

    def btn_click(e: ControlEvent):
        if not file_path.value:
            file_path.error_text = "enter the path"
            page.update()
        else:
            go_request(path=file_path.value)

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Launch",
                    on_click=btn_click,
                    width=100,
                    height=55,
                ),
                file_path,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


def go_request(path: str) -> None:
    request(path=path)


if "__main__" == __name__:
    ft.app(target=main)
