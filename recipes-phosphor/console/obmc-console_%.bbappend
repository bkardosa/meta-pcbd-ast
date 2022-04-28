FILESEXTRAPATHS:prepend:pcb486-ast2500 := "${THISDIR}/${PN}:"

SRC_URI += "file://0001-virtual-uart-devices.patch"
SRC_URI += "file://lib/systemd/system/obmc-console@.service"
SRC_URI += "file://lib/systemd/system/vuart-bridge@.service"

do_install:append:pcb486-ast2500() {
        install -m 0755 -d ${D}${sysconfdir}/${BPN}
        rm -f ${D}${sysconfdir}/${BPN}/server.ttyVUART0.conf
        ln -sr ${D}${sysconfdir}/${BPN}.conf ${D}${sysconfdir}/${BPN}/server.tty4000.conf

        rm -f ${D}${base_libdir}/systemd/system/obmc-console@.service
        install -m 0644 ${WORKDIR}/lib/systemd/system/* ${D}${base_libdir}/systemd/system/
}

FILES:${PN} += "${sysconfdir}"
FILES:${PN} += "${base_libdir}/systemd/system"

