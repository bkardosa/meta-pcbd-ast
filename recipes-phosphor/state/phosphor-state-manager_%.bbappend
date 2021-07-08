do_configure_append() {
  sed -i 's/ExecStart=/#ExecStart=/g' service_files/phosphor-reset-host-check@.service
  sed -i '/^#ExecStart=.*/a ExecStart=/bin/true' service_files/phosphor-reset-host-check@.service
}
