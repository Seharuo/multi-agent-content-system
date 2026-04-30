from agents.writer import WriterAgent
from agents.reviewer import ReviewerAgent
from agents.publisher import PublisherAgent

class ManagerAgent:
    def __init__(self):
        self.writer = WriterAgent("writer")
        self.reviewer = ReviewerAgent("reviewer")
        self.publisher = PublisherAgent("publisher")

    async def handle_task(self, task):
        print(f"🚀 开始任务：{task['topic']}")

        result = await self.writer.run(task)
        review = await self.reviewer.run(result)

        if not review["approved"]:
            print("重写中...")
            result = await self.writer.run(task)
            review = await self.reviewer.run(result)

        await self.publisher.run(review)
        print(f"✅ 完成：{task['topic']}")
