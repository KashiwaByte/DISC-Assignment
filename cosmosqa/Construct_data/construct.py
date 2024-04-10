import csv
import json

csv_file = 'data/train.csv'
jsonl_file = 'Construct_data/Cosmosqa_train.jsonl'

# 生成JSONL文件
messages = []

with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # 跳过标题行

    for row in reader:
        if len(row) >= 4:
            context = row[1]
            question = row[2]
            answer0 = row[3]
            answer1 = row[4]
            answer2 = row[5]
            answer3 = row[6]
            label = row[7]
            message={ "instruction":"As a reading comprehension expert, you will receive context, question and four answer options. Please understand the given Context first and then output the label of the correct option as the answer to the question based on the Context","input": str({'context':{context},'question':{question},"answer0":{answer0},"answer1":{answer1},"answer2":{answer2},"answer3":{answer3}}),"output":label}
            messages.append(message)
# 保存为JSONL文件
with open(jsonl_file, 'w', encoding='utf-8') as file:
    for message in messages:
        file.write(json.dumps(message, ensure_ascii=False) + '\n')
        