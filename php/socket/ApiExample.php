<?php

require_once "KiWiApi.php";

$api = new KiWiApi();

/*$api->callApi( 'openFile', ["QString"=>"/home/yash/Projects/xdebug/SublimeXdebug/Xdebug.py"] );*/


//Update current outline line
$api->callApi( 'updateOutlineModel', ["QString"=>"DATA"] );
