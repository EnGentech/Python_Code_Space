import flet as ft

txt = ft.Text
cin = ft.TextField
btn = ft.ElevatedButton
chk = ft.Checkbox

def main(page: ft.Page):
    page.title = 'ToDo List'
    input_text = cin(hint_text="Add to do list", width=300)
    page.theme_mode = "light"
    def update(e):
        page.add(chk(label=input_text.value))

    page.add(
        ft.Row(
            controls=[
                input_text,
                btn(text='Add', on_click=update)
            ]
        )
    )
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)