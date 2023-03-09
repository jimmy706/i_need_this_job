from apiflask import APIBlueprint

bp = APIBlueprint('promote_letter', __name__, url_prefix='/promote_letter')

from app.promote_letter import routes
