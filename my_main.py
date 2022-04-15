"""my main"""

from my_game import *

info_ua = """\
Украї́на — держава, розташована в Східній Європі.
Ця чудова країна відома нам всім своєю багатою культурою
Але її спіткало горе.
На жаль, Україна має довбанутого сусіда - росію.
Отже, на нас лежить велика відповідальність!
Ми маємо знищити нашого ворога економічно і
допомогти ЗСУ зробити це ще й фізично.
Щоб це реалізувати, тобі потрібно домовитись про допомогу з різними країнами.
Нехай щастить!!!"""
info_us = """\
Сполу́чені Шта́ти Аме́рики — федеративна республіка, що складається з 50 штатів.
Від початку війни США нам помагала, але зараз морозиться і не хоче
дати сильну і потужну економічну і воєнну допомогу.
Знайди, як вламати дідуся Джо, щоб перемогти ту кляту росію!"""
info_uk = """\
Вели́ка Брита́нія - суверенна держава, розташована на Британських островах.
При владі цієї країни знаходиться Борис Джонсонюк
Вони теж нам помагають, але не достатньо.
Знайти, як вламати нашого кудрявого Бориса,
щоб перемогти ту кляту росію!"""
info_baltic = """\
Країни Балтії — країни, що омиваються Балтійським морем.
Вони лапочки і дуже нам помагають,
але нам все одно потрібна їхня допомога,
щоб перемогти ту кляту росію!"""
info_poland = """\
Респу́бліка По́льща — держава в Центральній Європі. 
Ця країна межує з нами на заході і дуже нам допомагає
Поляки ну дуже лапочки, але треба бляха ще допомоги,
щоб перемогти ту кляту росію!"""
info_belarus = """\
Респу́бліка Білору́сь — держава у Східній Європі без виходу до моря,
що межує з Україною на півдні.
Ще недавно ми навіть не підозрювали, що ця країна може нас так підставити.
Знайди те, що зможе зупинити вусатого диктатора помагати росії."""
info_russia = """\
>>> print('фекалії' == 'росія')
True
>>> print('багно' == 'росія')
True
>>> print('фашизм' == 'росія')
True
Отже, коротко росію ми описали. Все, що треба зробити, це зававити
росію економічно і військово.
Для цього тобі треба об'єднатись зі всіма дружніми країнами і переконати
тимчасово ворожі країни проти росії"""
info_zimbabwe = """\
Респу́бліка Зімба́бве — держава у Південній Африці.
Вона чомусь вирішила проголосувати за росію.
Знайди те, що зможе зупинити Зімба́бве помагати росії."""
info_china = """\
Кита́йська Наро́дна Респу́бліка — держава в Східній Азії.
Це економічно сильна комуністична країна, яка заграє з
росією і помагає їй.
Знайди те, що зможе зупинити Китай помагати росії."""
ukraine = Ukraine("Україна", info_ua)
ukraine.add_influence('інформація про звірства росіян')


usa = Friend("США", info_us)
usa.add_influence("javelin")
usa.add_influence("танки")
usa.add_influence("санкції")
usa.add_influence("fighter jet")
usa.add_weakness('permission for the usa')

uk = Friend("Велика Британія", info_uk)
uk.add_influence("permission for the usa")
uk.add_influence("санкції")
uk.add_influence("fighter jet")
uk.add_weakness('permission for the uk')

baltic = Friend("Країни Балтії", info_baltic)
baltic.add_influence("permission for the uk")
baltic.add_influence("санкції")
baltic.add_influence("javelin")
baltic.add_weakness('permission for baltic')

poland = Friend("Польща", info_poland)
poland.add_influence("permission for baltic")
poland.add_influence("банани")
poland.add_influence("танки")
poland.add_influence("санкції")
poland.add_weakness('інформація про звірства росіян')

belarus = Enemy("Білорусь", info_belarus)
belarus.add_weakness("бульба")
belarus.add_influence("fighter jet")
belarus.add_influence("танки")

russia = Superenemy("росія", info_russia)
russia.add_weakness(["javelin", "танки", "санкції", "fighter jet"])

zimbabwe = Enemy("Зімба́бве", info_zimbabwe)
zimbabwe.add_weakness("банани")
zimbabwe.add_influence("рис")

china = Enemy("Китай", info_china)
china.add_weakness("рис")
china.add_influence("бульба")
china.add_influence("санкції")

current_room = ukraine
backpack = []
all_counties = [usa, uk, baltic, poland, zimbabwe, china, belarus, russia, ukraine]
dead = False

menu = """
1 - Вибрати іншу країну
2 - Атакувати росію(автоматична зміна поточної держави)
3 - вибрати річ для дипломатії
4 - дізнатись в якій ми зараз країні
5 - завершити гру"""
print("Зараз ти, друже, в Україні")
print(current_room.info)
while dead == False:
    print(menu)
    command = input(">>> ")
    if command == "1":
        print("\nТи можеш вибрати, яку з цих країн:")
        for i in all_counties:
            print("* ", i.name)
        command = input(">>> ")
        new_county = False
        for i in all_counties:
            if i.name == command:
                current_room = i
                print(f"Зараз ти, друже, в {command}")
                print(current_room.info)
                new_county = True
        if not new_county:
            print("Нема такої країни спробуй знову")
    elif command == "3":
        part = ukraine.return_all()
        if part == "Україна ще не має дипломатичної зброї":
            print("Україна ще не має дипломатичної зброї")
        else:
            print(part)
            print("вибери зброю для дипломатії")
            command = input(">>> ")
            part = current_room.check_weakness(command)
            if part != None:
                ukraine.add_influence(part)
                ukraine.delete(command)
            else:
                print(f"Тобі не вдалось домовитись з {current_room.name}")
    elif command == "2":
        current_room = russia
        part = ukraine.return_all()
        if part == "Україна ще не має дипломатичної зброї":
            print("Україна ще не має дипломатичної зброї")
        else:
            print(part)
            print("вибери зброю для дипломатії")
            command = input(">>> ")
            part = ukraine.check_influence(command)
            if part:
                if command in current_room.weakness:
                    result = current_room.hit_enemy()
                    if result:
                        break
                    ukraine.delete(command)
                else:
                    print(f"{command} - це не зброя для росії(((")
            else:
                print("Щось пішло не так! Можливо, це неправильний ввід даних!")
    elif command == "4":
        print(current_room.name)
    elif command == "5":
        break
    else:
        print("Щось пішло не так. Спробуй знову")
