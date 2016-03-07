
class Armor(Object):
  def __init__(self, config):
    self.tipe = config.tipe
    self.damage_resistance = config.damage_resistance
    # Whether defenses are active or passive
    self.active = config.active
    # Range of enemy detection for active defenses
    self.range = config.defense_range

  def get_tipe(self):
    return self.tipe

  def get_damage_resistance(self):
    return self.damage_resistance

  def set_damage_resistance(self, resistance):
    self.damage_resistance = resistance

  def is_active(self):
    return self.active

  def get_defense_range(self):
    if self.active:
      return self.defense_range

  def set_range(self, defense_range):
    if self.active:
      self.range = defense_range
