from openai import OpenAI
from dotenv import load_dotenv
from docx import Document 
import os
load_dotenv()
print(os.getenv("OPENAI_API_KEY"), os.getenv("BASE_URL"))



def prompting():
    #CLIENT
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("BASE_URL")
    )

    #INSTRUCTIONS PROMPT
    with open("docs/prompt.txt", 'r', encoding="utf-8") as f:
        instructions_prompt = f.read()

    #DOCX FILE
    document = Document("docs/document.docx")

    generated_prompts = []

    ind = 0
    #PROMPTING
    for para in document.paragraphs:
        is_heading = False
        if any(run.bold is True for run in para.runs):
            is_heading = True


        if not(is_heading) and not(para.text.strip()==""):
            response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": instructions_prompt},
                {"role": "user", "content": para.text}
                ],
        )
            print(response.choices[0].message.content)
            ind += 1
            generated_prompts.append([ind, para.text, response.choices[0].message.content])

    return generated_prompts


if __name__ == "__main__":
    prompting()