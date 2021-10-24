#!/usr/bin/env python3

'''
  このプログラムは、Subscriberの位置づけにある
  　Publisher : talker.py
'''

import rospy
from std_msgs.msg import String

#  受信側も同じようにstd_msgs/String型を必要とする

def callback(message):
#この関数の引数には、結果としてstd_msgs/String型のインスタンスが入る
    rospy.loginfo("I heard %s", message.data)
    #  基本的に、文字列を表示するだけ。結果はROSのTopicとしてPublishされてもいる。ネットワークを通じて確認できる
    
rospy.init_node('listener')

# while not rospy.is_shutdown():
sub = rospy.Subscriber('chatter', String, callback)
#  chatterという名前でstd_msgs/String型のTopicを、subscribeし、受信したデータをcallbackする関数を実行している

rospy.sleep(0.1)
#  spiin()で無限ループしながら受信を待つ。受信をしたらcallback関数が呼ばれる