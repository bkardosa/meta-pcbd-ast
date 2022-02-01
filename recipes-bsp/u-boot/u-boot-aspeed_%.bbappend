FILESEXTRAPATHS:prepend := "${THISDIR}/files:"

SRC_URI += "file://0001-env.patch"
SRC_URI += "file://u-boot_env.txt"

do_compile:append() {
    if [ -n "${UBOOT_ENV}" ]
    then
        # Generate redundant environment image
        ${B}/tools/mkenvimage -r -p 0 -s 0x10000 -o ${WORKDIR}/${UBOOT_ENV_BINARY} ${WORKDIR}/u-boot_env.txt
    fi
}

