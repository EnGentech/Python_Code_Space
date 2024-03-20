import flet as ft
from time import sleep

def main(page: ft.Page):
    page.title = "Counter"

    text = ft.Text()
    page.add(text)

    for x in range(1, 11):
        text.value = f"Count: {x}"
        page.update()
        sleep(1)

ft.app(target=main, view=ft.WEB_BROWSER)
