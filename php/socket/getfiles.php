<?php

$root = '/etc';

$iter = new RecursiveIteratorIterator(
    new RecursiveDirectoryIterator($root, RecursiveDirectoryIterator::SKIP_DOTS),
    RecursiveIteratorIterator::SELF_FIRST,
    RecursiveIteratorIterator::CATCH_GET_CHILD // Ignore "Permission denied"
);

$paths = array($root);
foreach ($iter as $path => $dir) {
    if ($dir->isDir()) {
        $paths[] = $path;
    }
}

print_r($paths);


//glob
