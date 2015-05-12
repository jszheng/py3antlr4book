SET CLASSPATH=%~dp0antlr4-4.5.1-complete.jar;.
doskey antlr4=java org.antlr.v4.Tool $*
doskey grun=java org.antlr.v4.runtime.misc.TestRig $*
doskey antlr4py3=java org.antlr.v4.Tool -Dlanguage=Python3 $*
doskey antlr4py2=java org.antlr.v4.Tool -Dlanguage=Python2 $*
doskey antlr4vpy3=java org.antlr.v4.Tool -Dlanguage=Python3 -no-listener -visitor $*
doskey antlr4vpy2=java org.antlr.v4.Tool -Dlanguage=Python2 -no-listener -visitor $*
doskey pygrun=python %~dp0pygrun $*

