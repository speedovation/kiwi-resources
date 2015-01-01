from arpeggio import PTNodeVisitor
from PythonQt import *
from PythonQt.QtGui import QStandardItemModel
from PythonQt.QtGui import QStandardItem

class Visitor(PTNodeVisitor):

    
    def __init__(self, defaults=True, debug=False, api=""):
        super().__init__(defaults, debug)

        #blank entry is global namespace
        self.namespace = { '': '' }
        self.classes = { }
        self.functions = []
        
        #default is blank that is global namespace
        self.current_namespace = ''
        self.current_class = ''
        self.api = api
        
        filename = api.filepath()
        m = api.outlineModel()
        m.clean(m)
        
        #m.insertRow(2, QStandardItem("d->fileInfo()- TTTT"))
        

    def visit_namespace(self, node, children):
        print (" namespace name" )
        #print (children)
        self.classes = {}
        self.functions = []
        n = children[0].replace('\\\\','\\')
        self.namespace[n] = self.classes
        self.current_namespace = n
        
        ### Inserting namespace in outline DOM model
        self.api.updateOutlineModel(n)
        

    def visit_abstractclass(self, node, children):
        #print (" class name" )
#        print (children)
#        self.functions = []
#        self.classes[ children[1] ] = self.functions
#        
#        self.namespace[ self.current_namespace] = self.classes
        pass
#"this is will %d dsds asad "
        
    def visit_class(self, node, children):
#        print (" class name" )
#        print (children)
        self.functions = []
        self.classes[ children[0] ] = self.functions
        
        self.namespace[ self.current_namespace] = self.classes 
        
        ### Inserting namespace in outline DOM model
        self.api.updateOutlineModel(children[0],1)    

    def visit_classfunction(self, node, children):
        """
            Removes parenthesis if exists and returns what was contained inside.
        """
        #print ("Class Function name")
        #print (node)
        #print(children)
        
        # This will set visibility in front of functions 
        #print (node)
#        print (children[0])
        #self.functions.append ( children[0] )
    
    def visit_function(self, node, children):
        """
            Removes parenthesis if exists and returns what was contained inside.
        """
        #print ("Function name")
        #print(children)
        #print (node)

        ### Inserting function in outline DOM model
        self.api.updateOutlineModel(children[0], 2)
        
        self.functions.append ( children )
        
    def visit_comment(self, node, children):
        #print ( "Comments starts" )
        #print ( children )
        #print (node)
        #print ( "Comments ends" )
        pass
        
    def visit_nonspace(self, node, children):
        #print ( "Comments starts" )
#        print ("Nonspace")
#        print (node)
        pass

    def visit_arguments(self, node, children):
        #print ( "Comments starts" )
#        print ("Nonspace")
#        print (node)
        pass
        
    def visit_argument(self, node, children):
        #print ( "Comments starts" )
#        print ("Nonspace")
#        print (node)
        pass
