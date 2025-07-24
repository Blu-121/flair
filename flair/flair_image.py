from flair_base_widget import FlairBaseWidget, FlairWidgetStyle
import flet as ft
import asyncio


class FlairImage(FlairBaseWidget):
    def __init__(
            self,
            master: ft.Page,
            image_src: str = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYz8zEAFyjZKTNeQW-MRagzdrD-bTFpArsiA&s',
            width: int = 160,
            height: int = 90,
            abs_x: float = 0,
            abs_y: float = 0,
            style: FlairWidgetStyle = FlairWidgetStyle(enable_bg=False, blur_scale=0.0)
    ):
        self.master = master
        self.image_src = image_src
        self.width = width
        self.height = height
        self.abs_x = abs_x
        self.abs_y = abs_y
        self.style = style
        self.bg_image_src = self.image_src

        super().__init__(
            self.master,
            self.width,
            self.height,
            style=FlairWidgetStyle(enable_bg=False, blur_scale=0.0),
            abs_x=self.abs_x,
            abs_y=self.abs_y
        )

        self.image = ft.Image(
            src=self.image_src,
            width=self.width,
            height=self.height,
            fit=ft.ImageFit.FILL,
        )

        self.next_image = ft.Image(
            src=self.bg_image_src,
            width=self.width,
            height=self.height,
            fit=ft.ImageFit.FILL,
        )

        self.image_current = ft.Container(
            content=self.image,
            blur=ft.Blur(self.style.blur_scale, self.style.blur_scale),
            border_radius=self.style.border_radius,
        )
        self.image_next = ft.Container(
            content=self.next_image,
            blur=ft.Blur(self.style.blur_scale, self.style.blur_scale),
            border_radius=self.style.border_radius,
            opacity=0.0
        )

        self.body = ft.Stack(
            [
                self.image_current,
                self.image_next
            ]
        )

        self.build_widget(self.body)

    async def change_image(self, new_src: str, apply_blend: bool=False, anim_duration: float=200.0):
        if not apply_blend:
            await self.fade_out(anim_duration)
            self.image.src = new_src
            await self.image.update_async()
            await self.body.update_async()

            await self.fade_in(anim_duration)
        else:
            self.next_image.src = new_src
            await self.next_image.update_async()
            await self.body.update_async()
            steps = 50
            delay = anim_duration / steps / 1000
            for i in range(steps + 1):
                self.image_current.opacity = 1 - (i / steps)
                self.image_next.opacity = (i / steps)
                await self.image_next.update_async()
                await self.image_current.update_async()
                await self.body.update_async()
                await asyncio.sleep(delay)
