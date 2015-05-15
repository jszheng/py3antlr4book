__author__ = 'jszheng'

import sys
from collections import OrderedDict
from string import Template

from antlr4 import *
from antlr4.InputStream import InputStream

from CymbolLexer import CymbolLexer
from CymbolParser import CymbolParser
from CymbolListener import CymbolListener


class Graph:
    def __init__(self):
        self.nodes = OrderedDict()
        self.edges = OrderedDict()

    def add_edge(self, src, dst):
        if src in self.edges:
            self.edges[src].append(dst)
        else:
            self.edges[src] = [dst]

    def add_node(self, function_name):
        self.nodes[function_name] = True

    def __str__(self):
        return "edges : " + self.edges.__str__() + ", functions :　" + list(self.nodes.keys()).__str__()

    def toDOT(self):
        # funcs = ';'.join(self.nodes.keys())
        funcs = ""
        for f in self.nodes.keys():
            funcs += f + ';'
        edges = ""
        for (key, value) in self.edges.items():
            for dst in value:
                edges += "  " + key + " -> " + dst + ";\n"

        tpl_str = """
digraph G {
  ranksep=.25;
  edge [arrowsize=.5]
  node [shape=circle, fontname="ArialNarrow",
        fontsize=12, fixedsize=true, height=.45];

  $func_list
$edge_list
}
"""
        tpl = Template(tpl_str)
        return tpl.substitute(func_list=funcs, edge_list=edges)


class FunctionListener(CymbolListener):
    def __init__(self):
        self.graph = Graph()
        self.current_function_name = None

    def enterFunctionDecl(self, ctx: CymbolParser.FunctionDeclContext):
        name = ctx.ID().getText()
        self.current_function_name = name
        self.graph.add_node(name)

    def exitCall(self, ctx):
        name = ctx.ID().getText()
        self.graph.add_edge(self.current_function_name, name)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())

    lexer = CymbolLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CymbolParser(token_stream)
    tree = parser.top()

    # lisp_tree_str = tree.toStringTree(recog=parser)
    # print(lisp_tree_str)

    walker = ParseTreeWalker()
    collector = FunctionListener()
    walker.walk(collector, tree)
    # print(collector.graph)
    print(collector.graph.toDOT())

