import asyncio
from agents.manager import ManagerAgent
from core.queue import TaskQueue

async def main():
    manager = ManagerAgent()
    queue = TaskQueue()

    asyncio.create_task(queue.worker(manager))

    topics = [
        "课题申报写作技巧",
        "论文快速发表攻略",
        "教学设计高分模板",
        "小红书引流文案技巧"
    ]

    for topic in topics:
        await queue.add_task({"topic": topic})

    await queue.queue.join()

if __name__ == "__main__":
    asyncio.run(main())
