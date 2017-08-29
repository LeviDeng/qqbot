from qqbot import qqbotsched
import time

@qqbotsched(minute='0-59/1')
def sendTime(bot):
    b=bot.List('buddy','452790339')[0]
    bot.SendTo(b,time.asctime())
