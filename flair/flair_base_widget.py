import flet as ft
from .flair_widget_style import FlairWidgetStyle
import asyncio


class FlairBaseWidget:
    def __init__(
            self,
            master,
            width: int=200,
            height: int=200,
            abs_x: float= 0.0,
            abs_y: float=0.0,
            style: FlairWidgetStyle=FlairWidgetStyle(),
    ):
        self.master = master
        self.width = width
        self.height = height
        self.style = style
        self.abs_x = abs_x
        self.abs_y = abs_y

        self.body = ft.Stack()

    def build_widget(self, body):
        self.body = ft.Stack(
            [
                ft.Container(
                    width=self.width,
                    height=self.height,
                    bgcolor=(
                        self.style.bg_color if self.style.enable_bg # ->
                        else ft.Colors.TRANSPARENT
                    ),
                    blur=ft.Blur(self.style.blur_scale, self.style.blur_scale),
                    border_radius = self.style.border_radius,
                ),

                body
            ],
            width=self.width,
            height=self.height,
            top=self.abs_y,
            left=self.abs_x,
        )

    async def fade_out(self, duration: float = 200.0):
        steps = 50
        delay = duration / steps / 1000
        for i in range(steps + 1):
            self.body.opacity = 1 - (i / steps)
            await self.body.update_async()
            await asyncio.sleep(delay)

    async def fade_in(self, duration: float = 200.0):
        steps = 50
        delay = duration / steps / 1000
        for i in range(steps + 1):
            self.body.opacity = i / steps
            await self.body.update_async()
            await asyncio.sleep(delay)

    def get_body(self) -> ft.Stack | bool:
        try:
            return self.body
        except Exception as e:
            print(e)
            return False
