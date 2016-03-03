
class Server():
	def __init__(self):
		pass

	def register_robot(self, robot_description):
		# Instantiate and return robot object as per description
		pass

	def get_position(self, robot):
		# Return robot position
		pass

	def request_move(self, magnitude, direction):
		# Check if requested move is legal and return updated position
		pass

	def attack(self, robot):
		# Perform attack move for robot and return results
		pass

	def observe(self, robot):
		# Return observations for robot based on sensor capabilities
		pass