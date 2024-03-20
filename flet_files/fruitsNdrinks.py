import flet as ft

def main(page: ft.Page):
    page.title = "Rows$Columns"
    txt = ft.Text
    page.add(
        ft.Row(controls=[ft.Text("my favorite fruits:")]),
        ft.Row(
            controls=[
                txt('apple'),
                txt('mango'),
                txt('banana')
            ]
        ),
        ft.Column(controls=[ft.Text("\n\nmy favorite drinks:")]),
        ft.Column(
            controls=[
                txt('yoghurt'),
                txt('red wine'),
                txt('holandia')
            ]
        )
    )

ft.app(target=main, view=ft.WEB_BROWSER)