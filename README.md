# AIAgentExer

这是一个AI Agent学习项目，主要通过OpenAI API、LangChain和LlamaIndex实现多种智能Agent。

## 项目结构

```
AIAgentExer/
├── agents/                 # Agent实现目录
│   ├── ppt_creator/       # Agent 1: 自动化PPT创作
│   ├── function_caller/   # Agent 2: 多功能选择引擎
│   ├── react_agent/       # Agent 3: ReAct自动定价
│   ├── plan_executor/     # Agent 4: Plan-and-Execute库存调度
│   ├── knowledge_base/    # Agent 5: LlamaIndex知识检索
│   └── open_agents/       # Agent 6: 开源Agent集成
├── utils/                 # 工具函数
├── tests/                 # 测试目录
├── data/                  # 数据目录
├── requirements.txt       # 项目依赖
└── README.md             # 项目说明
```

## Agents 说明

### Agent 1: 自动化办公实现
通过OpenAI的Assistants API和DALL·E 3模型，实现自动化PPT创作。

### Agent 2: 多功能选择引擎
使用Function Calling实现函数调用的智能选择。

### Agent 3: 推理与行动的协同
基于LangChain的ReAct框架实现智能定价系统。

### Agent 4: 计划和执行的解耦
使用LangChain的Plan-and-Execute框架实现智能库存调度。

### Agent 5: 知识的提取与整合
通过LlamaIndex实现检索增强生成（RAG）。

### Agent 6: GitHub的网红聚落
集成和实现AutoGPT、BabyAGI和CAMEL等开源Agent。

## 环境要求
- Python 3.8+
- OpenAI API Key
- 相关Python包依赖