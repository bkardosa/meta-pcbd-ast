sysroot_stage_all:append() {
        rm -rf ${D}${base_libdir}/systemd/system/obmc-host-startmin@0.target.wants
}

