<?php
namespace app\index\controller;

use think\Controller;
use think\Db;
class Index extends Controller
{
    public function index()
    {
        $data = Db::name('data')->select();
        return $this->fetch();
    }
    public function upload_file( $form )
    {
        return json_encode($form);
    }
}