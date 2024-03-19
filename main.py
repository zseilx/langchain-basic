#!venv/bin/python3

from langchain_openai import ChatOpenAI


def main():
    llm = ChatOpenAI()
    llm.invoke("how can langsmith help with testing?")


if __name__ == "__main__":
    main()
