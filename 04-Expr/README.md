# How to run
```
% pygrun Expr prog --tree t.expr
(prog
   (stat
      (expr 193) \n)
   (stat a =
      (expr 5) \n)
   (stat b =
      (expr 6) \n)
   (stat
      (expr
         (expr a) +
         (expr
            (expr b) *
            (expr 2))) \n)
   (stat
      (expr
         (expr (
            (expr
               (expr 1) +
               (expr 2)) )) *
      (expr 3)) \n))
      
% python test_Expr.py t.expr
(prog 
  (stat (expr 193) \n) 
  (stat a = (expr 5) \n) 
  (stat b = (expr 6) \n) 
  (stat (expr (expr a) + (expr (expr b) * (expr 2))) \n) 
  (stat (expr (expr ( (expr (expr 1) + (expr 2)) )) * (expr 3)) \n)
)
```