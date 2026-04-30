# multi-agent-content-system
Multi-agent content automation system based on Python asyncio
# 🚀 Multi-Agent Content Automation System

一个基于多Agent协同的内容运营自动化系统，实现从内容生成、审核到发布的全流程自动化。

---

## 📌 项目简介

本项目构建了一个轻量级多Agent系统，通过多个AI Agent协同工作，模拟真实运营团队，实现内容生产流程的自动化。

系统包含以下核心角色：
- Manager Agent：任务调度与流程控制
- Writer Agent：内容生成
- Reviewer Agent：内容审核与优化
- Publisher Agent：内容发布

通过任务队列驱动，实现多任务并发处理与自动流转。

---

## 🧠 核心能力

- ✅ 多Agent协同（Multi-Agent System）
- ✅ 自动工作流（Workflow Automation）
- ✅ 异步任务调度（asyncio + Queue）
- ✅ 自动审核与重试机制
- ✅ 可扩展架构（支持接入大模型/API）

---

## 🔁 系统流程
Task Input
↓
Manager Agent
↓
Writer Agent → Reviewer Agent
↓
(Fail → Rewrite)
↓
Publisher Agent
↓
Completed

---

## ⚙️ 技术架构

- Python 3
- asyncio（异步执行）
- 内存任务队列（可扩展为Redis）
- 模块化Agent设计

---

## 🚀 快速开始

```bash
git clone https://github.com/yourname/multi-agent-content-system.git
cd multi-agent-content-system
python main.py
