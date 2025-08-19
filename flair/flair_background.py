import flet as ft
import asyncio


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
        self.blur = blur

        self.image_current = ft.Image(src=image_src, fit=ft.ImageFit.FIT_HEIGHT)
        self.image_next = ft.Image(src="", fit=ft.ImageFit.FIT_HEIGHT, opacity=0)

        self.container_current = ft.Container(
            width=self.root.window.width,
            height=self.root.window.height,
            content=self.image_current,
            opacity=1.0
        )
        self.container_next = ft.Container(
            width=self.root.window.width,
            height=self.root.window.height,
            content=self.image_next,
            opacity=1.0
        )

        self.body = ft.Stack(
            controls=[
                self.container_current,
                self.container_next,
                ft.Container(
                    width=self.root.window.width,
                    height=self.root.window.height,
                    blur=ft.Blur(self.blur, self.blur)
                )
            ]
        )

    def get_body(self) -> ft.Container:
        return self.body

    async def change_image(self, new_image_src: str, duration_ms: int = 500, steps: int = 10):
        step_delay = duration_ms / steps / 1000

        self.image_next.src = new_image_src
        self.image_next.opacity = 0
        self.image_next.update()

        for i in range(steps):
            self.image_next.opacity = (i + 1) / steps
            self.image_next.update()
            await asyncio.sleep(step_delay)

        self.image_current.src = new_image_src
        self.image_current.update()

        self.image_next.opacity = 0
        self.image_next.update()
