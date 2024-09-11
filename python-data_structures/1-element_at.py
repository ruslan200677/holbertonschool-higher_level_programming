#!/usr/bin/python3
if __name__ == "__main__":
   my_list = [0, 2, 3]
def element_at(my_list, idx):
  if idx < 0:
    return None
  if idx < 0 or idx >= len(my_list):
    return None
  print("{:d}".format(my_list, idx))