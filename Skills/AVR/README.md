# Harness the full potential of the AVR

- When using the Atmel Studio to build our project. We have no control over the memory allocation of the flash memory of the AVR device. In the `project solution folder -> Debug folder -> .map` file includes the memory allocation details of the AVR device.

- However we can do that memory allocation manually using the methods described in the `avr-libc` documentation.

```
Memory Configuration

Name             Origin             Length             Attributes
text             0x00000000         0x00008000         xr
data             0x00800060         0x00000800         rw !x
eeprom           0x00810000         0x00000400         rw !x
fuse             0x00820000         0x00000002         rw !x
lock             0x00830000         0x00000400         rw !x
signature        0x00840000         0x00000400         rw !x
user_signatures  0x00850000         0x00000400         rw !x
*default*        0x00000000         0xffffffff
```

```
END GROUP
                [0x00000000]                __TEXT_REGION_ORIGIN__ = DEFINED (__TEXT_REGION_ORIGIN__)?__TEXT_REGION_ORIGIN__:0x0
                [0x00800060]                __DATA_REGION_ORIGIN__ = DEFINED (__DATA_REGION_ORIGIN__)?__DATA_REGION_ORIGIN__:0x800060
                [0x00008000]                __TEXT_REGION_LENGTH__ = DEFINED (__TEXT_REGION_LENGTH__)?__TEXT_REGION_LENGTH__:0x20000
                [0x00000800]                __DATA_REGION_LENGTH__ = DEFINED (__DATA_REGION_LENGTH__)?__DATA_REGION_LENGTH__:0xffa0
                [0x00000400]                __EEPROM_REGION_LENGTH__ = DEFINED (__EEPROM_REGION_LENGTH__)?__EEPROM_REGION_LENGTH__:0x10000
                [0x00000002]                __FUSE_REGION_LENGTH__ = DEFINED (__FUSE_REGION_LENGTH__)?__FUSE_REGION_LENGTH__:0x400
                0x00000400                __LOCK_REGION_LENGTH__ = DEFINED (__LOCK_REGION_LENGTH__)?__LOCK_REGION_LENGTH__:0x400
                0x00000400                __SIGNATURE_REGION_LENGTH__ = DEFINED (__SIGNATURE_REGION_LENGTH__)?__SIGNATURE_REGION_LENGTH__:0x400
                0x00000400                __USER_SIGNATURE_REGION_LENGTH__ = DEFINED (__USER_SIGNATURE_REGION_LENGTH__)?__USER_SIGNATURE_REGION_LENGTH__:0x400

```
- Atmel Studio should have a way to access and modify those attributes. check the documentation for more information. In atmel Studio `Project -> Properties -> toolchain`
