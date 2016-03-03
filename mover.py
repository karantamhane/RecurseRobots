
class Mover(Object):
# Instantiate using a config dict
  def __init__(self, config):
    self.tipe = config.tipe
    self.weight = config.weight
    self.speed = config.speed
    self.energy_cost = config.energy_cost
    self.inertia = config.inertia

  def get_tipe(self):
    return self.tipe

  def set_tipe(self, tipe):
    self.tipe = tipe

  def get_weight(self):
    return self.weight

  def set_weight(self, weight):
    self.weight = weight

  def get_speed(self):
    return self.speed

  def set_speed(self, speed):
    self.speed = speed

  def get_energy_cost(self):
    return self.energy_cost

  def set_energy_cost(self, energy_cost):
    self.energy_cost = energy_cost

  def get_inertia(self):
    return self.inertia

  def set_inertia(self, inertia):
    self.inertia = inertia
