from PIL import Image, ImageDraw, ImageFont
def zad1():
    image = Image.open("otkr1.jpg")
    width, height = image.size
    new_image = image.crop((100,100,width - 100,height-100))
    new_image.save("redotkr1.png")
    new_image.show()

def zad2():
    holidays = {"День рождения": "deni.jpg", "Новый год": "newyeae.jpg", "Свадьба": "svad.jpg"}
    holiday = input("Какой праздник вам нужон? ")
    for day in holidays:
        if day == holiday:
            image = Image.open(holidays[day])
            image.show()
    name = str(input("Кого вы хотите поздравить? "))
    font = ImageFont.truetype('ofont.ru_Roboto.ttf', size=50)
    width, height = image.size
    draw_text = ImageDraw.Draw(image)
    draw_text.text(
        (width / 2, height / 2),
        name,
        font = font,
        fill = ("#FFFFFF")
        )
    font = ImageFont.truetype('ofont.ru_Roboto.ttf', size=50)
    draw_text = ImageDraw.Draw(image)
    draw_text.text(
        (width / 2 - 30, height / 2 + 50),
        ", поздравляю",
        font = font,
        fill = ("#F64141")
        )
    image.show()
    image.save("congratulation.png")

zad2()