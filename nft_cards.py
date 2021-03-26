class Nft:
    def __init__(self, id, title, artist, price, img_link = "https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/image-bgEuwDxel93-Pg-large_1.png"):
        self.id = id
        self.title = title
        self.artist = artist
        self.price = price
        self.img_link = img_link


class Artist:
    def __init__(self, name, age):
        self.name = name
        self.age = age


artist_1 = Artist("Mr.M", 42)
artist_2 = Artist("Mr.D", 25)
artist_dict = {artist_1.name: artist_1, artist_2.name: artist_2}
nft_list = [Nft(1, "Neutrogena", artist_dict["Mr.D"],  0.555), Nft(2, "Losange", artist_dict["Mr.M"], 1.555),
            Nft(3, "LaKőr", artist_dict["Mr.M"], 520.21)]


def init_nft():
    pass


def get_nft_by_id(id):
    for nft in nft_list:
        if nft.id == int(id):
            return nft


def get_nft_list():
    return nft_list
