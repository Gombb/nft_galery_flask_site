#!/usr/bin/env python
# -*- coding: utf-8 -*-
from persistence import *


def get_latest_pics(amount):
    return get_product_list()[0:amount]


def init_nft():
    pass


def get_artist(artist_id):
    for artist in get_artist_list():
        if artist.id == int(artist_id):
            return artist


def get_products_for_artist_id(artist_id):
    result_list = []
    for product in get_product_list():
        if product.artist.id == int(artist_id):
            result_list.append(product)
    return result_list


def get_product_by_id(product_id):
    for product in get_product_list():
        if product.id == int(product_id):
            return product


def get_all_products():
    return get_product_list()
