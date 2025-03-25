# AIAgentExer

����һ��AI Agentѧϰ��Ŀ����Ҫͨ��OpenAI API��LangChain��LlamaIndexʵ�ֶ�������Agent��

## ��Ŀ�ṹ

```
AIAgentExer/
������ agents/                 # Agentʵ��Ŀ¼
��   ������ ppt_creator/       # Agent 1: �Զ���PPT����
��   ������ function_caller/   # Agent 2: �๦��ѡ������
��   ������ react_agent/       # Agent 3: ReAct�Զ�����
��   ������ plan_executor/     # Agent 4: Plan-and-Execute������
��   ������ knowledge_base/    # Agent 5: LlamaIndex֪ʶ����
��   ������ open_agents/       # Agent 6: ��ԴAgent����
������ utils/                 # ���ߺ���
������ tests/                 # ����Ŀ¼
������ data/                  # ����Ŀ¼
������ requirements.txt       # ��Ŀ����
������ README.md             # ��Ŀ˵��
```

## Agents ˵��

### Agent 1: �Զ����칫ʵ��
ͨ��OpenAI��Assistants API��DALL��E 3ģ�ͣ�ʵ���Զ���PPT������

### Agent 2: �๦��ѡ������
ʹ��Function Callingʵ�ֺ������õ�����ѡ��

### Agent 3: �������ж���Эͬ
����LangChain��ReAct���ʵ�����ܶ���ϵͳ��

### Agent 4: �ƻ���ִ�еĽ���
ʹ��LangChain��Plan-and-Execute���ʵ�����ܿ����ȡ�

### Agent 5: ֪ʶ����ȡ������
ͨ��LlamaIndexʵ�ּ�����ǿ���ɣ�RAG����

### Agent 6: GitHub���������
���ɺ�ʵ��AutoGPT��BabyAGI��CAMEL�ȿ�ԴAgent��

## ����Ҫ��
- Python 3.8+
- OpenAI API Key
- ���Python������