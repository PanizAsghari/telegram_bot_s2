import pymysql
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

import telegram

import logging
from telegram.error import NetworkError, Unauthorized
from time import sleep

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='88213009h', db='dblab', autocommit=True)



TOKEN = '420852520:AAHwTY-YRwTog5Hzc3o8p36pzwSyCi16FP4'


update_id = None

def main():
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot(TOKEN)

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1


def echo(bot):
    global update_id
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:  # your bot can receive updates without messages
            # Reply to the message
            msg_text='welcome'
            update.message.reply_text(
        text=msg_text
    )
        if update.message:
            save(update)

def save(update):
    cursor = conn.cursor()
    sql="create table if not exists table_messages(ID int NOT NULL AUTO_INCREMENT  PRIMARY KEY , MESSAGE varchar(250));"
    cursor.execute(sql)
    sql="INSERT INTO table_messages (MESSAGE) VALUES ('%s')" %(update.message.text)
    cursor.execute(sql)
    conn.commit()
    sql="SELECT * FROM table_messages"
    ms=cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)



if __name__ == '__main__':
    main()
