DESCRIPTION = "Root filesystem customization"

LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COREBASE}/meta/files/common-licenses/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = "file://etc/udhcpd.conf"
SRC_URI += "file://etc/udev/rules.d/42-cdc-ether.rules"
SRC_URI += "file://etc/systemd/network/00-bmc-ethslot42.network"
SRC_URI += "file://home/root/README.txt"


do_install() {
    install -d ${D}${sysconfdir}/udev/rules.d
    install -d ${D}${sysconfdir}/systemd/network
    install -d ${D}/home/root

    install -m 644 ${WORKDIR}/etc/udhcpd.conf ${D}${sysconfdir}
    install -m 644 ${WORKDIR}/etc/udev/rules.d/42-cdc-ether.rules ${D}${sysconfdir}/udev/rules.d/
    install -m 644 ${WORKDIR}/etc/systemd/network/00-bmc-ethslot42.network ${D}${sysconfdir}/systemd/network/
    install -m 644 ${WORKDIR}/home/root/* ${D}/home/root/
}

FILES:${PN} += "${sysconfdir}"
FILES:${PN} += "/home/root/README.txt"

RDEPENDS:${PN} += "udev systemd"
