from server import Server
bot = Server()

command_list = {
    "привет": bot.command_hi,
    "понедельник": bot.command_monday,
    "вторник": bot.command_tuesday,
    "среда": bot.command_wednesday,
    "четверг": bot.command_thursday,
    "пятница": bot.command_friday,
    "суббота": bot.command_saturday, 
}
bot.start(command_list)