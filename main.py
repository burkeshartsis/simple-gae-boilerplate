"""Main controller script for the Engage website"""

import os
import sys

# Third party libraries path must be fixed before importing webapp2
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app/external'))

import webapp2

# URL mapping for appliation in /app/routes.py
from app import routes

debug = os.environ['SERVER_SOFTWARE'].startswith('Dev')

# initialize the application
app = webapp2.WSGIApplication(debug=debug)

# add routes to the application
routes.add_routes(app)
