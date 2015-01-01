<?php
$st = get_declared_classes();

require_once '../docparser/Sami/Parser/DocBlockParser.php';
require_once '../docparser/Sami/Parser/ParserContext.php';
require_once '../docparser/Sami/Parser/Filter/FilterInterface.php';
require_once '../docparser/Sami/Parser/Filter/TrueFilter.php';
require_once '../docparser/Sami/Parser/Node/DocBlockNode.php';

require_once '../docparser/vendor/autoload.php';


/*require_once '../docparser/vendor/phpdocumentor/reflection-docblock/src/phpDocumentor/Reflection/DocBlock/Tag.php';

foreach (glob("../docparser/vendor/phpdocumentor/reflection-docblock/src/phpDocumentor/Reflection/DocBlock/Tag/*.php") as $filename)
{
    echo $filename;
    require_once $filename;
}

require_once '../docparser/vendor/phpdocumentor/reflection-docblock/src/phpDocumentor/Reflection/DocBlock.php';
require_once '../docparser/vendor/phpdocumentor/reflection-docblock/src/phpDocumentor/Reflection/DocBlock/Context.php';
require_once '../docparser/vendor/phpdocumentor/reflection-docblock/src/phpDocumentor/Reflection/DocBlock/Description.php';
require_once '../docparser/vendor/phpdocumentor/reflection-docblock/src/phpDocumentor/Reflection/DocBlock/Location.php';*/


//require_once '../docparser/vendor/phpdocumentor/reflection-docblock/src/phpDocumentor/Reflection/DocBlock/Tag/ParamTag.php';








class TestClass {
    /**
     * This is the short description.
     *  
     * This is the 1st line of the long description 
     * This is the 2nd line of the long description 
     * This is the 3rd line of the long description   
     *  
     * @param bool|string $foo sometimes a boolean, sometimes a string (or, could have just used "mixed")
     * @param bool $bar sometimes a boolean, sometimes an int (again, could have just used "mixed") 
     * @return string de-html_entitied string (no entities at all)
     */
    public function another_test($foo, $bar) {
        return strtr($foo,array_flip(get_html_translation_table(HTML_ENTITIES)));
    }
}

use Sami\Parser\DocBlockParser;
use Sami\Parser\ParserContext;
use Sami\Parser\Filter\FilterInterface;
use Sami\Parser\Filter\TrueFilter;
use Sami\Parser\Node\DocBlockNode;


$res = array_values(array_diff_key(get_declared_classes(),$st));
print_r($res);
print_r($st);

try {
    $method = new ReflectionMethod('TestClass', 'another_test');
    $comment = $method->getDocComment();
    if ($comment !== FALSE) {
        
        
        
        
        $docBlockParser = new DocBlockParser();
        $f = new TrueFilter();
        $context = new ParserContext($f, $docBlockParser, FALSE);
        
 
        $doc = $docBlockParser->parse($comment,$context);
        echo "\n** getDesc:\n";
        print_r($doc->getDesc());
        echo "\n** getTags:\n";
        print_r($doc->getTags());
        echo "\n** getTag('param'):\n";
        print_r($doc->getTag('param'));
        echo "\n** getErrors:\n";
        print_r($doc->getErrors());
        echo "\n** getOtherTags:\n";
        print_r($doc->getOtherTags());
        echo "\n** getShortDesc:\n";
        print_r($doc->getShortDesc());
        echo "\n** getLongDesc:\n";
        print_r($doc->getLongDesc());
    }
} catch (Exception $e) {
    print_r($e);
}

?>
