# Parse CSV file

```
% type t.csv
Details,Month,Amount
Mid Bonus,June,"$2,000"
,January,"""zippo"""
Total Bonuses,"","$5,000"

% python CSV_Loader.py t.csv
(top 
  (hdr 
    (row 
      (field Details) , 
      (field Month) , 
      (field Amount) \r \n)) 
  (row (field Mid Bonus) , (field June) , (field "$2,000") \r \n) 
  (row field , (field January) , (field """zippo""") \r \n) 
  (row (field Total Bonuses) , (field "") , (field "$5,000") \r \n))

Start Walking...
result = [
{'Month': 'June','Details': 'Mid Bonus', 'Amount': '"$2,000"'}, 
{'Month': 'January', 'Details': '', 'Amount': '"""zippo"""'}, 
{'Month': '""', 'Details': 'Total Bonuses', 'Amount': '"$5,000"'}
]
```

