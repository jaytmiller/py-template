"""This module defines Quart request handlers which implement the REST API."""

import os

from quart import request, jsonify

from {{PYT_PKG_NAME}}.main import init_api, service_function_1

from {{PYT_PKG_NAME}}.app import app

# -------------------------------------------------------------------------------------


@app.route("/check-alive", methods=["GET"])
async def check_alive():
    api = init_api(reinit=False)
    api.log.info("{{PYT_PKG_NAME}} is alive.")
    return jsonify("ok")


@app.route("/function-1", methods=["POST"])
async def handle_function_1_request():
    data = await request.get_json()
    spawn_info = service_function_1(
        data["par1"], data["par2"], data["par3"], data["par4"]
    )
    return jsonify(spawn_info)


if __name__ == "__main__":
    app.run(debug=bool(os.environ.get("DEBUG_QUART", False)))
