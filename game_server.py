#!/usr/bin/env python3

import recurse_robot_broker as broker
import recurse_robot_client as RRC

class Server(Object):
  def __init__(self, config):
    self.config = config # config is some object?
    self.robots = {}
    self.broker = broker.Broker(self)

  # These methods are remote-facing
  def register_robot(self, robot_description, conn):
    # Instantiate and return robot object as per description
    r = RRC.Robot(robot_description)
    robot_id = RRC.make_id(r)
    self.robots[robot_id] = r
    msg = make_message(query=register, tipe=reply, body=robot_id)
    self.broker.send_message(r, msg)

  def get_position(self, robot_id):
    # Return robot position
    r = self.robots[robot_id]
    msg = make_message(query=position, tipe=reply, body=r.position)
    self.broker.send_message(r, msg)

  def request_move(self, robot_id, magnitude, direction):
    # Check if requested move is legal and return updated position
    pass

  def attack(self, robot_id):
    # Perform attack move for robot and return results
    pass

  def observe(self, robot_id):
    # Return observations for robot based on sensor capabilities
    pass


# non-class functions
def make_message(query, tipe, body):
  pass

def send_message(robot, msg):
  pass
