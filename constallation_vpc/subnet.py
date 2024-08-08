from _ec2 import ec2

class Subnet(_ec2):
  def __init__(self, region_name, subnet_id:str=None):
