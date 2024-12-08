from flask import Flask
from app.back.api.api import router as api_router
from app.back.pages.user_back import router as user_router


app = Flask(__name__, static_folder='static')

app.register_blueprint(api_router)
app.register_blueprint(user_router)


