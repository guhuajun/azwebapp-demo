# -*- coding: utf-8 -*-
# pylint: disable=

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
import uvicorn

async def index(request):
    return JSONResponse({'hello': 'world'})

routes = [
    Route('/', index),
]

app = Starlette(debug=False, routes=routes)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
