#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor
import sys

grammar = """

#grammar HTML

    document    =   (tag / anyword)*
#    document   =   (doctype / text / tag)*
#    tag         =   open_tag (text / tag)* close_tag
    open_tag    =   "<" ~"[\w\W]" ">"
#    close_tag   =   "</" ~"[\w\W]+" ">"
#    doctype     =   "<!DOCTYPE " ~"[\w\W]+" ">"
#    text        =   ~"[^<]+"

#tag = ~"<([a-z]+)([^<]+)*(?:>(.*)<\/\1>|\s+\/>)"
tag = ~"<([A-Z][A-Z0-9]*)\b[^>]*>(.*?)</\1>"

anyword = ~"[\w\W]*" ws*
ws = ~"[\s]+"

"""




class EntryVisitor(NodeVisitor):
    
    def __init__(self, grammar, text):
        self.entry = {}
        ast = Grammar(grammar).parse(text)
        self.visit(ast)
    
    def visit_text(self, n, vc):
        self.entry['text'] = n.text
    
    def visit_doctype(self, n, vc):       
        self.entry['doctype'] = n.text
    
#    def visit_anyword(self, n, vc):       
#        self.entry['anyword'] = n.text
    
#    def visit_variable(self, n, vc):
#        self.entry['variable'] = n.text        
    
#    def visit_literal(self, n, vc):
#        self.entry['literal'] = n.text        
    
    def generic_visit(self, n, vc):
        pass
        
        
grammar = Grammar(grammar)


filename = sys.argv[1]
with open(filename) as file:
    contents = file.read()


print( grammar.parse(contents) )


#print(contents)
#EntryVisitor(grammar, contents).entry

print( EntryVisitor(grammar, contents).entry )
#




#for line in calc_text.splitlines():
    
#    print( EntryVisitor(grammar, line).entry )

#for line in text.splitlines():
#    print( EntryParser(grammar, line).entry )