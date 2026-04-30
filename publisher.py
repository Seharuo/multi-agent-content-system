import asyncio
import random

class ReviewerAgent:
    def __init__(self, name):
        self.name = name

    async def run(self, task):
        approved = random.choice([True, True, False])
        print("[Reviewer]", "通过" if approved else "驳回")
        await asyncio.sleep(1)
        return {"approved": approved, "content": task["content"]}
