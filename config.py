HEROKU = True   # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ
    API_ID = int(environ["3645214"])
    API_HASH = environ["50102c0b507d9cee1b73b12e5d414a74"]
    SUDO_CHAT_ID = int(environ["1001327974638"]) # Chat where the bot will play the music.
    SUDOERS = list(int(x) for x in environ.get("130856584", "").split()) # Users which have special control over the bot.
    SESSION_STRING = environ["BQAHa4lYfXdom_cP1CWS_jXFhcW-uyoKFtSB96x4wOo2rJakXwKdumHHNMSKyRxkBP7QNZ2n4khTCF7ww7xFuKVTzYwxJOny5DGemILkWo9IzL1eLLrWSXizQiIW5QqL5CfY1dtBhN5fIOqWARR-SC2F6ZH5r4bRdUBeeaR6-irOSNzy8dunJfmnKsa6kDaa-MLLNRyp9qGA_N4LcFszDzMEwZQDrp2IRjsku6swKL1QelivCkgo_plpoBNImcpSTGHBuWxCpoG29vqANnyKsP3IVvHYQjSX4KqII5fGltAKT76OPYoD0c_d4xbdQpILk_WonE4fHZs8LWtQS-SlXDGSTf8hVwA"] # Check Readme for session

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    SUDO_CHAT_ID = -1001485876964
    SUDOERS = [1243703097, 13216546]

# don't make changes below this line
ARQ_API = "https://thearq.tech"
