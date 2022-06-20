import telebot
import random
from telebot import types
from pytube import YouTube

token = '5433772583:AAGSe2OoeNOwveKVfrNb7mHIyuN89V_qE4M'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(msg):
      bot.send_message(msg.chat.id, 'Отправьте ссылку')

@bot.message_handler(content_types=['text'])
def get_video(msg):
    link = msg.text
    video = YouTube(link)
    filename = video.streams.filter(res='720p').first().default_filename
    video.streams.filter(res='720p').first().download()
    file = open(filename, 'rb')
    bot.send_video(msg.chat.id, file)
    bot.send_message(msg.chat.id, 'Приятного просмотра')
    
bot.polling()    
    

