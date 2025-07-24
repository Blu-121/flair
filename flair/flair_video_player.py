import flet as ft


class FlairVideoPlayer:
    def __init__(
            self,
            root: ft.Page,
            playlist: list[ft.VideoMedia],
            width: int = 160,
            height: int = 90,
            pad_x: int = 0,
            pad_y: int = 0,
            loop: bool = True,
            muted: bool = False,
            show_player_ui: bool = False,
    ):
        self.root = root
        self.playlist = playlist
        self.width = width
        self.height = height
        self.pad_x = pad_x
        self.pad_y = pad_y
        self.loop = loop
        self.muted = muted
        self.show_player_ui = show_player_ui
        self.body = None

    def __build_player(self):
        try:
            self.body = ft.Container(
                content=ft.Column(
                    spacing=0,
                    width=self.width,
                    height=self.height,
                    controls=[
                        ft.Container(height=self.pad_y),
                        ft.Row(
                            width=self.width,
                            height=self.height,
                            spacing=0,
                            controls=[
                                ft.Container(width=self.pad_x),
                                ft.Video(
                                    playlist=self.playlist,
                                    width=self.width,
                                    height=self.height,
                                    playlist_mode=ft.PlaylistMode.LOOP if self.loop else ft.PlaylistMode.SINGLE,
                                    muted=self.muted,
                                    show_controls=self.show_player_ui,
                                )
                            ]
                        )
                    ]
                )
            )

        except Exception as e:
            print(f'error: {e}')
