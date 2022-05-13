Sequence to start up SOL with latest STM32 FW:

# systemctl stop obmc-console@ttyS0
# gpioset 1 0=1 && sleep 3
# udhcpd /etc/udhcpd.conf
# systemctl start obmc-console@tty4000

Verify that TCP-UART bridge is running:
# journalctl -u vuart-bridge@tty4000

