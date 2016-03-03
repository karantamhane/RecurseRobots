#!/usr/bin/env python3

import RecurseRobotClient as RRC

class Server(Object):
  def __init__(self, config):
    self.config = config # config is some object?
    self.robots = {}

  def register_robot(self, robot_description):
    # Instantiate and return robot object as per description
    r = RRC.Robot(robot_description)
    robot_id = RRC.make_id(r)
    self.robots[robot_id] = r

  def get_position(self, robot_id):
    # Return robot position
    pass

  def request_move(self, robot_id, magnitude, direction):
    # Check if requested move is legal and return updated position
    pass

  def attack(self, robot_id):
    # Perform attack move for robot and return results
    pass

  def observe(self, robot_id):
    # Return observations for robot based on sensor capabilities
    pass
