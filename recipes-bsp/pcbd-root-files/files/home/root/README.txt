Sequence to start up SOL with latest STM32 FW:

# systemctl stop obmc-console@ttyS0
# gpioset 1 0=1 && sleep 3
# udhcpd /etc/udhcpd.conf

Wait for STM32 to get IP address (5-6 secs):
# ping 10.42.10.11

Start obmc-console service:
# systemctl start obmc-console@tty4000

Verify that TCP-UART bridge is running:
# journalctl -u vuart-bridge@tty4000

Boot up AGX Xavier - monitor boot process in SOL console:
# cd pythonTest
# python ./pwr_up.py -ip 10.42.10.11

Shut down AGX Xavier:
# python ./pwr_down.py -ip 10.42.10.11

