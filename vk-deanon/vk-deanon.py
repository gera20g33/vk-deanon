import webbrowser
import time
from colorama import init
from colorama import Fore, Back, Style
init()
#=======================================
banner=Fore.RED+"""
██████╗ ███████╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗
██╔══██╗██╔════╝██╔══██╗████╗  ██║██╔═══██╗████╗  ██║
██║  ██║█████╗  ███████║██╔██╗ ██║██║   ██║██╔██╗ ██║
██║  ██║██╔══╝  ██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║
██████╔╝███████╗██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║
╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝
by Dizzzackl
"""
print(banner)
print('\033[39m')
#=======================================
menu1=Fore.WHITE+"""
[1]начать deanon
"""
menu2=Fore.BLUE+"""
[2]информация
"""
menu3=Fore.RED+"""
[3]выход
"""
print(menu1)
print(menu2)
print(menu3)
print('\033[39m')
vibor = input(Fore.YELLOW+"select->")
print('\033[39m')
#=======================================
if vibor=='1':
    print(Fore.WHITE+'ну чтож начнём..')
    print(Fore.BLUE+'обновление данных....')
    time.sleep(2.4)
    print(Fore.RED+'данные обновленные погнали')
    print('\033[39m')
    yn=input('ты знаешь вк своего обидчика :')
    if yn == "да":
        print("в папке есть шаблон для данных")
        print('порошу все данные зпписывать в него ')
        print(Fore.WHITE+'тогда начнём')
        vk = input(Fore.BLUE+'укажи ссылку на вк своего обидчика->')
        webbrowser.open(vk)
        print(Fore.WHITE+'сканирую вк.....')
        time.sleep(2.4)
        print(Fore.BLUE+'его данные сохранены в мой регистер')
        print(Fore.RED+'узнай его id я сейчас открою сайт для этого ')
        time.sleep(2.4)
        webbrowser.open('https://regvk.com/id/')
        vkid = input(Fore.WHITE+'введи его id->')
        print(Fore.BLUE+'теперь узнаем его базовые данные')
        print(Fore.RED+'туда надо ввести ссылку на его акк')
        webbrowser.open('https://vk.com/app7183114')
        print(Fore.WHITE+'тепрь узнаем остальную инфу про его страницу')
        webbrowser.open(f'https://top100vk.com/{vkid}/')
        print(Fore.BLUE+'через минут откроються тг боты')
        time.sleep(60)
        print(Fore.WHITE+'теперь пришло время тг ботов')
        webbrowser.open('https://t.me/InfoVkUser_bot')
        webbrowser.open('https://t.me/FindNameVk_bot')
        webbrowser.open('https://t.me/GetPhone_bot')
        print(Fore.WHITE+'всё поздравляю ты достал базовую инфу о нём')
        print(Fore.BLUE+'напомню инфу о нём:' , vk , vkid)
        input(Fore.RED+'нажми ENTER чтобы выйти')
        print('\033[39m')
    if yn == "нет":
        print('тогда купи приватку в моём тг канале')
        webbrowser.open(f'https://t.me/norka_Dizzzackla')
        input(Fore.RED + 'нажми ENTER чтобы выйти')
#=======================================
if vibor=='2':
    info=Fore.BLUE+"""
    
    Этот код создан Dizzzackl'ам, он предстовляет из себя обучениею деанона по вк
    приватное продолжение вы сможете купить в моём тг канале её цена 600 рублей или
    6,26 usd . всем приятного пользования и до в стречи в будущем !
    """
    tgk=input('открыть тг канал ?')
    if tgk=='да':
        webbrowser.open(f'https://t.me/norka_Dizzzackla')
        input(Fore.RED + 'нажми ENTER чтобы выйти')
        print('\033[39m')
#======================================
if vibor=="3":
    webbrowser.open(f'https://t.me/norka_Dizzzackla')
    input(Fore.RED + 'нажми ENTER чтобы выйти')
    print('\033[39m')


