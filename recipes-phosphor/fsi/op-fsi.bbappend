do_configure:append() {
  sed -i 's/ExecStart=/#ExecStart=/g' ../fsi-scan@.service
  sed -i '/^#ExecStart=.*/a ExecStart=/bin/true' ../fsi-scan@.service
}
