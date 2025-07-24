from dataclasses import dataclass

@dataclass(frozen=True)
class OnHoverEvent:
    ...

@dataclass(frozen=True)
class OnClickEvent:
    ...

@dataclass(frozen=True)
class AnimNotify:
    ON_CLICK: OnClickEvent = OnClickEvent
    ON_HOVER: OnHoverEvent = OnHoverEvent
