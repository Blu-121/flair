import flet as ft


class FlairOverlay:
    def __init__(self, root: ft.Page, *widgets: tuple[int, ft.Control]):
        self.root = root
        self.widgets = widgets
        self.layers: dict[int, list[ft.Control]] = {}
        self.stack_elements: list[ft.Control] = []
        self.stack: ft.Stack | None = None

        self.__sort_widgets()

    def __sort_widgets(self):
        for key, control in self.widgets:
            if not isinstance(key, int):
                print(f"wrong key: {key}")
                continue

            if key not in self.layers:
                self.layers[key] = []

            self.layers[key].append(control)

        print(f"layers: {self.layers}")

    def place_widgets(self) -> ft.Stack:
        self.stack_elements.clear()

        for layer_index in sorted(self.layers.keys()):
            self.stack_elements.extend(self.layers[layer_index])

        self.stack = ft.Stack(controls=self.stack_elements)
        self.root.add(self.stack)

        print(f"added: {self.stack_elements}")
        return self.stack
