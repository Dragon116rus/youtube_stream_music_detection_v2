import asyncio
from shazamio import Shazam
import json

async def main():
  shazam = Shazam()
  out = await shazam.recognize_song('shazam.m4a')
  print(json.dumps(out))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())