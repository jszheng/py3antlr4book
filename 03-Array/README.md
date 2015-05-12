# Introduction
This example shows how to use listener to do simple translation of input array.

# How to run
```
% antlr4py3 ArrayInit.g4
% pygrun ArrayInit init --tree input.txt
[@0,0:0='{',<1>,1:0]
[@1,1:2='99',<4>,1:1]
[@2,3:3=',',<2>,1:3]
[@3,5:5='3',<4>,1:5]
[@4,6:6=',',<2>,1:6]
[@5,8:10='451',<4>,1:8]
[@6,11:11='}',<3>,1:11]
[@7,12:11='<EOF>',<-1>,1:12]

% pygrun ArrayInit init --tokens input.txt
(init {
   (value 99) ,
   (value 3) ,
   (value 451) })

% python test_array.py input.txt
(init { (value 99) , (value 3) , (value 451) })
"\u0063\u0003\u01c3"

```