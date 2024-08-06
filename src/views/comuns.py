import flet as ft


logo = ft.Image(src="/images/logo.png", width=300, height=300)
name = ft.TextField(hint_text="name", border="underline", height=60, width=200)
password = ft.TextField(hint_text="password", password=True, border="underline", can_reveal_password=True, height=60, width=200)
input = ft.TextField(hint_text="message", border="underline", height=60, width=200)
pr = ft.ProgressRing(width=50, height=50, stroke_width = 2)
error = ft.Text("Usuario no encontrado")