from telepot.loop import MessageLoop
from Pagina import Pagina
import telepot

class TelegramBot:
    Bot=None;

    def __init__(self,msg):
        content_type, chat_type, chat_id = telepot.glance(msg);
        self.IdChat=chat_id;

    def SendPhoto(self,urlImg,desc=""):
        TelegramBot.Bot.sendPhoto(self.IdChat,urlImg,desc);

    def SendText(self,text):
        TelegramBot.Bot.sendMessage(self.IdChat,text);

    @staticmethod
    def Start(token):
        TelegramBot.Bot=telepot.Bot(token);
        return MessageLoop(TelegramBot.Bot, handle=TelegramBot._DoIt);
    
    @staticmethod
    def _DoIt(message):
        chat=TelegramBot(message);
        url=None;
        if "caption" in message:
            if "http" in message["caption"]:
                url=message["caption"];

        elif "reply_to_message" in message:
            if "http" in message["reply_to_message"]["caption"]:
                url=message["reply_to_message"]["caption"]; 
      
        elif "http" in message["text"]:
            url=message["text"];

        if url is not None:
            for photo in Pagina(url).GetPhotos():
                    chat.SendPhoto(photo);
        else:
            chat.SendText("Error solo se admiten URL de un lugar en particular ;) que no te diré :D");