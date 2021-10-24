#!/usr/bin/env python3

import rospy
import actionlib
from ros_test.msg import TestActionAction, TestActionGoal, TestActionFeedback

def ActionClient():
    action_client = actionlib.SimpleActionClient( "test_action", TestActionAction )
    print( "action_client wait for server." )
    action_client.wait_for_server()
    goal = TestActionGoal()
    goal.pass_data = "hoge"
    action_client.send_goal( goal )
    print( "action_client's goal go." )
    print( "action_client wait for result." )
    action_client.wait_for_result()
    result = action_client.get_result()
    print( "action_client got result. " )
    if result:
        print( "Result is True." )
    else:
        print( "Result is False." )
    print( "Finish 1" )
    rospy.sleep(1.0)
    return

def ActionClient2():
    action_client2 = actionlib.SimpleActionClient( "test_action2", TestActionAction )
    print( "action_client2 wait for server." )
    action_client2.wait_for_server()
    goal2 = TestActionGoal()
    goal2.pass_data = "hoge"
    action_client2.send_goal( goal2 )
    print( "action_client2's goal go." )
    print( "action_client2 wait for result." )
    action_client2.wait_for_result()
    result2 = action_client2.get_result()
    print( "action_client2 got result. " )
    if result2:
        print( "Result is True." )
    else:
        print( "Result is False." )
    print( "Finish 2" )
    rospy.sleep(1.0)
    return

if __name__ == '__main__':
    try:
        rospy.init_node( 'action_client' )
        ActionClient()
        ActionClient2()
    except rospy.ROSInterruptException:
        pass