'''
    SOURCE OF BLOCKBROS API RECREATION

    MATT - 8/4/2025
    I’m not really on blockbros or have interacted with BlockBros anymore. I’m also not a great Python coder, so sorry if anything is poorly written this was just a learning experience

    Enjoy :)

    Database uses postgres
'''

class database_uri:
    development = ""
    published = ""

class config:
    SQLALCHEMY_DATABASE_URI = database_uri.published
    VPNAPI_KEY = "c0158ecfc93f4032b4267f38bed47b1a" # https://vpnapi.io/
