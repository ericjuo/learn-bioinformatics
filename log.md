# My Learning Log
## Format
### DATE, 2021
#### Today's Progress:

#### Thoughts:

#### Link to work:

#### Resources:
---
## [2021](#2021)
### Febuary 2, 2021
#### Today's Progress:
- Learned to use `git stash -u` and `git stash pop`. It's very useful when switch between tasks.
- VS code is a good alternative of Jupyter notebook. By typing `# %%`, VS code will create a cell just like jupyter notebook. Press `Shift` + `Enter` to run code in the cell.
- Learned to create sqlite3 database and read sql with pandas by `pd.read_sql("SELECT * FROM table", conn)`
- Write multiple sheets in excel.
```python
with pd.Excelwriter('file.xlsx') as writer:
    df1.to_excel(writer, sheet_name = 'Sheet 1')
    df2.to_excel(writer, sheet_name = 'Sheet 2')
```
- Learned skewness of dataset. There are three types of skewness, left skew, symmetric and right skew. Left skew indicates a long left tail in the data distribution; right skew indicates a long right tail in the data distribution.
#### Thoughts:
Today I am writing code to analyse stability data of ELISA kit. It involves calculation of percent recovery, sample to positive (S/P) value and positive-to-negative value, and then assess if these values conforms to the validation criteria. Although it is convient using pandas dataframe for calculation directly, I think I can write better code using class and function features instead of just dataframe manipulation. Besides, I found `df.loc` function has been modified in lastest version of pandas. I should carefully read the document of df.loc.
#### Link to work:

#### Resources:
- https://gitbook.tw/chapters/faq/stash.html
- https://code.visualstudio.com/docs/python/jupyter-support-py
- https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html
- https://docs.python.org/3/library/sqlite3.html
- https://stackoverflow.com/questions/42370977/how-to-save-a-new-sheet-in-an-existing-excel-file-using-pandas

---
### Febuary 1, 2021

#### Today's Progress:
- Compeleted readings of Chapter 1 of OpenIntro Statistics. I learned that there are 4 typing of sampling, they are simple random sampling, stratified sampling, cluster sampling and multistage sampling.
- Also there are 4 principles of experiment design, including controlling, randomization, replication and blocking.
- Without random sampling, the sample can not be generalized to the population. Without random assignment, the experiment can not be concluded as causative. A good experiment design should include random sampling and random assignment.
#### Thoughts:
At first, I was confused between controlling and blocking, but then I realized that controlling is to control variations other than treatments; while blocking is to group by variations are not treaments and can not be controlled.

#### Resources:
- Diez D., Cetinkaya-Rundel M., Barr C. D. OpenIntro Statistics Fourth Edition. 2019. 
---