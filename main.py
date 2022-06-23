import pandas as pd
import os
import numpy as np
import re
import datetime


class Count:
    """Get sms counts within the e-appointment database"""

    def __init__(self, filepath, name):
        self.start_time = datetime.datetime.now()
        self.file_path = filepath
        self.name = name
        self.character_count = None
        self.sms_mean = None
        self._all_punctuation = r"""!"#$%&'()*+,./:;<=>?@[\]^_`{|}~"""
        self.end_time = None

    @property
    def filename(self):
        return os.path.join(self.file_path, self.name)

    @filename.setter
    def filename(self, val):
        import os
        if os.path.exists(val):
            return val
        else:
            assert "Enter a valid file"

    @property
    def regexp(self):
        return self._all_punctuation

    @regexp.setter
    def regexp(self, value):
        self._all_punctuation = value

    def count_it(self, sms_content):
        return "".join(re.findall(rf'[^a-zA-Z\s0-9\{self._all_punctuation}]+', sms_content)).__len__()

    def read_data(self):
        return pd.read_csv(self.filename, sep=',')

    def get_stats(self):
        dataframe = self.read_data()
        dataframe['character_count'] = (
                dataframe.content.apply(self.count_it) * 2
                + dataframe.content.str.len()
                - dataframe.content.apply(self.count_it))
        dataframe['sms_count'] = np.ceil(dataframe.character_count / 70)

        (self.character_count, self.sms_mean) = (dataframe.sms_count.sum(), dataframe.sms_count.mean())
        self.end_time = datetime.datetime.now()

    def __str__(self):
        if self.character_count is None:
            assert 'Get stats module must be initiated first.'
        return f'total_count:{self.character_count}, sms_mean:{self.sms_mean}'

    def get_run_time(self):
        return str(self.end_time - self.start_time)


if __name__ == '__main__':
    file_path = "."
    file_name = "smsCount.csv"
    count = Count(file_path, file_name)
    count.get_stats()
    print(count.get_run_time())
    print(count)
