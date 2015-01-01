
<?php
error_reporting(E_ALL);

echo "<h2>TCP/IP Connection</h2>\n";

/* Get the port for the WWW service. */
$service_port = 9040;

/* Get the IP address for the target host. */
$address = "127.0.0.1";

/* Create a TCP/IP socket. */
$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
if ($socket === false) {
    echo "socket_create() failed: reason: " . socket_strerror(socket_last_error()) . "\n";
} else {
    echo "OK.\n";
}

echo "Attempting to connect to '$address' on port '$service_port'...";
$result = socket_connect($socket, $address, $service_port);
if ($result === false) {
    echo "socket_connect() failed.\nReason: ($result) " . socket_strerror(socket_last_error($socket)) . "\n";
} else {
    echo "OK.\n";
}

$in = "HEAD / HTTP/1.1\r\n";
$in .= "Host: www.example.com\r\n";
$in .= "Connection: Close\r\n\r\n";
$out = '';

$a = [
       "name"   => "filepath",
       "args"   => ["int"=>"1"],
       "return" => TRUE,
     ];

$b = [
       "name"   => "openFile",
       "args"   => ["QString"=>"/home/yash/Projects/xdebug/SublimeXdebug/Xdebug.py"],
       "return" => TRUE,
     ];

$b = [
       "name"   => "openFile",
       "args"   => ["QString"=>"/home/yash/Projects/xdebug/SublimeXdebug/Xdebug.py"],
       "return" => TRUE,
     ];

$in = json_encode($b);

echo "Sending HTTP HEAD request...";
socket_write($socket, $in, strlen($in));
echo "OK.\n";

echo "Reading response:\n";
while ($out = socket_read($socket, 9040)) {
    echo $out;
}

echo "Closing socket...";
socket_close($socket);
echo "OK.\n\n";
?>
