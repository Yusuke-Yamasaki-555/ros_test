#!/usr/bin/env python3
import rospy

'''

　　このプログラムは、『ROSで始めるロボットプログラミング』(小倉＿崇　著)の第８章の内容に沿っている
　  『kobuki』というロボットのシュミレータのインストールが必要
　　このコンピュータには、インストールされていないため、このプログラムは動作しない

    が、Topicの内容を変更し、turtlesimで動くようにした
    　（turtlesimの起動：$ rosrun turtlesim turtlesim_node）
    kobuki専用の箇所は、dicstringで記述している

    コードの参考として、このプログラムを残す

'''

from geometry_msgs.msg import Twist
# Twistは、並進の速度と回転の速度を合わせたもの。ロボットの速度を命令するのによく使われる

rospy.init_node('vel_Publisher')

""" pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10) """
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
# PublisherのTopic名の指定

while not rospy.is_shutdown():
    vel = Twist()
    direction = input('f: forward, b: backward, l: left, r: right > ')
    #キーボード入力を受け付ける
    #raw_inputはpythonの標準関数、入力があるまでプログラムをブロックする
    #エンターキーが入力されるまでに入力された文字列が、directionに入る

    if 'f' in direction:
        vel.linear.x = 0.5
    if 'b' in direction:
        vel.linear.x = -0.5
    if 'l' in direction:
        vel.angular.z = 1.0
    if 'r' in direction:
        vel.angular.z = -1.0
    if 'q' in direction:
        break
    # '' 内の文字列が入力の文字列に含まれていたら、if文内を実行する（ROSはSI単位系を採用している為、単位は、x:[m/s] z:[rad/s]）

    print(vel)
    pub.publish(vel)