import flet as ft


def main(page: ft.Page):

    i1 = ft.Image(
        src="https://picsum.photos/200/300?1",
        animate_position=ft.animation.Animation(500, ft.AnimationCurve.EASE_OUT),
        left=0,
    )
    i2 = ft.Image(
        src="https://picsum.photos/200/300?2",
        animate_position=ft.animation.Animation(500, ft.AnimationCurve.EASE_OUT),
        left=-400,
    )
    i3 = ft.Image(
        src="https://picsum.photos/200/300?3",
        animate_position=ft.animation.Animation(500, ft.AnimationCurve.EASE_OUT),
        left=400,
    )


    def animate(e):
        if i1.left == 0 :
            i3.left = 0
            i1.left = -400
            i2.left = -800

        elif i2.left == 0 :
            i1.left = 0
            i2.left = -400
            i3.left = 400
        elif i3.left == 0 :
            i2.left = 0
            i1.left = 400
            i3.left = 800
        page.update()

    page.add(
        ft.Stack(
            [
                i1,
                i2,
                i3,
            ],
            width=200,
            height=300,
        ),
        ft.ElevatedButton("Slide!", on_click=animate),
    )


ft.app(target=main)