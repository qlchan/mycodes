       header("Content-type:application/vnd.ms-excel");
       header("Content-Disposition:attachment;filename=money10.xls");
                //输出内容如下： 
                echo   "已领取金额"."\t"; 
                echo   "可领取金额"."\t"; 
                echo   "概率值"."\t"; 
                echo   "\n";
                $moneys = array(0, 1, 6, 10);
                $money = 10;
                for($i=0; $i<1000000; $i++) {
                    $arr = MsTopicRedPacketHelper::getRedPacketCash($money);
                    echo   $money."\t"; 
                    echo   $arr[0]."\t"; 
                    echo   $arr[1]."\t"; 
                    echo   "\n";
                   // echo MsTopicRedPacketHelper::getRedPacketCash($money).'<br>';
                }

