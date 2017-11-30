# things.py

# Let's get this party started!
import falcon


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class ThingsResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nTwo things awe me most, the starry sky '
                     'above me and the moral law within me.\n'
                     '\n'
                     '    ~ Immanuel Kant\n\n')

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()

# things will handle all requests to the '/things' URL path
app.add_route('/things', things)

import falcon
from falcon_swagger_ui import register_swaggerui_app

SWAGGERUI_URL = '/swagger'  # without trailing '/'
# SCHEMA_URL = 'http://petstore.swagger.io/v2/swagger.json'

# For developer environment you can expose a static endpoint like:
from falcon_swagger_ui import StaticSinkAdapter


# app = falcon.API()
SCHEMA_URL = '/swagger.json' # Can't read swagger JSON from http://127.0.0.1:8000/docs/v2/swagger.json
app.add_sink(
    StaticSinkAdapter('/home/greg/falcon-swagger-example/schema.json'), SCHEMA_URL
)


register_swaggerui_app(app, SWAGGERUI_URL, SCHEMA_URL, config={
    'supportedSubmitMethods': ['get'],
})







# import falcon
# from falcon_swagger_ui import StaticSinkAdapter
# from falcon_swagger_ui import register_swaggerui_app
#
# SWAGGERUI_URL = '/swagger'
# SCHEMA_URL = '/swagger.json'
#
# app = falcon.API()
# app.add_sink(
#     StaticSinkAdapter('/home/greg/falcon-swagger-example/schema.json'), SCHEMA_URL
# )
#
# register_swaggerui_app(app, SWAGGERUI_URL, SCHEMA_URL, config={
#     'supportedSubmitMethods': ['get'],
# })
