import csv
import asyncio
from docx import Document 
from async_video_prompt_generate import (
    prompting, structed_paragraphs, client_create, instructions_reader
)


#RUN SCRIPT AND CREATE TABLE
async def main():
    #EXPORT DOC AND START PROMPTING
    document_read = Document("docs/document.docx")
    doc = structed_paragraphs(document_read)
    data = await prompting(client=client_create(), paragraphs=doc, instructions_prompt=instructions_reader())

    #CREATING TABLE
    with open("docs/prompts_table.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "paragraph", "response"])
        writer.writerows(data)


#RUN
if __name__ == "__main__":
    asyncio.run(main())