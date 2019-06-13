#!/usr/bin/env python

import asyncio
import json
from pynput.keyboard import Key, Controller
import websockets

keyboard = Controller()

async def handle_input(websocket, path):
	while True:
		input = await websocket.recv()
		
		data = json.loads(input)
		
		print(data)
		
		try:
			if data['type'] == "keyboard":
				key = data['event']['eventData']
				if data['event']['eventType'] == "down":
					keyboard.press(key)
				elif data['event']['eventType'] == "up":
					keyboard.release(key)
		except ValueError:
			pass
				

start_server = websockets.serve(handle_input, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()