import flet as ft

def main(page: ft.Page):
    """the function defines the main function for the execution"""
    page.title = "Hello page"

    text = ft.Text("Hello World, this is my first flet file")
    page.controls.append(text)
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)