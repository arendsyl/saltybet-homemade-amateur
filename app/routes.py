from app import api

from app.resources.shape import DataFrameShape

# Add every routes of the project
api.add_resource(DataFrameShape, '/api/shape')