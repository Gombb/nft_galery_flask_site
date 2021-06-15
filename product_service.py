#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import requests
import time

contract_address1 = "0x495f947276749Ce646f68AC8c248420045cb7b5e"
token_id1 = "63150080862586220144499677713436387260670121981595781099876257943183637348353"
contract_address2 = "0x495f947276749Ce646f68AC8c248420045cb7b5e"
token_id2 = "14756086664038233523160058507758541272568006944930919508280125615919402582017"
contract_address3 = "0x495f947276749Ce646f68AC8c248420045cb7b5e"
token_id3 = "14756086664038233523160058507758541272568006944930919508280125614819890954241"
contract_address4 = "0xC2C747E0F7004F9E8817Db2ca4997657a7746928"
token_id4 = "1131"


def price_in_ether(price_tag):
    return round(float(price_tag) * 0.000000000000000001, 4)


class Nft:

    def __init__(self, artist, contract_address, open_sea_token_id):
        self.contract_address = contract_address
        self.open_sea_token_id = open_sea_token_id
        self.metadata = self.query_metadata_from_opensea()
        self.sleep = self.sleep()
        self.last_price = price_in_ether(self.metadata["orders"][-1]["current_price"])
        self.base_price = price_in_ether(self.metadata["orders"][0]["base_price"])
        self.id = self.metadata["id"]
        self.title = self.metadata["name"]
        self.description = self.metadata["description"]
        self.artist = artist
        self.img_link = self.metadata["image_url"]

    def sleep(self):
        time.sleep(3)

    def query_metadata_from_opensea(self):
        url = "https://api.opensea.io/api/v1/asset/"
        url += self.contract_address + "/"
        url += self.open_sea_token_id + "/"
        curl_req = requests.get(url)
        return curl_req.json()


class Artist:
    def __init__(self, id, name, age, avatar, bio):
        self.id = id
        self.name = name
        self.age = age
        self.avatar = avatar
        self.bio = bio


test_img_link_1 = "https://i.pinimg.com/564x/1d/9b/57/1d9b5704645fcecb8d514fd8f798c136.jpg"
test_img_link_2 = "https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/image-bgEuwDxel93-Pg-large_1.png"
test_img_link_3 = "https://craftinga.com/wp-content/uploads/2020/11/Trump-Witch.jpg"
avatar_1 = "https://pbs.twimg.com/profile_images/1346530588090634240/8wmsHX88_400x400.png"

lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
artist_1 = Artist(1, "Mr.M", 42, avatar_1, lorem_ipsum)
artist_2 = Artist(2, "Mr.D", 25, avatar_1, lorem_ipsum)
artist_dict = {artist_1.name: artist_1, artist_2.name: artist_2}
artist_list = [artist_1, artist_2]
nft_1 = Nft(artist_dict["Mr.D"], contract_address1, token_id1)
nft_2 = Nft(artist_dict["Mr.M"], contract_address2, token_id2)
nft_3 = Nft(artist_dict["Mr.M"], contract_address3, token_id3)
nft_4 = Nft(artist_dict["Mr.D"], contract_address4, token_id4)

product_list = []
for i in range(20):
    product_list.append(nft_1)
    product_list.append(nft_2)
    product_list.append(nft_3)
    product_list.append(nft_4)






def get_latest_pics(amount):
    return product_list[0:amount]


def init_nft():
    pass


def get_artist(artist_id):
    for artist in artist_list:
        if artist.id == int(artist_id):
            return artist


def get_products_for_artist_id(artist_id):
    result_list = []
    for product in product_list:
        if product.artist.id == int(artist_id):
            result_list.append(product)
    return result_list


def get_product_by_id(product_id):
    for product in product_list:
        if product.id == int(product_id):
            return product


def get_product_list():
    return product_list
