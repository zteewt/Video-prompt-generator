from openai import AsyncOpenAI
from dotenv import load_dotenv
from docx import Document 
import os
import asyncio
load_dotenv()
print(os.getenv("OPENAI_API_KEY"), os.getenv("BASE_URL"))



#DOCX FILE
document = Document("docs/document.docx")

#CLIENT
def client_create():
    client = AsyncOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("BASE_URL")
    )
    return client

#INSTRUCTIONS PROMPT
def instructions_reader():    
    with open("docs/prompt.txt", 'r', encoding="utf-8") as f:
        instructions_prompt = f.read()
    return instructions_prompt


#EXCLUDE HEADERS
def structed_paragraphs(document: Document):
    paragraphs = []
    for para in document.paragraphs:
        is_heading = False
        if any(run.bold is True for run in para.runs):
            is_heading = True
    
        if not(is_heading) and not(para.text.strip()==""):
             paragraphs.append(para.text)

    return paragraphs


#PROMPTING
async def prompting(client: AsyncOpenAI, paragraphs: list, instructions_prompt: str):
    generated_prompts = []
    ind = 0


    tasks = []
    for i in range(len(paragraphs)):
        task = asyncio.create_task(client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": instructions_prompt},
                {"role": "user", "content": paragraphs[i]}
            ],
        ))

        tasks.append(task)
        ind += 1

    responses = await asyncio.gather(*tasks)
    
    for i, resp in enumerate(responses, start=1):
        generated_prompts.append([i, paragraphs[i-1], resp.choices[0].message.content])
    
    return generated_prompts



#RUN FROM THIS FILE
if __name__ == "__main__":
    asyncio.run(prompting(
        client=client_create(),
        paragraphs=structed_paragraphs(document), 
        instructions_prompt=instructions_reader()
    ))