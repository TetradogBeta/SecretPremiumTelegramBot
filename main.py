from TelegramHelper.Bot import Bot
from Pagina import Pagina
from os.path import exists
import time
import os
import sys

def Main():
    fileConfig="Config";

    if exists(fileConfig):
        fConfig = open(fileConfig, "r");
        config = fConfig.readlines();
        fConfig.close();
        token=config[0].replace("\n","");
        regex=config[1].replace("\n","");

    elif len(sys.argv)>1:
        token=sys.argv[1];
        regex=sys.argv[2];
        fConfig = open(fileConfig, 'w');
        fConfig.writelines([token,regex]);
        fConfig.close();

    bot=Bot(token,"Secret V2.0");

    bot.Default.AddRegex(regex,SendPhotos);
    bot.Default.Default=lambda cli:cli.SendText("Solo URL de ese sitio!");

    bot.Start();

def SendPhotos(cli):
    for photo in Pagina(cli.Args[0]).GetPhotos():
        cli.SendPhoto(photo);

Main();