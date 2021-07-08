do_configure_append() {
  sed -i 's/ExecStart=/#ExecStart=/g' start_host@.service
  sed -i '/^#ExecStart=.*/a ExecStart=/bin/true' start_host@.service
}
