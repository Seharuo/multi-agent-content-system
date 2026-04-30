import asyncio

class PublisherAgent:
    def __init__(self, name):
        self.name = name

    async def run(self, task):
        print("[Publisher] 发布：", task["content"])
        await asyncio.sleep(1)
