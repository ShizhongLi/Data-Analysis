"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""


call_number_list_of_texts, answer_number_list_of_texts, timestamp_list_of_texts = zip(*texts)
call_number_list_of_calls, answer_number_list_of_calls, timestamp_list_of_calls, during_time_of_calls  = zip(*calls)

set_of_all_numbers = set(call_number_list_of_texts) | set(answer_number_list_of_texts) | set(call_number_list_of_calls) | set(answer_number_list_of_calls)

print('There are {} different telephone numbers in the records.'.format(len(set_of_all_numbers)))