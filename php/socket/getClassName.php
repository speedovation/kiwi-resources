<?php 

require_once "parser.php";

$file = "samplec.php";

/*$fp = fopen($file, 'r');
$class = []; 
$buffer = '';
$i = 0;
while (!$class) {
    if (feof($fp)) break;

    $buffer .= fread($fp, 512);
    $tokens = token_get_all($buffer);
	
	print_r($tokens);

    if (strpos($buffer, '{') === false) continue;

    for (;$i<count($tokens);$i++) {
        if ($tokens[$i][0] === T_CLASS) {
            for ($j=$i+1;$j<count($tokens);$j++) {
                if ($tokens[$j] === '{') {
                    $class[] = $tokens[$i+2][1];
                }
            }
        }
    }
}
*/
$content = file_get_contents($file);

$p = new Parser($content);
$r = $p->parseSource();

print_r($r);

