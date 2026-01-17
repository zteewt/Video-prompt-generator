import csv
from video_prompt_generate import prompting

def main():
    data = prompting()
    with open("docs/prompts_table.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "paragraph", "response"])
        writer.writerows(data)


if __name__ == "__main__":
    main()