#!/usr/bin/env python
# -*- coding: utf-8 -*-
import persistence
import requests


artist_cache = []


class Product:
    #decide on using meta_id in database or keeping both but giving them unified name
    def __init__(self, db_id, artist, contract_address, open_sea_token_id):
        self.contract_address = contract_address
        self.open_sea_token_id = open_sea_token_id
        self.metadata = self.query_metadata_from_opensea()
        self.last_price = self.price_in_ether(self.metadata["orders"][-1]["current_price"])
        self.base_price = self.price_in_ether(self.metadata["orders"][0]["base_price"])
        self.db_id = db_id
        self.meta_id = self.metadata["id"]
        self.title = self.metadata["name"]
        self.description = self.metadata["description"]
        self.artist = artist
        self.img_link = self.metadata["image_url"]

    def query_metadata_from_opensea(self):
        url = "https://api.opensea.io/api/v1/asset/"
        url += self.contract_address + "/"
        url += self.open_sea_token_id + "/"
        curl_req = requests.get(url)
        return curl_req.json()

    def price_in_ether(self, price_tag):
        return round(float(price_tag) * 0.000000000000000001, 4)


class Artist:
    def __init__(self, id, name, age, avatar, bio):
        self.id = id
        self.name = name
        self.age = age
        self.avatar = avatar
        self.bio = bio


def get_artist_list():
    if len(artist_cache) != 0:
        return artist_cache
    else:
        query_result = persistence.get_all_artist()
        for artist in query_result:
            artist_cache.append(Artist(artist["id"], artist["name"], 420, artist["avatar_url"], artist["bio"]))
        return artist_cache


def get_artist_for_id(artist_id):
    if len(artist_cache) == 0:
        get_artist_list()
    for artist in artist_cache:
        if int(artist.id) == int(artist_id):
            return artist


def get_product_list():
    product_list = []
    query_result = persistence.get_all_product()
    for product in query_result:
        product_list.append(Product(product["id"], get_artist_for_id(product["artist_id"]), product["contract_address"],
                                    product["token_id"]))
    return product_list


def get_product_by_id(product_id):
    product = persistence.get_product_for_id(product_id)[0]
    return Product(product_id, get_artist_for_id(product["artist_id"]), product["contract_address"], product["token_id"])


def get_products_for_artist_id(artist_id):
    #create separate query to avoid using getall query
    result_list = []
    for product in get_product_list():
        if product.artist.id == int(artist_id):
            result_list.append(product)
    return result_list


def get_latest_products(amount):
    return get_product_list()[0:amount]


