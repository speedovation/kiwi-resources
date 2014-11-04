#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor


sample1 = """public function
<?php
class Enum {
    protected $self = array();
    public function __construct( ) {}
    public function __construct( $fun ) {
        $args = func_get_args();
        for( $i=0, $n=count($args); $i<$n; $i++ )
            $this->add($args[$i]);
    }
   
    public function __get(  $name = null ) {
        return $this->self[$name];
    }
   
    public function add(  $name = null,  $enum = null ) {
        if( isset($enum) )
            $this->self[$name] = $enum;
        else
            $this->self[$name] = end($this->self) + 1;
    }


"""






calc_grammar = """

#calc = argument*
calc =  ( function / variable / symbol / anyword )* 

function = visibility ws* function_keyword ws* functionname ws* arguments* ws* block
block = "{" ws* ~"[^}]*" ws* "}"
arguments = "(" ws* argument* ws* ")"
function_keyword = "function"
functionname = word

#$types = array("cappuccino")
#arguments end with optional comma
argument = ( byvalue / byreference ) ws* ("=" ws* value )* ws* ","* ws*
byreference = "&" variable
byvalue = variable

#value may be variable or array or string or any php type
value = ( variable / word )

visibility = "public" / "protected" / "private"
variable = ~"\$[a-zA-z]+[a-zA-Z0-9_]*"
word = ~"[a-zA-Z0-9_]+"
literal = ~"[a-zA-Z]+"


comment = ~"('//.*')|('/\*.*\*/')"
symbol = ~"[\W]+"

anyword = ~"[\w]*" ws*
ws = ~"[\s]+"


"""



calc_text = """\
4+5
4+6+(4*7) ssgs $ddd
gdj
$some
$1some
$some676GH
  
"""


class EntryVisitor(NodeVisitor):
    
    def __init__(self, grammar, text):
        self.entry = {}
        self.variables = []
        self.function = []
        self.visibility = []
        self.test = []
        ast = Grammar(grammar).parse(text)
        self.visit(ast)
    
    def visit_number(self, n, vc):
        self.entry['number'] = n.text
    
#    def visit_expression(self, n, vc):       
#        self.entry['expression'] = n.text

    def visit_byvalue(self, n, vc):
        print ("byvalue" + n.text)
        self.entry['byvalue'] = n.text
        
    def visit_arguments(self, n, vc):
        self.entry['arguments'] = n.text

    def visit_function(self, n, vc):
        self.entry['function'] = n.text

    def visit_visibility(self, n, vc):
        self.entry['visibility'] = n.text
    
    def visit_anyword(self, n, vc):       
        self.entry['anyword'] = n.text
    
    def visit_variable(self, n, vc):
        self.variables.append( n.text)    
    
    def visit_visibility(self, n, vc):
        self.visibility.append( n.text)    
        self.entry['visibility'] = n.text
    
    def visit_word(self, n, vc):
        self.function.append( n.text)    
        self.entry['functionname'] = n.text

    def visit_test(self, n, vc):
        self.test.append( n.text)    
        self.entry['test'] = n.text
    
#    def visit_literal(self, n, vc):
#        self.entry['literal'] = n.text        
    
    def generic_visit(self, n, vc):
        pass
        
        
grammar = Grammar(calc_grammar)
#print( grammar.parse(input) )

sample2 = """$name = null, $name = null"""


input = sample1

res = EntryVisitor(calc_grammar, input)

print( res.entry )
#print( res.variables )
print( res.function )
#print( res.visibility )
#print( res.test )


#for line in calc_text.splitlines():
    
#    print( EntryVisitor(calc_grammar, line).entry )

#for line in text.splitlines():
#    print( EntryParser(grammar, line).entry )