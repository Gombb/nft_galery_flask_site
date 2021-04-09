from flask import *
import product_service
app = Flask(__name__)


@app.route('/')
def route_index():
    return render_template("index.html")


@app.route("/detailed/artist/artist<artist_id>")
def detailed_artist_view(artist_id):
    return render_template("artist_detailed.html")


@app.route("/discover")
def route_discover():
    products = product_service.get_nft_list()
    return render_template("discover.html", nfts=products)


@app.route("/detailed/image/<image_id>")
def detailed_image_view(image_id):
    product_card = product_service.get_nft_by_id(image_id)
    return render_template("image_detailed.html", nft_card=product_card)


if __name__ == '__main__':
    app.run()
