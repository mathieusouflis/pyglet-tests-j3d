import pyglet
from pyglet.window import mouse


def main() -> None:
    class DragWindow(pyglet.window.Window):
        def __init__(self):
            super().__init__(800, 600, "Drag the cube")
            self.cube = pyglet.shapes.Rectangle(
                self.width // 2 - 50, self.height // 2 - 50, 200, 300, color=(255, 0, 0)
            )
            self.grab_offset = None

        def hit(self, x, y):
            c = self.cube
            return c.x <= x <= c.x + c.width and c.y <= y <= c.y + c.height

        def on_draw(self):
            self.clear()
            self.cube.draw()

        def on_mouse_press(self, x, y, button, modifiers):
            if button == mouse.LEFT and self.hit(x, y):
                self.grab_offset = (x - self.cube.x, y - self.cube.y)

        def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
            if self.grab_offset is not None:
                self.cube.x = x - self.grab_offset[0]
                self.cube.y = y - self.grab_offset[1]

        def on_mouse_release(self, x, y, button, modifiers):
            self.grab_offset = None

    DragWindow()
    pyglet.app.run()
