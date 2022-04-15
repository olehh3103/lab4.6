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

usa = Friend("США", info_us)
usa.add_influence("javelin")
usa.add_influence("танки")
usa.add_influence("санкції")
usa.add_influence("fighter jet")

uk = Friend("Великобританія", info_uk)
uk.add_influence("permission for the usa")
uk.add_influence("санкції")
uk.add_influence("fighter jet")

baltic = Friend("Країни Балтії", info_baltic)
baltic.add_influence("permission for the uk")
baltic.add_influence("санкції")
baltic.add_influence("javelin")

poland = Friend("Польща", info_poland)
poland.add_influence("permission for baltic")
poland.add_influence("bananas")
poland.add_influence("танки")
poland.add_influence("санкції")

belarus = Enemy("Білорусь", info_belarus)
belarus.add_weakness("бульба")
belarus.add_influence("fighter jet")
belarus.add_influence("танки")

russia = Superenemy("росія", info_russia)
russia.add_weakness({"Javelin":2, "танки":3, "санкції":5, "fighter jet":3})

zimbabwe = Enemy("Зімба́бве", info_zimbabwe)
zimbabwe.add_weakness("банани")
zimbabwe.add_influence("рис")

china = Enemy("Китай", info_china)
china.add_weakness("рис")
china.add_influence("бульба")
china.add_influence("санкції")

current_room = ukraine
backpack = []
all = [usa, uk, baltic, poland, zimbabwe, china, belarus, russia, ukraine]
dead = False

while dead == False:

    print(current_room.info)
    print("\nТи можеш вибрати, яку з цих країн:")
    for i in all:
        print("* ", i.name)
    command = input(">>> ")
    for i in all:
        if i.name == command:
            
                # inhabitant = current_room.get_character()
                # if inhabitant is not None:
                #     inhabitant.describe()

                # item = current_room.get_item()
                # if item is not None:
                #     item.describe()

                # command = input("> ")

                # if command in ["north", "south", "east", "west"]:
                #     # Move in the given direction
                #     current_room = current_room.move(command)
                # elif command == "talk":
                #     # Talk to the inhabitant - check whether there is one!
                #     if inhabitant is not None:
                #         inhabitant.talk()
                # elif command == "fight":
                #     if inhabitant is not None:
                #         # Fight with the inhabitant, if there is one
                #         print("What will you fight with?")
                #         fight_with = input()

                #         # Do I have this item?
                #         if fight_with in backpack:

                #             if inhabitant.fight(fight_with) == True:
                #                 # What happens if you win?
                #                 print("Hooray, you won the fight!")
                #                 current_room.character = None
                #                 if inhabitant.get_defeated() == 2:
                #                     print("Congratulations, you have vanquished the enemy horde!")
                #                     dead = True
                #             else:
                #                 # What happens if you lose?
                #                 print("Oh dear, you lost the fight.")
                #                 print("That's the end of the game")
                #                 dead = True
                #         else:
                #             print("You don't have a " + fight_with)
                #     else:
                #         print("There is no one here to fight with")
                # elif command == "take":
                #     if item is not None:
                #         print("You put the " + item.get_name() + " in your backpack")
                #         backpack.append(item.get_name())
                #         current_room.set_item(None)
                #     else:
                #         print("There's nothing here to take!")
                # else:
                #     print("I don't know how to " + command)

# kitchen = game.Room("Kitchen")
# kitchen.set_description("A dank and dirty room buzzing with flies.")

# dining_hall = game.Room("Dining Hall")
# dining_hall.set_description("A large room with ornate golden decorations on each wall.")

# ballroom = game.Room("Ballroom")
# ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

# kitchen.link_room(dining_hall, "south")
# dining_hall.link_room(kitchen, "north")
# dining_hall.link_room(ballroom, "west")
# ballroom.link_room(dining_hall, "east")

# dave = game.Enemy("Dave", "A smelly zombie")
# dave.set_conversation("What's up, dude! I'm hungry.")
# dave.set_weakness("cheese")
# dining_hall.set_character(dave)

# tabitha = game.Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
# tabitha.set_conversation("Sssss....I'm so bored...")
# tabitha.set_weakness("book")
# ballroom.set_character(tabitha)

# cheese = game.Item("cheese")
# cheese.set_description("A large and smelly block of cheese")
# ballroom.set_item(cheese)

# book = game.Item("book")
# book.set_description("A really good book entitled 'Knitting for dummies'")
# dining_hall.set_item(book)

# current_room = kitchen
# backpack = []

# dead = False

# while dead == False:

#     print("\n")
#     current_room.get_details()

#     inhabitant = current_room.get_character()
#     if inhabitant is not None:
#         inhabitant.describe()

#     item = current_room.get_item()
#     if item is not None:
#         item.describe()

#     command = input("> ")

#     if command in ["north", "south", "east", "west"]:
#         # Move in the given direction
#         current_room = current_room.move(command)
#     elif command == "talk":
#         # Talk to the inhabitant - check whether there is one!
#         if inhabitant is not None:
#             inhabitant.talk()
#     elif command == "fight":
#         if inhabitant is not None:
#             # Fight with the inhabitant, if there is one
#             print("What will you fight with?")
#             fight_with = input()

#             # Do I have this item?
#             if fight_with in backpack:

#                 if inhabitant.fight(fight_with) == True:
#                     # What happens if you win?
#                     print("Hooray, you won the fight!")
#                     current_room.character = None
#                     if inhabitant.get_defeated() == 2:
#                         print("Congratulations, you have vanquished the enemy horde!")
#                         dead = True
#                 else:
#                     # What happens if you lose?
#                     print("Oh dear, you lost the fight.")
#                     print("That's the end of the game")
#                     dead = True
#             else:
#                 print("You don't have a " + fight_with)
#         else:
#             print("There is no one here to fight with")
#     elif command == "take":
#         if item is not None:
#             print("You put the " + item.get_name() + " in your backpack")
#             backpack.append(item.get_name())
#             current_room.set_item(None)
#         else:
#             print("There's nothing here to take!")
#     else:
#         print("I don't know how to " + command)