# Parse CSV file

```
% type t.csv
Details,Month,Amount
Mid Bonus,June,"$2,000"
,January,"""zippo"""
Total Bonuses,"","$5,000"

% python CSV_Loader.py t.csv
Start Walking...
result = [
{'Month': 'June','Details': 'Mid Bonus', 'Amount': '"$2,000"'}, 
{'Month': 'January', 'Details': '', 'Amount': '"""zippo"""'}, 
{'Month': '""', 'Details': 'Total Bonuses', 'Amount': '"$5,000"'}
]
```

