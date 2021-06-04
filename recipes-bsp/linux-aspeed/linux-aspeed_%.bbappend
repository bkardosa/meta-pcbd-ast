FILESEXTRAPATHS_prepend := "${THISDIR}/files:"

SRC_URI += "file://fragment-01-debug.cfg"
SRC_URI += "file://fragment-02-usb.cfg"
SRC_URI += "file://fragment-03-video-buf.cfg"

SRC_URI += "file://0001-ehci-debug.patch"
SRC_URI += "file://0002-dts-kvm-sol.patch"

