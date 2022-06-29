from BraineCommTest import BraineCommTest
import time
import braine_comm_pb2

# Reading device IP address and port
ip_address = input("Device IP: ")
#port = int(input("Device port: "))
port = 6000

print(ip_address)
print(port)

test = BraineCommTest(ip_address, port, "DEBUG")
test.getStmIdFunc()
test.getSwVersionFunc()
test.setControlStateFunc(braine_comm_pb2.START)
test.getControlStateFunc()
#test.setControlStateFunc(braine_comm_pb2.STOP)
#test.getControlStateFunc()
#test.setControlStateFunc(braine_comm_pb2.SLEEP)
#test.getControlStateFunc()

test.setDebugCmdFunc(braine_comm_pb2.POWER_UP)
test.getTempFunc(0)
test.getTempFunc(1)
# test.setDebugCmdFunc(braine_comm_pb2.POWER_BUTTON)
time.sleep(3)
test.setDebugCmdFunc(braine_comm_pb2.POWER_DOWN)
test.getPowerFunc(0)
test.getPowerFunc(1)
test.getControlStateFunc()

