from _vpc import vpc

class Subnet(_vpc):
  def __init__(self, region_name, subnet_id:str=None):
