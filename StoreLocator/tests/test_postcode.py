from app.StoreLocator import create_app
from app.StoreLocator.db import get_db
from app.StoreLocator.postcode import search, coords, distance
from math import radians

app = create_app()


class TestPostcode:
    def get_data(self):
        with app.app_context():
            self.db = get_db()
            self.stores = self.db.execute('SELECT * FROM store').fetchall()


    def test_search_harrogate(self):
            self.get_data()

            # Short range
            results = search(self.stores, 'hg2 0fe', '10')

            # Check if sorted north south
            assert results == sorted(results, key=lambda x: x[3], reverse=True)
            # Sanity results check
            assert len(results) == 0


            # Larger range (300km<)
            results = search(self.stores, 'hg2 0fe', '500')

            # Check if sorted north south
            assert results == sorted(results, key=lambda x: x[3], reverse=True)
            # Sanity results check
            assert len(results) == 94


    def test_search_camden(self):
            self.get_data()
            results = search(self.stores, 'nw1 6bj', '10')

            # Check if sorted north south
            assert results == sorted(results, key=lambda x: x[3], reverse=True)

            # Sanity results check
            assert results[0][1] == 'Camden'
            assert results[-1][1] == 'Battersea'
            assert len(results) == 3


    def test_coords(self):
        with app.app_context():
            assert coords('ls19 6dn') == (-1.67979, 53.850309)
            assert coords('N0T A POSTCODE') == None
            assert coords('hg2 0fe') == (-1.559575, 53.984699)


    def test_distance(self):
        with app.app_context():
            assert round(distance(radians(-0.956537),
                           radians(51.157421),
                           radians(0.870721),
                           radians(51.135177))) == 127
