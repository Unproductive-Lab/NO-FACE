import flet as ft
# Я хотел изучить Флаттер
# Но мне отрезали нос
# И я расхотел

import sys
# Вы можете хотеть изменить переменные ниже, т.к. они являются важной частью достижения сохранности сообщения
BYTESHIFVALUE = 4
FACE = "NOFACE"
#Просто договоритесь с получателем об определенных настойках
def makeface(incode : bytes):
    res = ''
    chin = incode[len(incode)//2:]
    forehead = incode[:len(incode)//2]
    face = chin + forehead
    face = FACE.join(face[i:i+1] for i in range(0, len(face), 1)).encode("utf-8") 

    face = bin(int.from_bytes(face,byteorder=sys.byteorder)) 
    #face = bin(int.from_bytes(face,byteorder=sys.byteorder) >> BYTESHIFVALUE)  
    # ^^^ Этот вариант безопаснее, но может подхавать некоторые буквы. Используйте, если для вас безопасность важнее точности

    for k in range(len(face)):
        if face[k] == '0':
            res = res + 'NOFACE'
        elif face[k] == '1':
            res = res + 'NOFАCE'
        elif face[k] == 'b':
            res = res + ':'
    face = res

    face = (FACE * BYTESHIFVALUE) + face
    return face

def breakface(S, sub):
    i = 0
    while i < len(S):
        for e in sub:
            if S[i:].startswith(e):
                S = S[:i] + S[i+len(e):]
                i -= 1
                break
        else: i += 1
    return S

def deface(encoded : str):

    c = encoded.rpartition(':')[0].count(FACE)

    encoded = encoded[encoded.find(":")+1:]
    encoded = encoded.replace("NOFАCE","1")
    encoded = encoded.replace("NOFACE","0")
    en = int(encoded,2)
    #en = int(encoded,2) << c
    # ^^^ Этот вариант безопаснее, но может подхавать некоторые буквы. Используйте, если для вас безопасность важнее точности
    
    enc = en.to_bytes(len(encoded),byteorder=sys.byteorder) 
    enco = enc.decode("utf-8") 
    encod = breakface(enco,FACE).split('\x00', 1)[0]
    if len(encod) % 2 != 0:
        chin = encod[(len(encod)//2)+1:]
        forehead = encod[:(len(encod)//2)+1]
    else:
        chin = encod[len(encod)//2:]
        forehead = encod[:len(encod)//2]
    face = chin + forehead
    return face


# Бывает
def main(page: ft.Page):
    page.title = 'NOFACE'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width=700
    page.window.height=300
    page.window.resizable = False
    
    # tb это не террорблейд, а текстбокс
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
        # Ебаные лямбды я ваш хуй сосал почему вам надо давать аргумент, хотя когда
        # вы без аргумента, то вы жалуетесь что один есть вместо нуля... АААААА!!!! Пидоры!
    ]))

    ]))

    page.update()

ft.app(main)
