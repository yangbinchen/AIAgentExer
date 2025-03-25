import os
import json
import requests
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 获取API密钥
api_key = os.getenv("OPENAI_API_KEY")
serpapi_key = os.getenv("SERPAPI_API_KEY")

if not api_key:
    raise ValueError("请在.env文件中设置OPENAI_API_KEY")
if not serpapi_key:
    raise ValueError("请在.env文件中设置SERPAPI_API_KEY")


# 定义搜索函数 (替代 SerpAPIWrapper)
def search_with_serpapi(query):
    """使用SerpAPI进行搜索"""
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "api_key": serpapi_key,
        "engine": "google"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json()
        # 提取有用的搜索结果信息
        organic_results = results.get("organic_results", [])
        if organic_results:
            info = []
            for result in organic_results[:3]:  # 只取前3条结果
                info.append({
                    "title": result.get("title", ""),
                    "snippet": result.get("snippet", ""),
                    "link": result.get("link", "")
                })
            return json.dumps(info, ensure_ascii=False)
        return "没有找到相关搜索结果。"
    else:
        return f"搜索失败，错误代码：{response.status_code}"


# 定义工具列表
tools = [
    {
        "name": "Search",
        "description": "当大模型没有相关知识时，用于搜索知识",
        "function": search_with_serpapi
    }
]

# 定义ReAct代理的提示模板
react_prompt_template = """Answer the following questions as best you can. You have access to the following tools:

Search: 当大模型没有相关知识时，用于搜索知识

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [Search]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {question}
Thought:"""


# 实现ReAct代理的函数
def react_agent(question, max_iterations=5):
    """使用OpenAI API实现ReAct代理"""
    conversation = [
        {"role": "system", "content": "你是一个按照ReAct框架工作的AI助手，需要思考、采取行动、观察，然后给出回答。"},
        {"role": "user", "content": react_prompt_template.format(question=question)}
    ]

    for i in range(max_iterations):
        # 调用OpenAI API获取回应
        response = openai_chat_completion(conversation)
        print(response)

        # 分析回应
        if "Final Answer:" in response:
            # 到达最终答案
            conversation.append({"role": "assistant", "content": response})
            return extract_final_answer(response)

        # 提取行动和行动输入
        action, action_input = extract_action_and_input(response)

        if not action:
            # 如果无法提取行动，则直接返回响应
            return response

        # 添加助手的思考过程到对话
        conversation.append({"role": "assistant", "content": response})

        # 执行工具调用
        observation = execute_tool(action, action_input)

        # 添加观察结果到对话
        observation_message = f"Observation: {observation}"
        conversation.append({"role": "user", "content": observation_message})

    # 达到最大迭代次数后，强制返回结果
    final_response = openai_chat_completion(
        conversation + [{"role": "user", "content": "你必须现在给出Final Answer，不要再进行更多思考和行动。"}])
    return extract_final_answer(final_response)


def openai_chat_completion(messages):
    """调用OpenAI API进行聊天补全"""
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": messages,
        "temperature": 0.7
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"API调用失败，错误代码：{response.status_code}, 错误信息：{response.text}"


def extract_action_and_input(response):
    """从响应中提取行动和行动输入"""
    if "Action:" not in response or "Action Input:" not in response:
        return None, None

    action_part = response.split("Action:")[1].split("\n")[0].strip()
    action_input_part = response.split("Action Input:")[1].split("\n")[0].strip()

    return action_part, action_input_part


def execute_tool(action, action_input):
    """执行工具调用"""
    for tool in tools:
        if tool["name"].lower() == action.lower():
            return tool["function"](action_input)
    return f"错误：找不到名为'{action}'的工具"


def extract_final_answer(response):
    """从响应中提取最终答案"""
    if "Final Answer:" in response:
        final_answer = response.split("Final Answer:")[1].strip()
        return final_answer
    return response


# 主函数
if __name__ == "__main__":
    question = "当前Agent最新研究进展是什么?"

    print("第一次运行的结果：")
    result1 = react_agent(question)
    print("\n最终答案:")
    print(result1)

    print("\n第二次运行的结果：")
    result2 = react_agent(question)
    print("\n最终答案:")
    print(result2)
