
class Damager(Object):

# Instantiate using a config dict
  def __init__(self, config):
    self.tipe = config.tipe
    self.weight = config.weight
    self.damage_value = config.damage_value
    self.ranged = config.ranged

  def is_ranged(self):
    return self.ranged

  def get_weight(self):
    return self.weight

  def set_weight(self, weight):
    self.weight = weight

  def get_damage_value(self):
    return self.damage_value

  def set_damage_value(self, damage):
    self.damage_value = damage