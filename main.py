import pandas as pd
import os
import numpy as np
import re

file_path = "."
file_name = "smsCount.csv"

file_ = os.path.join(file_path, file_name)
def count_it(sms_content):
    all_punctuation = r"""!"#$%&'()*+,./:;<=>?@[\]^_`{|}~"""
    return "".join(re.findall(rf'[^a-zA-Z\s0-9\{all_punctuation}]+', sms_content)).__len__()

df = pd.read_csv(file_, sep=',')
df['character_count'] = df.content.str.len()
df['sms_count'] = np.ceil(df.character_count / 70)
df['sms_count_2'] = np.ceil((df.content.apply(count_it)*2  + df.content.str.len() - df.content.apply(count_it)) / 70)

test_data = count_it(df.content[1]) * 2 + df.content[1].__len__() - count_it(df.content[1])

total_count = df.sms_count.sum()
total_count_2 = df.sms_count_2.sum()
sms_mean = df.sms_count.mean()
sms_mean_2 = df.sms_count_2.mean()
print(f'total_count:{total_count}, sms_mean:{sms_mean}')
print(f'total_count:{total_count_2}, sms_mean:{sms_mean_2}')
pass
