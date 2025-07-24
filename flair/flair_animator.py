import flet as ft
from . import flair_anim_notifys


class FlairAnimator:
    def __init__(self, animation, click_action=lambda e: None, hover_action=lambda e: None, enable_flip_flopping=False):
        self.animation = animation
        self.__on_click_action = None
        self.__on_hover_action = None
        self.instance = None
        self.body = ft.Container()
        self.click_action = click_action
        self.hover_action = hover_action
        self.enable_flip_flopping = enable_flip_flopping
        self.original_props = {}
        self.flipped = False

    def set_main_actions(self, body: ft.Container):
        self.__on_click_action = self.click_action
        self.__on_hover_action = self.hover_action
        self.body = body

    def set_animation_actions(self):
        if self.animation.get_notify() == flair_anim_notifys.OnClickEvent:
            def on_click(e):
                props = self.animation.get_options()

                if not self.original_props:
                    self.original_props = {prop: getattr(self.body, prop) for prop in props}

                if self.enable_flip_flopping:
                    if not self.flipped:
                        for prop, (op, val) in props.items():
                            current = getattr(self.body, prop)
                            if op == "add":
                                setattr(self.body, prop, current + val)
                            elif op == "set":
                                setattr(self.body, prop, val)

                        self.flipped = True
                    else:
                        for prop in props:
                            setattr(self.body, prop, self.original_props[prop])
                        self.flipped = False

                    self.body.update()

                else:
                    for prop, (op, val) in props.items():
                        current = getattr(self.body, prop)
                        if op == "add":
                            setattr(self.body, prop, current + val)
                        elif op == "set":
                            setattr(self.body, prop, val)

                    self.body.update()

                self.__on_click_action(e)

            self.instance.content.on_click = on_click

        if self.animation.get_notify() == flair_anim_notifys.OnHoverEvent:
            def on_hover(e):
                props = self.animation.get_options()

                if not self.original_props:
                    self.original_props = {prop: getattr(self.body, prop) for prop in props}

                if self.enable_flip_flopping:
                    if not self.flipped:
                        for prop, (op, val) in props.items():
                            current = getattr(self.body, prop)
                            if op == "add":
                                setattr(self.body, prop, current + val)
                            elif op == "set":
                                setattr(self.body, prop, val)

                        self.flipped = True
                    else:
                        for prop in props:
                            setattr(self.body, prop, self.original_props[prop])
                        self.flipped = False

                    self.body.update()

                else:
                    for prop, (op, val) in props.items():
                        current = getattr(self.body, prop)
                        if op == "add":
                            setattr(self.body, prop, current + val)
                        elif op == "set":
                            setattr(self.body, prop, val)

                    self.body.update()

                self.__on_click_action(e)

            self.instance.content.on_click = on_hover

            self.instance.content.on_hover = on_hover

    def apply_durations(self):
        for track, duration in self.animation.get_durations().items():
            setattr(self.body, track, duration)

    def __call__(self, widget):
        def wrapper(*args, **kwargs):
            self.instance = widget(*args, **kwargs)
            self.set_main_actions(self.instance.content)
            self.apply_durations()
            self.set_animation_actions()
            return self.instance

        return wrapper
