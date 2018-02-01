# Copyright (C) 2016 The CyanogenMod Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

def FullOTA_InstallEnd(info):
  ExtractFirmwares(info)

def ExtractFirmwares(info):
  info.script.Mount("/system")
  info.script.AppendExtra('mount("ext4", "EMMC", "/dev/block/bootdevice/by-name/modem", "/firmware", "");')
  info.script.AppendExtra('ui_print("Extracting modem firmware");')
  info.script.AppendExtra('run_program("/sbin/sh", "/tmp/install/bin/extract_firmware.sh");')
  info.script.AppendExtra('ui_print("Firmware extracted");')
  info.script.AppendExtra('unmount("/firmware");')
  info.script.Unmount("/system")

def magisk(info):
  info.script.Mount("/system")
  info.script.AppendExtra('ui_print("- Flashing Magisk...");')
  info.script.AppendExtra('package_extract_dir("magisk", "/tmp/magisk");')
  info.script.AppendExtra('run_program("/sbin/busybox", "unzip", "/tmp/magisk/magisk.zip", "META-INF/com/google/android/*", "-d", "/tmp/magisk");')
  info.script.AppendExtra('run_program("/sbin/sh", "/tmp/magisk/META-INF/com/google/android/update-binary", "dummy", "1", "/tmp/magisk/magisk.zip");')
  info.script.Unmount("/system")

def dolbyatmos(info):
  info.script.Mount("/system")
  info.script.AppendExtra('ui_print("- Flashing dolbyatmos...");')
  info.script.AppendExtra('package_extract_dir("dolbyatmos", "/tmp/dolbyatmos");')
  info.script.AppendExtra('run_program("/sbin/busybox", "unzip", "/tmp/dolbyatmos/dolbyatmos.zip", "META-INF/com/google/android/*", "-d", "/tmp/dolbyatmos");')
  info.script.AppendExtra('run_program("/sbin/sh", "/tmp/dolbyatmos/META-INF/com/google/android/update-binary", "dummy", "1", "/tmp/dolbyatmos/dolbyatmos.zip");')
  info.script.Unmount("/system")
