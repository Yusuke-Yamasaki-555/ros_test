#!/usr/bin/env python3

import rospy
import actionlib
from ros_test.msg import TestActionAction, TestActionResult, TestActionFeedback

class ActionServer(object):
    def __init__(self):
        self._action_server = actionlib.SimpleActionServer( 'test_action', TestActionAction, execute_cb = self.execute, auto_start = False )
        self._action_server.start()
        print( "test_action.server start." )

    def execute(self, goal):
        fb = 556
        i = 100
        rs = False
        feedback = TestActionFeedback( fb )
        self._action_server.publish_feedback( feedback )
        print( "Feedback go." )
        if self._action_server.is_preempt_requested():
            self.action_server.set_preempted()
            print( "server break." )
        if goal.pass_data == "hoge":
            rs == True
        result = TestActionResult( rs )
        self._action_server.set_succeeded( rs )
        print( "Result go." )

class ActionServer2(object):
    def __init__(self):
        self._action_server = actionlib.SimpleActionServer( 'test_action2', TestActionAction, execute_cb = self.execute, auto_start = False )
        self._action_server.start()
        print( "test_action2.server start." )

    def execute(self, goal):
        fb = 556
        i = 100
        rs = False
        feedback = TestActionFeedback( fb )
        self._action_server.publish_feedback( feedback )
        print( "2Feedback go." )
        if self._action_server.is_preempt_requested():
            self.action_server.set_preempted()
            print( "2server break." )
        if goal.pass_data == "hoge":
            rs == True
        result = TestActionResult( rs )
        self._action_server.set_succeeded( rs )
        print( "2Result go." )

if __name__ == '__main__':
    rospy.init_node( 'action_server' )
    action_server = ActionServer()
    action_server2 = ActionServer2()
    print( "test_action.server stay for client." )
    rospy.spin()
