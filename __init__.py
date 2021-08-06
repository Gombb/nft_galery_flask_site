from flask import *
import data_manager
app = Flask(__name__)


@app.route('/')
def route_index():
    last_five_image = data_manager.get_latest_products(3)
    return render_template("index.html", image_list=last_five_image)


# @app.route('/test')
# def route_test():
#     print(product_service.get_artist_for_id(1))


@app.route("/detailed/artist/<artist_id>")
def detailed_artist_view(artist_id):
    artist = data_manager.get_artist_for_id(artist_id)
    product_list = data_manager.get_products_for_artist_id(artist_id)
    print(artist)
    print(product_list)
    return render_template("artist_detailed.html", artist=artist, product_list=product_list)


@app.route("/discover")
def route_discover():
    product_list = data_manager.get_product_list()
    return render_template("discover.html", product_list=product_list)


@app.route("/detailed/image/<product_id>")
def detailed_image_view(product_id):
    product = data_manager.get_product_by_id(product_id)
    return render_template("image_detailed.html", product=product)


if __name__ == '__main__':
    app.run(debug=True)
