import flet as ft

def main(page: ft.Page):
    def on_pan_update1(e: ft.DragUpdateEvent):
        c.top = max(0, c.top + e.delta_y)
        c.left = max(0, c.left + e.delta_x)
        c.update()

    def on_pan_update_resize(e: ft.DragUpdateEvent):
        delta_x = e.delta_x
        delta_y = e.delta_y

        if e.control.data == "top_left":
            c.width = max(50, c.width - delta_x)
            c.height = max(50, c.height - delta_y)
            c.left = max(0, c.left + delta_x)
            c.top = max(0, c.top + delta_y)
        elif e.control.data == "top_right":
            c.width = max(50, c.width + delta_x)
            c.height = max(50, c.height - delta_y)
            c.top = max(0, c.top + delta_y)
        elif e.control.data == "bottom_left":
            c.width = max(50, c.width - delta_x)
            c.height = max(50, c.height + delta_y)
            c.left = max(0, c.left + delta_x)
        elif e.control.data == "bottom_right":
            c.width = max(50, c.width + delta_x)
            c.height = max(50, c.height + delta_y)

        c.update()

    def create_gd():
        return ft.Container(ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=10,
        on_pan_update=on_pan_update1,
    ), expand=90)
    gd_main = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=10,
        on_pan_update=on_pan_update1,
    )



    resize_gds = [
    ft.Container(
        ft.GestureDetector(
            mouse_cursor=(
                ft.MouseCursor.RESIZE_UP_LEFT if corner == "top_left" else
                ft.MouseCursor.RESIZE_UP_RIGHT if corner == "top_right" else
                ft.MouseCursor.RESIZE_DOWN_LEFT if corner == "bottom_left" else
                ft.MouseCursor.RESIZE_DOWN_RIGHT
            ),
            drag_interval=10,
            on_pan_update=on_pan_update_resize,
            content=ft.Container(bgcolor=ft.colors.TRANSPARENT, width=20, height=20),
            data=corner,
        ),
        expand=5
    )
    for corner in ["top_left", "top_right", "bottom_left", "bottom_right"]
]




    c_1st_row = ft.Row(controls=[resize_gds[0],create_gd(), resize_gds[1]], expand=5, spacing=0)
    c_2st_row = ft.Row(controls=[create_gd()], expand=90, spacing=0)
    c_3st_row = ft.Row(controls=[resize_gds[2],create_gd(), resize_gds[3]], expand=5, spacing=0)
    c_columns = ft.Column(controls=[c_1st_row,c_2st_row,c_3st_row], expand=1, spacing=0)
    c = ft.Container(
        c_columns,
        bgcolor=ft.colors.AMBER,
        width=200,
        height=200,
        left=0,
        top=0,
        padding=0,
        margin=0
    )

    page.add(ft.Stack([c], width=page.window.width, height=page.window.height))

ft.app(target=main)