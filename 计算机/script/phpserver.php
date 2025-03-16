<?php
// php web服务器


// 作为测试用
function test()
{
    $a = $_GET;
    print_r($a);
}


// 返回字符串
function getstring()
{
    echo "hello,this is phpserver.php";
}

// test();
getstring();