from flask import *
import product_service
app = Flask(__name__)


@app.route('/')
def route_index():
    return render_template("index.html")


@app.route("/detailed/artist/<artist_id>")
def detailed_artist_view(artist_id):
    artist = product_service.get_artist(artist_id)
    product_list = product_service.get_products_for_artist_id(artist_id)
    return render_template("artist_detailed.html", artist=artist, product_list=product_list)


@app.route("/discover")
def route_discover():
    product_list = product_service.get_product_list()
    return render_template("discover.html", product_list=product_list)


@app.route("/detailed/image/<product_id>")
def detailed_image_view(product_id):
    product = product_service.get_product_by_id(product_id)
    return render_template("image_detailed.html", product=product)


if __name__ == '__main__':
    app.run(debug=True)
