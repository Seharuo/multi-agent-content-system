import asyncio

class WriterAgent:
    def __init__(self, name):
        self.name = name

    async def run(self, task):
        content = f"🔥 爆款内容：{task['topic']}"
        print("[Writer]", content)
        await asyncio.sleep(1)
        return {"content": content}
