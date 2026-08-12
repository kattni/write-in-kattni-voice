Title: Python-Powered eInk Name Badge
Date: 2024-5-15 10:52
Author: Kattni
Tags: Python, Programming, Tutorials, Getting Started
Slug: python-powered-eink-name-badge
Summary: Turn the Pimoroni Badger2040 into a snazzy conference badge
HideTOC: Yes
Status: published

Chances are if you run into me at PyCon US 2024, I'll be wearing a little electronic badge. It shows my name and some contact info, as well as my logo, by default. If you press the proper buttons, however, it launches a game of Tic-Tac-Toe that you can play interactively. It tracks the score for the current set of games, as well as the overall score for all games played during the conference. The version I'm wearing includes some extras that add a layer of difficulty, including soldering. So, I decided to write up this tutorial with a simpler version that you can do without the extra work.

You can make a simple "Hello my name is"-style badge, complete with your name and pronouns, using Python! CircuitPython is a version of Python designed to run on tiny computers called microcontrollers. The Badger2040W is a microcontroller board with an eInk display built into it. Together, they make an excellent, Python-powered conference badge.

This tutorial walks you through the steps needed to prepare your Badger2040, configure the badge to your name and pronouns, and load the code onto the board. When you're done here, you'll have a snazzy badge to show off at your next conference.

## Materials
The project covered in this tutorial does not require a battery pack for the badge, however, there are plenty of other projects where batteries would be needed. If you don't have appropriate battery packs on hand already, I suggest picking up a badge with an accessory kit.

The Badger2040W might be available elsewhere, but I ordered it directly from Pimoroni, so that's where I linked. You can check their reseller list to see if it's available anywhere in the US. I would typically order Pimoroni gear from DigiKey, but the W is not available from them, which is what led me to ordering directly. I link to the basic Badger2040 board as well, which is available from DigiKey. It should work the same for this tutorial.

* [Pimoroni Badger2040W](https://shop.pimoroni.com/products/badger-2040-w?variant=40514062188627) (Available from the UK only) - This is the badge I ordered. If you order this, you will need to ensure you have a data-capable USB Micro cable, and a lanyard.
* [Pimoroni Badger2040W + Accessory Kit](https://shop.pimoroni.com/products/badger-2040-w?variant=40514062221395) (Available from the UK only) - This is the same badge as I ordered, but with a kit. The kit comes with a battery pack, velcro for attaching it, lanyard, and USB cable.
* [Pimoroni Badger2040 + Accessory Kit](https://www.digikey.com/en/products/detail/pimoroni-ltd/PIM610/16716825) (Available in the US) - This is not the same badge as I ordered. This code _should_ run the same on this version of it, however, the hardware is a bit different; it has no Wifi, and the microcontroller is built into the board, versus having a separate board attached to the back. This kit comes with a battery pack, velcro for attaching it, lanyard, and USB cable.

## Simple Name Badge
Once you have your Badger2040 in-hand, you're ready to get going with your name badge.

_Note: As they are essentially interchangeable for the main part of this tutorial, I'll refer to the board as the "Badger2040" throughout, except where I am referring specifically to the Badger2040W version._

### Prerequisites and Assumptions
There major prerequisite is needing the hardware listed above.

If you're running MacOS Sonoma below 14.4, there are some major issues with CircuitPython that can cause file corruption. **It is _highly_ recommended that you upgrade to 14.4+ before continuing.** Note that writing files to CircuitPython in Sonoma is slower than previous versions of MacOS. Be sure to let it finish before continuing on to next steps.

There are a few basic programming terms used in this tutorial. The way the steps are presented should allow you to work through this tutorial without any programming knowledge. 

### kBits
I usually intend the kBits to include everything necessary to complete the tutorial, however, this tutorial is very step-based, and the detailed steps below are pretty straightforward. So, I'll be listing the basics here, but you'll need to read on to complete this one.

* Load CircuitPython onto your Badger2040.
* Download the code and library.
* Configure your name and pronouns as you want them displayed on the badge.
* Load the code and library onto the Badger2040.
* Attach a lanyard, and badge it up!

### Prepare Your Badge
The Badger2040 ships with a nifty set of applications on it. When you plug it in, you'll see an app-switcher, which you can use the buttons to navigate. I'd suggest checking it out, if you're interested. **What you're about to do will delete that code.** (It's available through Pimoroni's website! It's not lost forever. However, I won't be covering how to restore it.)

The first thing you need to do is to install CircuitPython. There's a Follow these steps.

* Head over to the download page for [CircuitPython for the Badger2020W](https://circuitpython.org/board/pimoroni_badger2040w/) (or the [Badger2040](https://circuitpython.org/board/pimoroni_badger2040/) if that's what you picked up).
* You'll want the "latest stable release". **Click the purple "DOWNLOAD ..UF2 NOW" button.**
* **Plug your board into your computer using a USB Micro to USB A cable that has data functionality.** Charge-only cables will not work!
* There are two buttons on the back of the board: RESET and BOOTSEL. On the Badger2040W, RESET is on the top-right, and BOOTSEL is on the smaller green board attached to the back.
* **Press and _hold_ BOOTSEL.** Do not release it.
* **Press and _release_ RESET.**
* You should see a new drive mount and appear in your file explorer called _RPI-RP2_.
* **Once the _RPI-RP2_ drive appears, _release_ BOOTSEL.**
* **Navigate to wherever you downloaded the UF2 file.**
* **Drag the UF2 file to the _RPI-RP2_ drive.**
* Wait while it copies over. The RPI-RP2 drive will unmount and disappear.
* You should see a new drive mount and appear called _CIRCUITPY_. You've successfully installed CircuitPython on your Badger2040!

### Download the Code and Library
You need to load the code and required library onto your Badge2040W. So the next step is to download them. 

Click [here](https://github.com/kattni/badger2040W-simple-badge/archive/refs/heads/main.zip) to download the code and libraries as a zip file from GitHub.

Once downloaded, extract the contents to wherever is convenient for you. The zip should include the following file and directories:

* code.py
* lib/
    * adafruit_display_text/

Once verified, you're ready to configure the code.

### Configure Your Name and Pronouns
The main thing to configure in the code is the text on the badge, particularly, your name and pronouns. 

To edit the code, open the _code.py_ file that you extracted from the zip in the previous step. You can open it in your favorite Python editor. If you're new to programming, you can open it in a basic text editor.

At the top of the file, after the import list, there are two variables: `NAME_STRING` and `PRONOUN_STRING`. To configure the text on the badge, you'll change the text in quotes (`"`).

For example, to update the badge for me, I would change the `NAME_STRING` line to the following:

```python
NAME_STRING = "Kattni"
```

To update the pronouns to they/them, you would change the `PRONOUN_STRING` line to the following:

```python
PRONOUN_STRING = "THEY/THEM"
```

The rest of the configuration is optional. It'll be explained later in the tutorial, as you are unlikely to need it until after you've loaded the code onto the badge.

Now that you've configured your name and pronouns, it's time to load the code onto the badge.

### Load the Code and Library onto The Badge
Remember the _CIRCUITPY_ drive that appeared after loading CircuitPython onto your Badger2040? It's time to use it. 

You should already have the contents of the zip you downloaded pulled up in your file explorer, and you should have configured the code in the _code.py_ file. 

To load the code and library onto the badge, drag the _code.py_ file and the _lib/_ directory (including the subdirectory it contains) onto the _CIRCUITPY_ drive. Replace the existing _code.py_ file and _lib/_ directory when prompted.

The display should refresh (reload), and your badge will be displayed.

Eject the _CIRCUITPY_ drive from your file explorer, and unplug the Badger2040.

### Wearing Your Badge
Attach a lanyard and wear your badge in style!

eInk displays are designed to maintain whatever is on the display even when they are powered off. Therefore, as long as you let the badge code fully load before unplugging the Badger2040 from your computer, the badge will remain on the display once it is unplugged, without the need for a battery. 

You're all set to go!

### Optional Configuration
The other two configuration sections available in the code are only necessary if you need to change the font size of your name to enable it to fit, or if you want to update the text along the top of the badge. 

#### Configure Name Font Size, If Your Name Doesn't Fit
In the event that you have a longer name, you may find that it doesn't fit on the badge. If this happens, you can decrease the name font size. 

To decrease the name font size, update the `NAME_SCALE` line to the following:
```python
NAME_SCALE = 2
```

#### Configure the "Hello" Text
If you'd rather the "HELLO MY NAME IS" said something different, you can configure that as well. To update the "HELLO" text on the badge, update the `HELLO_STRING` line to your desired text. 

For example, to update it to read "HELLO I'M", you would update the `HELLO_STRING` line to the following:

```python
HELLO_STRING = "HELLO I'M"
```

### Troubleshooting Along The Way
If you run into issues not covered in this tutorial, there's a [guide](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython) available for CircuitPython with numerous troubleshooting steps. Please refer to the guide for a resolution, and then return to this tutorial to continue.

## Kattni's PyCon US 2024 Badge
Thanks to [Tim C](https://github.com/FoamyGuy/CircuitPython_Badger2040W_TicTacToe/tree/main) for designing my badge code this year!

This code requires the Badger2040W (the WiFi version), and includes an 8-pixel NeoPixel LED stick attached to the Qwiic/STEMMA QT connector on the back using the SDA pin (blue wire on a standard STEMMA QT cable). Attaching the LED stick requires soldering. I will not be covering how to do this in this tutorial, I am simply providing the code as-is. It will run fine without the LEDs connected; they are not necessary for the code to run, it simply won't have the LED animations visible.

Note that to run this detached from your computer, you must attach a battery pack to the back of the Badger2040W.

You can download the zip [here](https://github.com/kattni/pycon-us-2024-badge/archive/refs/heads/main.zip). Extract the content from the zip. Follow the steps [here](#Load-the-Code-and-Library-onto-The-Badge) to copy the content to the Badger2040W.

You'll see the initial badge on the display. To play Tic-Tac-Toe, press and hold the A button, then press the C button, and release both. The game should start. Use the same button sequence to return to the badge. 

Within the game, use the up, down, A, and C buttons to move around the board. Pressing B will place your marker on the board. When a game is complete, press

The badge is a bitmap file called _badge.bmp_. You can create a black and white bitmap file with the same dimensions, and replace the existing file on the _CIRCUITPY_ drive to show your own badge.
