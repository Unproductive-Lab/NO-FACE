import flet as ft
from noface import *



def main(page: ft.Page):
    page.title = 'NOFACE'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width=700
    page.window.height=300
    page.window.resizable = False
    tb1 = ft.TextField(value='',text_align=ft.TextAlign.LEFT,width=300,hint_text="Кодируемая строка")
    tb2 = ft.TextField(read_only=True, value="")
    page.add(    (ft.Column(alignment=ft.MainAxisAlignment.END,controls=[
        ft.SafeArea(ft.Text("(CTRL+A, CTRL+C)",text_align=ft.TextAlign.CENTER)),
        tb2
    ])))
    def faceit(tb1):
        print("asdasdasd")
        tb2.value = makeface(tb1.value)
        tb2.update()
        page.update()
        #a = makeface({str(tb1.value)})    
    
    def defaceit(tb1):
        print("asdasdasd")
        tb2.value = deface(tb1.value)
        tb2.update()
        page.update()
        #a = makeface({str(tb1.value)})   
    
    page.add(ft.Row(spacing=100,controls=[
    (ft.Column(controls=[
        ft.SafeArea(ft.Text("1. Введите строку")),
        tb1
    ])),

    (ft.Column(controls=[
        ft.SafeArea(ft.Text("2. Нажмите кнопку ")),
        ft.OutlinedButton(text="NOFACE",on_click= lambda x: faceit(tb1)),
        ft.OutlinedButton(text="Расшифровать NOFACE",on_click= lambda x: defaceit(tb1))
    ]))




    ]))

    #page.add(ft.SafeArea(ft.Text("1. Введите кодируемую строку")))
    #page.add(ft.TextField(value='',text_align=ft.TextAlign.LEFT,width=300,hint_text="Кодируемая строка")) 

    
    page.update()



ft.app(main)
