class Nft:
    def __init__(self, id, title, artist, price, img_link = "https://lh6.ggpht.com/HlgucZ0ylJAfZgusynnUwxNIgIp5htNhShF559x3dRXiuy_UdP3UQVLYW6c=s1200"):
        self.id = id
        self.title = title
        self.artist = artist
        self.price = price
        self.img_link = img_link

nft_list = [Nft(1, "Neutrogena", "Mr. M", 0.555), Nft(2, "Losange", "Mr.D", 1.555), Nft(3, "LaKőr", "Mr. A", 520.21)]


def init_nft():
    pass


def get_nft_list():
    return nft_list
