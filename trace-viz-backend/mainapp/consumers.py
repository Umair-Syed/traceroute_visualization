# Django Channels consumers are similar to views, but they are long-lived and can send multiple responses back.

import asyncio
import platform
import re
import subprocess
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from threading import Thread

class TracerouteConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("Connected (in consumer)")

    async def receive_json(self, content):
        print(f"Received message: {content}")
        hostname = content.get('hostname')
        if hostname:
            print(f"Running traceroute for hostname: {hostname}")
            timeout = 10

            # Get the current event loop
            loop = asyncio.get_running_loop()
            
            # Start a new thread that will run the traceroute command
            thread = Thread(target=self.traceroute, args=(hostname, timeout, loop))
            thread.start()

    def traceroute(self, hostname, timeout, loop):
        proc = subprocess.Popen(
            ["tracert" if platform.system() == 'Windows' else "traceroute", "-w", str(timeout), hostname],
            stdout=subprocess.PIPE,
            text=True,
        )
        
        # Read the command output line by line
        for line in proc.stdout:
            ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
            ip_addresses = re.findall(ip_pattern, line)
            
            # Send the message asynchronously to the client
            asyncio.run_coroutine_threadsafe(self.send_json(ip_addresses), loop)
