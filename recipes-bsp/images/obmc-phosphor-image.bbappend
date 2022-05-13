OBMC_IMAGE_EXTRA_INSTALL:append:pcb486-ast2500 = " \
    bmcweb \
    webui-vue \
    obmc-op-control-power \
    iperf3 \
    ethtool \
    tcpdump \
    python3 \
    python3-pip \
    python3-smbus \
    usbutils \
    mtd-utils \
    sudo \
    socat \
    minicom \
    avahi-daemon \
    avahi-utils \
    pcbd-root-files \
    "

EXTRA_USERS_PARAMS:pn-obmc-phosphor-image = " \
  usermod -p .Oi2v9eH48IwM root; \
  "

python do_insert_uboot_env() {
    import subprocess

    nor_image = os.path.join(d.getVar('IMGDEPLOYDIR', True),
                             '%s.static.mtd' % d.getVar('IMAGE_NAME', True))

    def _append_image(imgpath, start_kb, finish_kb):
        imgsize = os.path.getsize(imgpath)
        maxsize = (finish_kb - start_kb) * 1024
        bb.debug(1, 'Considering file size=' + str(imgsize) + ' name=' + imgpath)
        bb.debug(1, 'Spanning start=' + str(start_kb) + 'K end=' + str(finish_kb) + 'K')
        bb.debug(1, 'Compare needed=' + str(imgsize) + ' available=' + str(maxsize) + ' margin=' + str(maxsize - imgsize))
        if imgsize > maxsize:
            bb.fatal("Image '%s' is too large!" % imgpath)

        subprocess.check_call(['dd', 'bs=1k', 'conv=notrunc',
                               'seek=%d' % start_kb,
                               'if=%s' % imgpath,
                               'of=%s' % nor_image])


    _append_image(os.path.join(d.getVar('DEPLOY_DIR_IMAGE', True),
                               'u-boot_env.%s' % d.getVar('UBOOT_ENV_SUFFIX',True)),
                  384, 448)

}

addtask insert_uboot_env after do_generate_static before do_image_complete

