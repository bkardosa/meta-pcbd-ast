
do_install:append () {
    sed -i 's/.*deny-interfaces.*/&\ndeny-interfaces=ethslot42/' ${D}${sysconfdir}/avahi/avahi-daemon.conf
}
