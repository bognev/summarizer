# 

##Input
Pandas dataframe and options to customize output, for example:
* output_type - markdown, html or xlsx
* out filename
* report - 0 - to string, 1 - to file

##Task description
The program should take pandas dataframe as input, iterate through each of the columns in the
dataframe and based on column datatype, create summary statistics for each, and print them out
in a table.
Calculated summary could include following items:
* column type
* min, max
* mean, median, mode
* percent of zero rows
* variance and standard deviation
* interquartile range and coefficient of variation
* number of distinct values 


##Output
A markdown, html or xlsx report with summary statistics

|       |  # sepal length (cm) |  # sepal width (cm) |   # petal length (cm) | #  petal width (cm) |  #   target |
|:------|--------------------:|-------------------:|--------------------:|-------------------:|-----------:|
| count |          150        |         150        |            150      |         150        | 150        |
| mean  |            5.84333  |           3.05733  |              3.758  |           1.19933  |   1        |
| std   |            0.828066 |           0.435866 |              1.7653 |           0.762238 |   0.819232 |
| min   |            4.3      |           2        |              1      |           0.1      |   0        |
| 25%   |            5.1      |           2.8      |              1.6    |           0.3      |   0        |
| 50%   |            5.8      |           3        |              4.35   |           1.3      |   1        |
| 75%   |            6.4      |           3.3      |              5.1    |           1.8      |   2        |
| max   |            7.9      |           4.4      |              6.9    |           2.5      |   2        |

## How to run
```bash
git clone https://github.com/bognev/summarizer.git
cd summarizer
python -m pip install ./dist/summarizer_package-0.1.0.tar.gz
chmod +x run.sh && ./run.sh
```
or 
```bash
report=1
out="report"
output_type="markdown"
python -u main.py  --report=$report --out=$out --output_type=$output_type
```