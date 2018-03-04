from app import stores, models, data
from flask import Flask

app = Flask(__name__)

members_store = stores.MembersStore()
posts_store = stores.PostsStore()
data.seed_stores(members_store, posts_store)

from app.views import *