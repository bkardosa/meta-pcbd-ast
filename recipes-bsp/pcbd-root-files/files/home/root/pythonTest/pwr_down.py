from BraineCommTest import BraineCommTest
import time
import braine_comm_pb2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-ip", help="IP address")
args = parser.parse_args()
if args.ip:
  ip_address = args.ip
# Reading device IP address and port
else:
  ip_address = input("Device IP: ")
port = 6000

print(f'target: {ip_address}:{port}')

test = BraineCommTest(ip_address, port, "DEBUG")
test.getStmIdFunc()
test.getSwVersionFunc()
test.setDebugCmdFunc(braine_comm_pb2.POWER_DOWN)
test.getPowerFunc(0)
test.getPowerFunc(1)
test.getControlStateFunc()

