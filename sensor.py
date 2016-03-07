
class Sensor(Object):
  # Instantiate using a dict. 
  def __init__(self, config):
    self.tipe = config.tipe
    self.range = config.range
    self.noise = config.noise

  def get_tipe(self):
    return self.tipe

  def get_range(self):
    return self.range

  def set_range(self, new_range):
    self.range = new_range

  def get_noise(self):
    return self.noise

  def set_noise(self, noise):
    self.noise = noise