import flet as ft









def main(page: ft.Page):
    page.title = "Text theme styles"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.window_height = 812
    page.window_width = 375
    page.add(
        ft.Container(ft.Column(
                controls=[
                    ft.Image(src=f"/images/logo.png",width=300,height=300),
                    ft.Text("chat gpt",size=30),
                    ft.OutlinedButton("log in"),
                    ft.Text("or",size=20),
                    ft.OutlinedButton("sign in")
                ],
            )
        )
    )


ft.app(main, assets_dir="assets")