do_configure_append() {
  sed -i 's/ExecStart=/#ExecStart=/g' op-cfam-reset.service
  sed -i '/^#ExecStart=.*/a ExecStart=/bin/true' op-cfam-reset.service
}
