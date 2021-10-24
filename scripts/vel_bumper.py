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

""" from kobuki_msgs.msg import BumperEvent """

rospy.init_node('vel_bumper')
vel_x = rospy.get_param('~vel_x', 0.5)
vel_rot = rospy.get_param('~vel_rot', 1.0)
# 上２行は、ROSのParameterの仕組みを使って速度をセットするための変数の定義

""" pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10) """
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
# PublisherのTopic名の指定

def callback(bumper):
    #callbackという関数の定義(この関数はsubが実行されない限り呼ばれないため、このプログラムでは一度も実行されない)
    print(bumper)
    #必須ではない引数の表示
    back_vel =Twist()
    back_vel.linear.x = -vel_x
    #後退するようにback_velのlinear.xに負の進行速度を代入
    r = rospy.Rate(10.0)
    for i in range(5):# 後退を0.5s(多分)継続
        pub.publish(back_vel)
        r.sleep()

""" sub = rospy.Subscriber('/mobile_base/events/bumper', BumperEvent, callback, queue_size = 1) """
# /mobile_base/events/bumperという名前でBumperEvent型のTopicを読み、受信したデータについて、callback関数を呼び出す

while not rospy.is_shutdown():
    vel = Twist()
    direction = input('f: forward, b: backward, l: left, r: right > ')
    #キーボード入力を受け付ける
    #raw_inputはpythonの標準関数、入力があるまでプログラムをブロックする
    #エンターキーが入力されるまでに入力された文字列が、directionに入る

    if 'f' in direction:
        vel.linear.x = vel_x
    if 'b' in direction:
        vel.linear.x = -vel_x
    if 'l' in direction:
        vel.angular.z = vel_rot
    if 'r' in direction:
        vel.angular.z = -vel_rot
    if 'q' in direction:
        break
    # '' 内の文字列が入力の文字列に含まれていたら、if文内を実行する（ROSはSI単位系を採用している為、単位は、x:[m/s] z:[rad/s]）

    print(vel)
    r = rospy.Rate(10.0)
    for i in range(10):# 代入された行動を1s継続
        pub.publish(vel)
        r.sleep()