from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot
from telegram.utils.request import Request



class Command(BaseCommand):

    help = 'Telegram bot'

    def handle(self, *args, **kwargs):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
        bot = Bot(
            request=request,
            token=settings.BOT_TOKEN,
        )
        print(bot.get_me())

