class Nft:
    def __init__(self, id, title,  description, artist, price, img_link):
        self.id = id
        self.title = title
        self.description = description
        self.artist = artist
        self.price = price
        self.img_link = img_link


class Artist:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


img_link_1 = "https://i.pinimg.com/564x/1d/9b/57/1d9b5704645fcecb8d514fd8f798c136.jpg"
img_link_2 = "https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/image-bgEuwDxel93-Pg-large_1.png"
img_link_3 = "https://craftinga.com/wp-content/uploads/2020/11/Trump-Witch.jpg"

lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
artist_1 = Artist(1, "Mr.M", 42)
artist_2 = Artist(2, "Mr.D", 25)
artist_dict = {artist_1.name: artist_1, artist_2.name: artist_2}
nft_1 = Nft(1, "Neutrogena", lorem_ipsum, artist_dict["Mr.D"],  0.555, img_link_1)
nft_2 = Nft(2, "Losange", lorem_ipsum, artist_dict["Mr.M"], 1.555, img_link_2)
nft_3 = Nft(3, "LaKor", lorem_ipsum, artist_dict["Mr.M"], 520.21, img_link_3)


nft_list = []
for i in range(20):
    nft_list.append(nft_1)
    nft_list.append(nft_2)
    nft_list.append(nft_3)


def init_nft():
    pass


def get_nft_by_id(id):
    for nft in nft_list:
        if nft.id == int(id):
            return nft


def get_nft_list():
    return nft_list
