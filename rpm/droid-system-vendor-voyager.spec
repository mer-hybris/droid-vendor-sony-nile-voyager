%define device voyager
%define rpm_device voyager

%define variant -vendor

%define dsd_path ./

Requires(post): coreutils
Requires(post): libcap

%include droid-system-device/droid-system.inc
# rest of this file is autogenerated. do not edit
%post
[ -e /vendor/overlay ] && chown 0:2000 /vendor/overlay
[ -e /vendor/overlay/SysuiDarkTheme ] && chown 0:2000 /vendor/overlay/SysuiDarkTheme
[ -e /vendor/usr ] && chown 0:2000 /vendor/usr
[ -e /vendor/usr/keylayout ] && chown 0:2000 /vendor/usr/keylayout
[ -e /vendor/rfs ] && chown 0:2000 /vendor/rfs
[ -e /vendor/rfs/msm ] && chown 0:2000 /vendor/rfs/msm
[ -e /vendor/rfs/msm/slpi ] && chown 0:2000 /vendor/rfs/msm/slpi
[ -e /vendor/rfs/msm/slpi/readonly ] && chown 0:2000 /vendor/rfs/msm/slpi/readonly
[ -e /vendor/rfs/msm/slpi/readonly/vendor ] && chown 0:2000 /vendor/rfs/msm/slpi/readonly/vendor
[ -e /vendor/rfs/msm/mpss ] && chown 0:2000 /vendor/rfs/msm/mpss
[ -e /vendor/rfs/msm/mpss/readonly ] && chown 0:2000 /vendor/rfs/msm/mpss/readonly
[ -e /vendor/rfs/msm/mpss/readonly/vendor ] && chown 0:2000 /vendor/rfs/msm/mpss/readonly/vendor
[ -e /vendor/rfs/msm/adsp ] && chown 0:2000 /vendor/rfs/msm/adsp
[ -e /vendor/rfs/msm/adsp/readonly ] && chown 0:2000 /vendor/rfs/msm/adsp/readonly
[ -e /vendor/rfs/msm/adsp/readonly/vendor ] && chown 0:2000 /vendor/rfs/msm/adsp/readonly/vendor
[ -e /vendor/lib ] && chown 0:2000 /vendor/lib
[ -e /vendor/lib/soundfx ] && chown 0:2000 /vendor/lib/soundfx
[ -e /vendor/lib/hw ] && chown 0:2000 /vendor/lib/hw
[ -e /vendor/lib/mediadrm ] && chown 0:2000 /vendor/lib/mediadrm
[ -e /vendor/lib/mediacas ] && chown 0:2000 /vendor/lib/mediacas
[ -e /vendor/etc ] && chown 0:2000 /vendor/etc
[ -e /vendor/etc/sensors ] && chown 0:2000 /vendor/etc/sensors
[ -e /vendor/etc/permissions ] && chown 0:2000 /vendor/etc/permissions
[ -e /vendor/etc/wifi ] && chown 0:2000 /vendor/etc/wifi
[ -e /vendor/etc/seccomp_policy ] && chown 0:2000 /vendor/etc/seccomp_policy
[ -e /vendor/etc/data ] && chown 0:2000 /vendor/etc/data
[ -e /vendor/etc/camera ] && chown 0:2000 /vendor/etc/camera
[ -e /vendor/etc/init ] && chown 0:2000 /vendor/etc/init
[ -e /vendor/etc/init/hw ] && chown 0:2000 /vendor/etc/init/hw
[ -e /vendor/etc/acdbdata ] && chown 0:2000 /vendor/etc/acdbdata
[ -e /vendor/etc/selinux ] && chown 0:2000 /vendor/etc/selinux
[ -e /vendor/lib64 ] && chown 0:2000 /vendor/lib64
[ -e /vendor/lib64/soundfx ] && chown 0:2000 /vendor/lib64/soundfx
[ -e /vendor/lib64/hw ] && chown 0:2000 /vendor/lib64/hw
[ -e /vendor/lib64/mediadrm ] && chown 0:2000 /vendor/lib64/mediadrm
[ -e /vendor/lib64/mediacas ] && chown 0:2000 /vendor/lib64/mediacas
[ -e /vendor/firmware ] && chown 0:2000 /vendor/firmware
[ -e /vendor/firmware/wlan ] && chown 0:2000 /vendor/firmware/wlan
[ -e /vendor/firmware/wlan/qca_cld ] && chown 0:2000 /vendor/firmware/wlan/qca_cld
[ -e /vendor/bin ] && chown 0:2000 /vendor/bin
[ -e /vendor/bin/toybox_vendor ] && chown 0:2000 /vendor/bin/toybox_vendor
[ -e /vendor/bin/timekeep ] && chown 0:2000 /vendor/bin/timekeep
[ -e /vendor/bin/init.qcom.ipastart.sh ] && chown 0:2000 /vendor/bin/init.qcom.ipastart.sh
[ -e /vendor/bin/hw ] && chown 0:2000 /vendor/bin/hw
[ -e /vendor/bin/hw/android.hardware.light@2.0-service.sony ] && chown 0:2000 /vendor/bin/hw/android.hardware.light@2.0-service.sony
[ -e /vendor/bin/hw/android.hardware.gnss@1.0-service-qti ] && chown 0:2000 /vendor/bin/hw/android.hardware.gnss@1.0-service-qti
[ -e /vendor/bin/hw/android.hardware.wifi@1.0-service ] && chown 1010:1010 /vendor/bin/hw/android.hardware.wifi@1.0-service
[ -e /vendor/bin/hw/android.hardware.memtrack@1.0-service ] && chown 0:2000 /vendor/bin/hw/android.hardware.memtrack@1.0-service
[ -e /vendor/bin/hw/rild ] && chown 0:2000 /vendor/bin/hw/rild
[ -e /vendor/bin/hw/android.hardware.nfc@1.0-service ] && chown 0:2000 /vendor/bin/hw/android.hardware.nfc@1.0-service
[ -e /vendor/bin/hw/wpa_supplicant ] && chown 0:2000 /vendor/bin/hw/wpa_supplicant
[ -e /vendor/bin/hw/android.hardware.graphics.composer@2.1-service ] && chown 0:2000 /vendor/bin/hw/android.hardware.graphics.composer@2.1-service
[ -e /vendor/bin/hw/android.hardware.sensors@1.0-service ] && chown 0:2000 /vendor/bin/hw/android.hardware.sensors@1.0-service
[ -e /vendor/bin/hw/android.hardware.thermal@1.0-service ] && chown 0:2000 /vendor/bin/hw/android.hardware.thermal@1.0-service
[ -e /vendor/bin/hw/android.hardware.cas@1.0-service ] && chown 0:2000 /vendor/bin/hw/android.hardware.cas@1.0-service
[ -e /vendor/bin/hw/android.hardware.biometrics.fingerprint@2.1-service.sony ] && chown 0:2000 /vendor/bin/hw/android.hardware.biometrics.fingerprint@2.1-service.sony
[ -e /vendor/bin/hw/android.hardware.media.omx@1.0-service ] && chown 0:2000 /vendor/bin/hw/android.hardware.media.omx@1.0-service
[ -e /vendor/bin/hw/android.hardware.vibrator@1.0-service ] && chown 0:2000 /vendor/bin/hw/android.hardware.vibrator@1.0-service
[ -e /vendor/bin/hw/android.hardware.configstore@1.0-service ] && chown 0:2000 /vendor/bin/hw/android.hardware.configstore@1.0-service
[ -e /vendor/bin/hw/android.hardware.camera.provider@2.4-service ] && chown 0:2000 /vendor/bin/hw/android.hardware.camera.provider@2.4-service
[ -e /vendor/bin/hw/android.hardware.power@1.0-service ] && chown 0:2000 /vendor/bin/hw/android.hardware.power@1.0-service
[ -e /vendor/bin/hw/android.hardware.boot@1.0-service ] && chown 0:2000 /vendor/bin/hw/android.hardware.boot@1.0-service
[ -e /vendor/bin/hw/android.hardware.drm@1.0-service ] && chown 0:2000 /vendor/bin/hw/android.hardware.drm@1.0-service
[ -e /vendor/bin/hw/android.hardware.bluetooth@1.0-service ] && chown 1002:1002 /vendor/bin/hw/android.hardware.bluetooth@1.0-service
[ -e /vendor/bin/hw/android.hardware.usb@1.0-service ] && chown 0:2000 /vendor/bin/hw/android.hardware.usb@1.0-service
[ -e /vendor/bin/hw/android.hardware.graphics.allocator@2.0-service ] && chown 0:2000 /vendor/bin/hw/android.hardware.graphics.allocator@2.0-service
[ -e /vendor/bin/hw/android.hardware.audio@2.0-service ] && chown 0:2000 /vendor/bin/hw/android.hardware.audio@2.0-service
[ -e /vendor/bin/vndservicemanager ] && chown 0:2000 /vendor/bin/vndservicemanager
[ -e /vendor/bin/sh ] && chown 0:2000 /vendor/bin/sh
[ -e /vendor/bin/macaddrsetup ] && chown 0:2000 /vendor/bin/macaddrsetup
[ -e /vendor/bin/vndservice ] && chown 0:2000 /vendor/bin/vndservice
[ -e /vendor/bin/thermanager ] && chown 0:2000 /vendor/bin/thermanager
[ -e /vendor/bin/hostapd ] && chown 1010:1010 /vendor/bin/hostapd
[ -e /vendor/bin/grep ] && chown 0:2000 /vendor/bin/grep
[ -e /vendor/bin/init.qcom.devstart.sh ] && chown 0:2000 /vendor/bin/init.qcom.devstart.sh
[ -e /vendor/./bin/hw/android.hardware.wifi@1.0-service ] && setcap cap_net_admin,cap_net_raw+ep /vendor/./bin/hw/android.hardware.wifi@1.0-service
[ -e /vendor/./bin/hw/android.hardware.bluetooth@1.0-service ] && setcap cap_net_admin,cap_sys_nice+ep /vendor/./bin/hw/android.hardware.bluetooth@1.0-service
[ -e /vendor/./bin/hostapd ] && setcap cap_net_admin,cap_net_raw+ep /vendor/./bin/hostapd
