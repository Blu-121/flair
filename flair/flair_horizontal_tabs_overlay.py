import flet as ft


class FlairHorizontalTabsOverlay:
    def __init__(
            self,
            root: ft.Page,
            tabs: list[ft.Tab],
            width: int = 200,
            height: int = 200,
            pad_x: int = 0,
            pad_y: int = 0,
            animation_duration: int = 250,
            show_custom_window_top: bool = False,
            window_top_height: int = 48,
            window_top_blur: ft.Blur = ft.Blur(40, 40),
            window_top_bg_color=ft.Colors.TRANSPARENT,
            window_top_enable_shadow: bool = False,
            window_top_border_color=ft.Colors.TRANSPARENT,
            tag: str = '<default_flair_tag>'
    ):
        self.root = root
        self.tabs = tabs
        self.show_custom_window_top = show_custom_window_top
        self.width = width
        self.height = height
        self.pad_x = pad_x
        self.pad_y = pad_y
        self.animation_duration = animation_duration
        self.window_top_height = window_top_height
        self.window_top_blur = window_top_blur
        self.window_top_bg_color = window_top_bg_color
        self.window_top_enable_shadow = window_top_enable_shadow
        self.window_top_border_color = window_top_border_color
        self.tag = tag
        self.body = None

        self.__build_widget()

    def __build_widget(self):
        try:
            self.root.window_title_bar_hidden = self.show_custom_window_top
            self.body = ft.Stack(
                controls=[
                    ft.Container(
                        width=self.width,
                        height=self.window_top_height,
                        bgcolor=self.window_top_bg_color,
                        shadow=ft.BoxShadow(spread_radius=3, blur_radius=15) if self.window_top_enable_shadow else None,
                        blur=self.window_top_blur,
                    ),
                    ft.Tabs(
                        tabs=self.tabs,
                        width=self.width,
                        height=self.height,
                        animation_duration=self.animation_duration,
                        selected_index=0,
                        divider_color=self.window_top_border_color,
                    ),
                    ft.Container(
                        content=ft.WindowDragArea(
                            content=ft.Container(bgcolor=ft.Colors.TRANSPARENT), #set color to debug WindowDragArea
                            width=self.width - (len(self.tabs)*75),
                            height=40
                        ) if self.show_custom_window_top else None,
                        top=3.5, right=3.5
                    ),
                    ft.Container(
                        content=ft.IconButton(
                            icon=ft.Icons.CLOSE,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=6)),
                            on_click=lambda _: self.root.window.close()
                        ) if self.show_custom_window_top else None, right=3.5, top=3.5
                    )
                ]
            )
        except Exception as e:
            print(f'error: {e}')

    def get_body(self) -> ft.Container | None:
        return self.body if self.body else None
