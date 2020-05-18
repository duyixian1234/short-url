from flask import Flask, request, jsonify, redirect
from redis import Redis
from os import getenv
from uuid import uuid4
from base64 import b64encode

cache_service = Redis.from_url(getenv("REDIS_URL", "redis://localhost:6379/1"))

app = Flask(__name__)


@app.route("/api/add")
def add_url():
    url = request.values.get("url")
    while cache_service.get(key := gen_key()):
        key = gen_key()
    cache_service.set(key, url)
    return jsonify(success=True, data=dict(origin=url, short=key))


@app.route("/<string:path>")
def get_url(path: str):
    if origin := cache_service.get(path):
        return redirect(origin.decode())
    return jsonify(success=False, msg="Not Found"), 404


def gen_key():
    return b64encode(uuid4().hex.encode()).decode()[:6]
