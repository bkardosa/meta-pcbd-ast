FILESEXTRAPATHS_prepend_congax7-ast2500 := "${THISDIR}/${PN}:"

do_install_append_congax7-ast2500() {
        install -m 0755 -d ${D}${sysconfdir}/${BPN}
        rm -f ${D}${sysconfdir}/${BPN}/server.ttyVUART0.conf
        ln -sr ${D}${sysconfdir}/${BPN}.conf ${D}${sysconfdir}/${BPN}/server.ttyS0.conf
}

