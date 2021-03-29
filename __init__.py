from flask import *
import nft_cards
app = Flask(__name__)


@app.route('/')
def route_index():
    return render_template("index.html")


@app.route("/detailed/artist/<artist_id>")
def detailed_artist_view(artist_id):
    return render_template("artist_detailed.html")


@app.route("/discover")
def route_discover():
    nfts = nft_cards.get_nft_list()
    return render_template("discover.html", nfts=nfts)


@app.route("/detailed/image/<image_id>")
def detailed_image_view(image_id):
    nft_card = nft_cards.get_nft_by_id(image_id)
    return render_template("image_detailed.html", nft_card=nft_card)


if __name__ == '__main__':
    app.run(debug=True)
