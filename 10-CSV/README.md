Rule with parameter and return.

```
% antlr4py3 CSV.g4

% python test_csv.py users.csv
{}
header: 'User,  Name,    Dept'
{'Dept': '101', 'Name': 'Terence', 'User': 'parrt'}
{'Dept': '020', 'Name': 'Tom', 'User': 'tombu'}
{'Dept': '008', 'Name': 'Kevin', 'User': 'bke'}
3 rows
row token interval: (6, 11)
row token interval: (12, 17)
row token interval: (18, 23)
```