Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r""C:/Users/RVUW291/Desktop/14prog_5ds_salaries.csv")
                 
SyntaxError: invalid decimal literal
df = pd.read_csv(r"C:/Users/RVUW291/Desktop/14prog_5ds_salaries.csv")
                 
df.columns
                 
Index(['work_year', 'experience_level', 'employment_type', 'job_title',
       'salary', 'salary_currency', 'salary_in_usd', 'employee_residence',
       'remote_ratio', 'company_location', 'company_size'],
      dtype='str')
df.skew(numeric_only=True)
                 
work_year        -1.016374
salary           28.937932
salary_in_usd     0.536401
remote_ratio      0.149454
dtype: float64
df.kurt(numeric_only=True)
                 
work_year           1.127965
salary           1147.567390
salary_in_usd       0.834006
remote_ratio       -1.925036
dtype: float64
sns.histplot(df["salary"])
                 
<Axes: xlabel='salary', ylabel='Count'>
plt.show()
                 
sns.histplot(df["salary"],kde=True)
                 
<Axes: xlabel='salary', ylabel='Count'>
plt.show()
                 
sns.distplot(df["salary"])
                 

Warning (from warnings module):
  File "<pyshell#12>", line 1
UserWarning: 

`distplot` is a deprecated function and will be removed in seaborn v0.14.0.

Please adapt your code to use either `displot` (a figure-level function with
similar flexibility) or `histplot` (an axes-level function for histograms).

For a guide to updating your code to use the new functions, please see
https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751

<Axes: xlabel='salary', ylabel='Density'>
>>> #b) Creating a pair plot for a DataFrame of 4laptops.csv
...                  
>>> import pandas as pd
>>> import seaborn as sns
>>> import matplotlib.pyplot as plt
>>> df2 = pd.read_csv(r"4laptops.csv")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    df2 = pd.read_csv(r"4laptops.csv")
  File "C:\Users\RVUW291\AppData\Roaming\Python\Python314\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\RVUW291\AppData\Roaming\Python\Python314\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\RVUW291\AppData\Roaming\Python\Python314\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\RVUW291\AppData\Roaming\Python\Python314\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Users\RVUW291\AppData\Roaming\Python\Python314\site-packages\pandas\io\common.py", line 926, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: '4laptops.csv'
>>> df2 = pd.read_csv(r"C:/Users/RVUW291/Desktop/10prog_4laptops.csv")
>>> sns.pairplot(df2)
<seaborn.axisgrid.PairGrid object at 0x00000239460797F0>
>>> plt.show()
