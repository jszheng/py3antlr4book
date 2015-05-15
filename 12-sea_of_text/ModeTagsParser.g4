parser grammar ModeTagsParser;

options { tokenVocab=ModeTagsLexer; } // use tokens from ModeTagsLexer.g4

entry: (tag | TEXT)* ;

tag : '<' ID '>'
    | '<' '/' ID '>'
    ;
