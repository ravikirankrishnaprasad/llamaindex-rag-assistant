from llama_index.core.tools.query_engine import QueryEngineTool
from llama_index.core.tools.types import ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.core.chat_engine.types import AgentChatResponse
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings

import chainlit as cl
from chainlit.input_widget import Select  # ✅ FIXED
import openai

from index_wikipages import create_index
from utils import get_apikey


# Globals
index = None
agent = None


def wikisearch_engine(idx):
    return idx.as_query_engine(response_mode="compact", verbose=True, similarity_top_k=10)


def create_react_agent(idx, model):
    query_engine_tools = [
        QueryEngineTool(
            query_engine=wikisearch_engine(idx),
            metadata=ToolMetadata(
                name="Wikipedia",
                description="Useful for performing searches on the wikipedia knowledgebase",
            ),
        )
    ]
    openai.api_key = get_apikey()
    Settings.llm = OpenAI(model=model)

    return ReActAgent.from_tools(
        tools=query_engine_tools,
        llm=Settings.llm,
        verbose=True,
    )


@cl.on_chat_start
async def on_chat_start():
    await cl.ChatSettings(
        [
            Select(
                id="MODEL",
                label="OpenAI - Model",
                values=["gpt-3.5-turbo", "gpt-4", "gpt-4o"],
                initial_index=0,
            )
        ]
    ).send()
    await cl.Message("👋 Welcome! Type `please index: <Wikipedia topic>` to start.").send()


@cl.on_message
async def handle_user_message(msg: cl.Message):
    global index, agent
    message = msg.content.strip()
    print("Received message:", message)

    # Handle indexing command
    if message.lower().startswith("please index:"):
        topic = message[len("please index:"):].strip()
        if not topic:
            await cl.Message("❌ Please provide a Wikipedia topic.").send()
            return

        await cl.Message(f"🔍 Indexing Wikipedia topic: **{topic}**...").send()
        index = create_index(topic)

        model = cl.user_session.get("settings", {}).get("MODEL", "gpt-3.5-turbo")
        agent = create_react_agent(index, model)

        await cl.Message(f"✅ Topic '{topic}' indexed and agent is ready!").send()
        return

    # Handle message with agent
    if agent:
        print("Agent is ready, sending message...")
        response = await cl.make_async(agent.chat)(message)
        final_text = response.response if isinstance(response, AgentChatResponse) else str(response)
        await cl.Message(author="Agent", content=final_text).send()
    else:
        await cl.Message("❌ Agent is not ready. First type: `please index: <Wikipedia topic>`").send()


@cl.on_settings_update
async def on_settings_update(settings):
    cl.user_session.set("settings", settings)
    print("Updated settings:", settings)
