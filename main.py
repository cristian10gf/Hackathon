#from src.core.db.db import get_all_clients, get_all_projects, get_all_users, get_cliente, get_project, get_user
#from src.core.services.funcionalitys import get_response



#print(get_response(input("Ingrese su pregunta: ")))
import flet as ft











def main(page: ft.Page):
    page.title = "Text theme styles"
    page.horizontal_alignment=ft.MainAxisAlignment.CENTER
    page.window_height = 812
    page.window_width = 375
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row([
                    ft.Image(src=f"/images/logo.png",width=300,height=300),
                    ],
                           alignment= ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row([
                        
                    ft.Text("chat gpt",size=30,text_align=ft.TextAlign("center")),
                        
                    ],
                           alignment= ft.MainAxisAlignment.CENTER
                           ),
                    ft.Row([
                    ft.OutlinedButton("log in"),
                    ],        
                           alignment= ft.MainAxisAlignment.CENTER
                           ),
                    ft.Row([
                    ft.Text("or",size=15),
                    ],
                           alignment= ft.MainAxisAlignment.CENTER
                           ),
                    ft.Row([
                    ft.OutlinedButton("sign in")
                    ],
                           alignment= ft.MainAxisAlignment.CENTER
                           ),
                ],alignment=ft.MainAxisAlignment.END
            )
        )
    )
    



ft.app(main, assets_dir="assets")