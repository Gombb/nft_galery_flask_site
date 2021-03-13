from flask import *
import nft_cards
app = Flask(__name__)


@app.route('/')
def route_index():
    return render_template("index.html")


@app.route("/discover")
def route_discover():
    nfts = nft_cards.get_nft_list()
    return render_template("discover.html", nfts=nfts)


@app.route("/detailed/<image_id>")
def detailed_view(image_id):

    return render_template("detailed.html")

if __name__ == '__main__':
    app.run()
