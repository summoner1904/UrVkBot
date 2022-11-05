import random
import vk_api
from base import *
from vk_api.longpoll import VkEventType, VkLongPoll
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from config import TOKEN


class BaseServer:
    vk = vk_api.VkApi(token=TOKEN)
    longpoll = VkLongPoll(vk)

    def start(self, command_list: dict):
        self.commands = command_list
        for event in self.longpoll.listen():
            self.command_worker(event)
    
    def command_worker(self, event):
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                if self.commands.get(event.text.lower()):
                    self.commands[event.text.lower()](event)
                else:
                    self.commands["ошибка"](event)


class UtilsServer(BaseServer):
    def send_msg(self, user_id, message, keyboard = None):
        if keyboard:
            params = {
                "user_id": user_id,
                "message": message,
                "random_id": random.randint(1, 10000),
                "keyboard": keyboard.get_keyboard()
            }
        else:
            params = {
                "user_id": user_id,
                "message": message,
                "random_id": random.randint(1, 10000),
            }
        self.vk.method("messages.send", params)


class Server(UtilsServer):
    def __init__(self):
        self.keyboard = KeyboardMixin()
        
    def command_error(self, event):
        self.send_msg(
            event.user_id,
            f"Введите день недели!"
        )

    def command_hi(self, event):
        self.send_msg(
            event.user_id,
            f"Привет!"
        )
    def command_keyboard(self, event):
        self.send_msg(
            event.user_id,
            f"Держи клавиатуру!",
            keyboard = self.keyboard.get_standart_keyboard()
        )
    def command_monday(self, event):
        self.send_msg(
            event.user_id,
            "\n".join(monday),
            keyboard=self.keyboard.get_standart_keyboard()
        )
    
    def command_tuesday(self, event):
        self.send_msg(
            event.user_id,
            "\n".join(tuesday)
        )
    
    def command_wednesday(self, event):
        self.send_msg(
            event.user_id,
            "\n".join(wednesday)
        )
    
    def command_thursday(self, event):
        self.send_msg(
            event.user_id,
            "\n".join(thursday)
        )
    
    def command_friday(self, event):
        self.send_msg(
            event.user_id,
            "\n".join(friday)
        )
    
    def command_saturday(self, event):
        self.send_msg(
            event.user_id,
            "\n".join(saturday)
        )


class KeyboardMixin(VkKeyboard):
    def get_standart_keyboard(self):
        keyboard = VkKeyboard()
        keyboard.add_button(label='Понедельник', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(label='Вторник', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(label='Среда', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(label='Четверг', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(label='Пятница', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(label='Суббота', color=VkKeyboardColor.PRIMARY)
        return keyboard