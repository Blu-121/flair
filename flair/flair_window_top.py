import flet as ft


class FlairWindowTop:
    def __init__(
            self,
            root: ft.Page,
            bg_color=ft.Colors.TRANSPARENT,
            blur: float = 0.0,
            debug: bool = False,
    ):
        self.root = root
        self.bg_color = bg_color
        self.blur = blur
        self.debug = debug
        self.root.window_title_bar_hidden=True

        self.body = ft.Stack(
            controls=[
                ft.Container(
                    width=self.root.window.width,
                    height=self.root.window.height-50,
                    bgcolor=self.bg_color,
                    blur=self.blur,
                ),
                ft.Container(
                    content=ft.WindowDragArea(
                        content=ft.Container(bgcolor=ft.Colors.YELLOW if self.debug else ft.Colors.TRANSPARENT),  # set color to debug WindowDragArea
                        height=40,
                        width=self.root.window.width,
                    ),
                    top=3.5, right=3.5
                ),
                ft.Container(
                    content=ft.IconButton(
                        icon=ft.Icons.CLOSE,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=6)),
                        on_click=lambda _: self.root.window.close()
                    ), right=3.5, top=3.5
                )
            ]
        )

    def get_body(self) -> ft.Container | None:
        return self.body if self.body else None
