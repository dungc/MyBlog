import logging
import asyncio
from asyncio import AbstractEventLoop
import os
import json
import time

from datetime import datetime

from aiohttp import web


def index(request):
    return web.Response(headers={'Content-Type': 'text/html'}, body=b'<h1>Hello World</h1>')


@asyncio.coroutine
def init(event_loop):
    app = web.Application(loop=event_loop)
    app.router.add_route('GET', '/', index)
    port = 9000
    srv = yield from event_loop.create_server(app.make_handler(), '', port=port)
    info = 'Server started at http://127.0.0.1:%d' % 9000
    logging.info(info)
    return srv

logging.basicConfig(level=logging.INFO)
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
