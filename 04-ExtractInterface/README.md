# How to Run
```
% python test_extract.py Demo.java
interface IDemo {
        int f(int x, String y);
        int[ ] g(/*no args*/);
        List<Map<String, Integer>>[] h();
}
```

# to make this test pass for python
- use the latest JAVA g4 file from ANTLR4 grammar depot
- comment out java action part for unicode
```antlr4
fragment
JavaLetter
    :   [a-zA-Z$_] // these are the "java letters" below 0xFF
//    |   // covers all characters above 0xFF which are not a surrogate
//        ~[\u0000-\u00FF\uD800-\uDBFF]
//        {Character.isJavaIdentifierStart(_input.LA(-1))}?
//    |   // covers UTF-16 surrogate pairs encodings for U+10000 to U+10FFFF
//        [\uD800-\uDBFF] [\uDC00-\uDFFF]
//        {Character.isJavaIdentifierStart(Character.toCodePoint((char)_input.LA(-2), (char)_input.LA(-1)))}?
    ;

fragment
JavaLetterOrDigit
    :   [a-zA-Z0-9$_] // these are the "java letters or digits" below 0xFF
//    |   // covers all characters above 0xFF which are not a surrogate
//        ~[\u0000-\u00FF\uD800-\uDBFF]
//        {Character.isJavaIdentifierPart(_input.LA(-1))}?
//    |   // covers UTF-16 surrogate pairs encodings for U+10000 to U+10FFFF
//        [\uD800-\uDBFF] [\uDC00-\uDFFF]
//        {Character.isJavaIdentifierPart(Character.toCodePoint((char)_input.LA(-2), (char)_input.LA(-1)))}?
    ;
- change type to datatype to avoid conflict with python keyword.
```
- add function to print the original text (including hidden channel)
```python
    def getAllText(self, ctx):  # include hidden channel
        token_stream = ctx.parser.getTokenStream()
        lexer = token_stream.tokenSource
        input_stream = lexer.inputStream
        start = ctx.start.start
        stop = ctx.stop.stop
        return input_stream.getText(start, stop)
```