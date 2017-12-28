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
    public function down_load()
    {
       
    }
    public function show_dir()
    {
        $filepath ='C:\Users\Administrator\Desktop\nntg\data';
        if (is_dir($filepath)) {                //检测是否是一个目录
            $dir =scandir($filepath);
            $ret = Array();
            foreach ($dir as $value){
                $curpath = $filepath . "\\" . $value;
                if (is_dir($curpath))
                    continue;
                $fileinfo = Array("name"=>""); //创建信息数组
                $handle = fopen($curpath,'r');
                $fstat = fstat($handle);
                $fileinfo['filename'] = $value;
                $fileinfo['size'] = round($fstat["size"]/1024,2);
                array_push($ret,$fileinfo);
            }
            $this->assign("ret",$ret);
            return $this->fetch();
        }
        else
        {
            return "error";
        }
    }
}