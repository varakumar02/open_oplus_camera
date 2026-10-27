# Patched odm camera configs for the OnePlus 9 (lemonade).
# The files are in open_oplus_camera_blobs/devices/lemonade, made from the stock ones by
# tools/odm_patch.py with patches-odm/lemonade. The stock copies stay in vendor/oneplus/lemonade.
# Inherit this before vendor/oneplus/lemonade/lemonade-vendor.mk: for one destination the
# first PRODUCT_COPY_FILES entry wins and the later one is ignored.

CAMERA_ODM_PATCHED := vendor/oplus/camera-blobs/devices/lemonade/odm

PRODUCT_COPY_FILES += \
    $(CAMERA_ODM_PATCHED)/etc/camera/CameraHWConfiguration.config:$(TARGET_COPY_OUT_ODM)/etc/camera/CameraHWConfiguration.config \
    $(CAMERA_ODM_PATCHED)/etc/camera/config/camera_unit_config:$(TARGET_COPY_OUT_ODM)/etc/camera/config/camera_unit_config \
    $(CAMERA_ODM_PATCHED)/etc/camera/config/camera_unit_feature_config.protobuf:$(TARGET_COPY_OUT_ODM)/etc/camera/config/camera_unit_feature_config.protobuf \
    $(CAMERA_ODM_PATCHED)/etc/camera/config/oplus_camera_algo_switch_config:$(TARGET_COPY_OUT_ODM)/etc/camera/config/oplus_camera_algo_switch_config \
    $(CAMERA_ODM_PATCHED)/etc/camera/config/oplus_camera_config:$(TARGET_COPY_OUT_ODM)/etc/camera/config/oplus_camera_config \
    $(CAMERA_ODM_PATCHED)/lib64/camera/com.qti.tuned.semco_imx689.bin:$(TARGET_COPY_OUT_ODM)/lib64/camera/com.qti.tuned.semco_imx689.bin
