import flet as ft


class FlairBackground:
    def __init__(
            self,
            root: ft.Page,
            bgcolor=ft.Colors.TRANSPARENT,
            blur: int = 0.0,
            image_src: str = None
    ):
        self.root = root
        self.bgcolor = bgcolor
        self.image_src = image_src
        self.blur = blur
        self.body = None

        self.__build_background()

    def __build_background(self):
        try:
            self.body = ft.Stack(
                controls=[
                    ft.Container(
                        width=self.root.window.width,
                        height=self.root.window.height,
                        content=ft.Image(src=self.image_src, fit=ft.ImageFit.FIT_HEIGHT),
                    ),
                    ft.Container(
                        width=self.root.window.width,
                        height=self.root.window.height,
                        blur=ft.Blur(self.blur, self.blur)
                    )
                ]
            )
        except Exception as e:
            print(f'error: {e}')

    def get_body(self) -> ft.Container | None:
        return self.body if self.body else None
