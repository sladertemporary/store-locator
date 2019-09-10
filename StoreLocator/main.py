from flask import render_template, Blueprint, request
from .db import get_db
from . import postcode

app = Blueprint('main', __name__, url_prefix='/')

# Main view
@app.route('/')
def index():
    db = get_db()
    stores = db.execute('SELECT * FROM store ORDER BY location').fetchall()

    return render_template('main/list.html', stores=stores)

# Search view
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        db = get_db()

        stores = db.execute('SELECT * FROM store').fetchall()
        input_postcode = request.form.get('postcode')
        input_radius = request.form.get('radius')

        results = postcode.search(stores, input_postcode, input_radius)

        return render_template('main/list.html',
                               stores=results,
                               postcode=input_postcode,
                               radius=input_radius)
    else:
        return index()
