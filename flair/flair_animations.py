import flet as ft
from .flair_anim_notifys import *


class FlairAnimation:
    def __init__(
            self,
            notify,
            tracks: list[dict[str, tuple[str, int | float]]],
            curve: ft.AnimationCurve=ft.AnimationCurve.BOUNCE_OUT,
            duration: int=200,
    ):
        self.tracks = tracks
        self.curve = curve
        self.duration = duration
        self.notify = notify

        self.animation = {
            anim_property : value for track in tracks for anim_property, value in track.items()
        }

        self.animation_durations = {
            'animate_opacity' : ft.animation.Animation(self.duration, self.curve),
            'animate_rotation' : ft.animation.Animation(self.duration, self.curve),

        }

    def get_options(self) -> dict:
        return self.animation

    def get_durations(self) -> dict:
        return self.animation_durations

    def get_notify(self):
        return self.notify


class FadeOutAnimationClick(FlairAnimation):
    def __init__(self):
        self.notify = AnimNotify.ON_CLICK
        super().__init__(
            notify=self.notify,
            tracks=[
                {'opacity' : ('set', 0.0)}
            ],
            duration=300,
            curve=ft.AnimationCurve.EASE_OUT
        )


class FadeOutAnimationHover(FlairAnimation):
    def __init__(self):
        self.notify = AnimNotify.ON_HOVER
        super().__init__(
            notify=self.notify,
            tracks=[
                {'opacity' : ('set', 0.0)}
            ],
            duration=300,
            curve=ft.AnimationCurve.EASE_OUT
        )


class FadeInAnimationClick(FlairAnimation):
    def __init__(self):
        self.notify = AnimNotify.ON_CLICK
        super().__init__(
            notify=self.notify,
            tracks=[
                {'opacity' : ('set', 1.0)}
            ],
            duration=300,
            curve=ft.AnimationCurve.EASE_OUT
        )


class FadeInAnimationHover(FlairAnimation):
    def __init__(self):
        self.notify = AnimNotify.ON_HOVER
        super().__init__(
            notify=self.notify,
            tracks=[
                {'opacity' : ('set', 1.0)}
            ],
            duration=300,
            curve=ft.AnimationCurve.EASE_OUT
        )

