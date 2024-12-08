from flask import Flask
from app.back.api.api import router as api_router


app = Flask(__name__)
app.register_blueprint(api_router)


