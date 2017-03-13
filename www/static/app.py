import logging
logging.basicConfig(level=logging.INFO)
import asyncio
import os
import json
import time

from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(headers={'Content-Type': 'text/html'}, body=b'<h1>Hello World</h1>')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    port = 9000
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', port=port)
    info = 'Server started at http://127.0.0.1:%d' % 9000
    logging.info(info)
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()