# Installing AVRDUDE for Atmel Studio(latest version known as Microchip Studio) 🐞

## 1. *Install drivers for USBasp cable*

1. Go to https://zadig.akeo.ie/ and download Zadig

<p align="center">
<img src="Figures/zadig.jpeg"  align="center" height=800>
</p>

3. Plug the USBasp cable into one of the USB ports.
4. Open zadig executable file.
5. Click Options -> List All Devices -> Select USBasp from the Drop down menu.
6. Select `libusb-win32 (v1.2.6.0)` and click install driver.

## 2. *Install WinAVR using the link* https://sourceforge.net/projects/winavr/

WinAVR (tm) is a suite of executable, open source software development tools for the Atmel AVR series of RISC microprocessors hosted on the Windows platform. Includes the GNU GCC compiler for C and C++.

## 3. *Go to `External Tools` of the `Tools` in the menu bar of the Atmel studio*

```
Title: USBasp // give a suitable name
Command: D:\WinAVR-20100110\bin\avrdude.exe // directory where WinAVR is installed.
Arguments: -p m32 -c usbasp -P usb -U flash:w:"$(ProjectDir)Debug\$(TargetName).hex":i // arguments are for ATMEGA32
Initial Directory: $(ProjectDir)
```
***Dont forget to check Use output window and Prompt for arguments (optional). After adding these entries your external tools window will look like this. Then press Apply and OK.***

<p align="center">
<img src="Figures/ext_tools.PNG"  align="center" height=400>
</p>

## 4. *Before using avrdude, Solution must be built. Then it can be uploaded to the MCU (Microcontroller Unit)*
1. Menu bar -> Build -> Build Solution
2. Tools -> USBasp

---

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
