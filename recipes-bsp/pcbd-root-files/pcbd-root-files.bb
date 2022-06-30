DESCRIPTION = "Root filesystem customization"

LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COREBASE}/meta/files/common-licenses/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = "file://etc/udhcpd.conf"
SRC_URI += "file://etc/udev/rules.d/42-cdc-ether.rules"
SRC_URI += "file://etc/systemd/network/00-bmc-ethslot42.network"
SRC_URI += "file://home/root/README.txt"
SRC_URI += "file://home/root/pythonTest/braine_comm_pb2.py"
SRC_URI += "file://home/root/pythonTest/BraineCommTest.py"
SRC_URI += "file://home/root/pythonTest/pwr_down.py"
SRC_URI += "file://home/root/pythonTest/pwr_up.py"
SRC_URI += "file://home/root/pythonTest/SerialLink.py"
SRC_URI += "file://home/root/pythonTest/test.py"


do_install() {
    install -d ${D}${sysconfdir}/udev/rules.d
    install -d ${D}${sysconfdir}/systemd/network
    install -d ${D}/home/root/pythonTest

    install -m 644 ${WORKDIR}/etc/udhcpd.conf ${D}${sysconfdir}
    install -m 644 ${WORKDIR}/etc/udev/rules.d/42-cdc-ether.rules ${D}${sysconfdir}/udev/rules.d/
    install -m 644 ${WORKDIR}/etc/systemd/network/00-bmc-ethslot42.network ${D}${sysconfdir}/systemd/network/
    install -m 644 ${WORKDIR}/home/root/README.txt ${D}/home/root/
    install -m 644 ${WORKDIR}/home/root/pythonTest/* ${D}/home/root/pythonTest/
}

FILES:${PN} += "${sysconfdir}"
FILES:${PN} += "/home/root"

RDEPENDS:${PN} += "udev systemd"
