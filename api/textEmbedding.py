import ollama


def api_generate(text: str):

    stream = ollama.generate(
        stream=False,
        model='deepseek-r1:70b',
        prompt=text,
    )
    return stream['response'].split("</think>\n\n")[-1]


def api_text_embedding(text: str):

    stream = ollama.embeddings(
        model="nomic-embed-text",
        prompt=text,    
    )
    return stream["embedding"]


if __name__ == '__main__':
    prompt = "hello"
    content = api_text_embedding(prompt)
    print(len(content))