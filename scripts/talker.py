#!/usr/bin/env python3
#  pythonで実行するファイルを作るための「お決まり」
#恐らく、python3が格納されている場所を書いている。たぶん

'''
  このプログラムは、Publisherの位置づけとなっている
  　Subscriber : listener.py
'''

import rospy
#  rospy(ROSでpythonを使うためのライブラリ。必ず)というモジュールをインポート

from std_msgs.msg import String
#  std_msgsというパッケージからStringというMessage型をインポート
#std_msgs/StringというMessage型を表している。この型でTopicをPublishするのに使う

rospy.init_node('talker')
#  pythonでrosのプログラムを書くとき、最初に書くもの（これをしないとrosの通信が一切できない）
#talkerという名前のrosノードになる。これを実行することで、ROSMasterに名前が登録される

pub = rospy.Publisher('chatter', String, queue_size=10)
#  Publisherを作っている。chatterという名前で、std_msgs/String型のTopicにPublishするPublisherを作っている
#queue_size=10は、バッファとして１０つ値を保持する、という意味

rate = rospy.Rate(10)
#  10Hz(毎秒１０回)で定期的にプログラムを実行するための、Rateというクラスのインスタンスを作っている

while not rospy.is_shutdown():
#  プログラムがCtrl+cで終了されるまでの無限ループを記述している
#rospy.is_shutdown()は、Ctrl+cが押されたときや、外部から終了命令が出たときにTrueになる＝無限ループから外れる
#プログラム中では、これを使って正常終了できるようにしておく必要がある

    hello_str = String()
    #  実際に送信するStringのメッセージを、Stringクラスから作る

    hello_str.data = "Hello ROS!!! %s" % rospy.get_time()
    #  作ったhello_strの内容を書き込む
    #hello_strのdataというメンバ変数に書き込んでいる
    r=rospy.Rate(100)
    '''
    上記のコードを書くには、std_msgs/Stringの構造を知っておく必要がある
    ROSのMessage型は、rosmsg showコマンドで調べられる
    今回の場合、$ rosmsg show std_msgs/String
    結果、string data（＝dataという名前の変数を持ち(=メンバ変数)、その型はstring）(=.dataをつければ、文字列を変数に代入できる)
    '''

    pub.publish(hello_str)
    rate.sleep()
    #  予め作っておいたPublisherであるpubを使って(行15)、ROSのメッセージであるhello_strをPublish(送信)している
