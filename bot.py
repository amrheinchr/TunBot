import sys
import time
import random
import datetime
import telepot
import urllib2
import os
import atexit
from subprocess import call

def goodNight():
    bot.sendMessage(owner, 'Good Night.')

atexit.register(goodNight)
f = open('credentials', 'r')
token = f.read(45)
f.readline()
owner = f.read(8);



def handle(msg):
    chat_id = msg['chat']['id']
    name = msg['chat']['first_name']
    command = msg['text']
    user = msg['from']
    print 'Got command',command, 'from', user, 'at', str(datetime.datetime.now())
    if str(chat_id) != owner:
        text = 'Got command ' + command + ' from ' + user['first_name'] + ' at ' + str(datetime.datetime.now())
        bot.sendMessage(owner, text)
    print 'execute'
    # Weather
    if command == 'Giesing':
        call(['./weather.sh', '098620'])
        img = open('weather.png', 'r')
        bot.sendPhoto(chat_id, img)
        img.close()
    elif command == 'Heidelberg':
        call(['./weather.sh', '107320'])
        img = open('weather.png', 'r')
        bot.sendPhoto(chat_id, img)
        img.close()
    elif command == 'Ladenburg':
        call(['./weather.sh', '107250'])
        img = open('weather.png', 'r')
        bot.sendPhoto(chat_id, img)
        img.close()
    elif command == 'Muenster':
        call(['./weather.sh', '103130'])
        img = open('weather.png', 'r')
        bot.sendPhoto(chat_id, img)
        img.close()
    elif command == 'Kahl':
        call(['./weather.sh', '194309'])
        img = open('weather.png', 'r')
        bot.sendPhoto(chat_id, img)
        img.close()
        
        # server time
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
        # raspbery ip
    elif command == '/ip':
        url = 'http://4.ifcfg.me/i'
        req = urllib2.Request(url)
        res = urllib2.urlopen(req)
        text = str(res.read())
        bot.sendMessage(chat_id, text)
        res.close()
    elif command == '/xkcd':
        call('./xkcd.sh')
        img = open('tmp.png', 'r')
        bot.sendPhoto(chat_id, img)
        img.close()
    elif command == '/smbc':
        call('./smbc.sh')
        img = open('smbc.png', 'r')
        bot.sendPhoto(chat_id, img)
        img.close()
        # call('rm tmp.png')
    elif command == '/update':
        call('./update.sh')
    elif command == '/weather':
        show_keyboard = {'keyboard': [['Kahl', 'Muenster'], ['Heidelberg', 'Giesing']], 'one_time_keyboard':True}
        bot.sendMessage(chat_id, 'For which location?', reply_markup=show_keyboard)
    elif command == '/proc':
        pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
        for pid in pids:
            try:
                text =  open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
                if text != "":
                    bot.sendMessage(chat_id, text)
            except IOError: # proc has already terminated
                    continue

bot = telepot.Bot(token)
bot.message_loop(handle)
bot.sendMessage(owner, 'Listening ... ')
print 'listening ...'

while 1:
    time.sleep(10)
