<?php

namespace think;

use think\initializer\RegisterService;

class App
{
    public static function run()
    {
        echo 'Hello, ThankPHP!';
    }

    protected $initializers=[
        RegisterService::class
    ];
}