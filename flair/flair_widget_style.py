from dataclasses import dataclass


@dataclass(frozen=False)
class FlairWidgetStyle:
    enable_bg: bool = False
    bg_color: str = '#FFFFFF'
    blur_scale: float = 30.0
    border_radius: int = 5
    border_color: str = '#FFFFFF'
