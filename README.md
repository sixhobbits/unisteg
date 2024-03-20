<p align="center">
  <a href="https://github.com/sixhobbits/unisteg">
    <img alt="Unisteg" title="Unisteg" src="./unisteg.png" width="100" style="color: black">
  </a>
</p>


<p align="center">
  <i>Hide text in text with invisible unicode characters</i><br/> 
</p>

<h1 align="center">
 Unisteg
</h1>

<br/>

Unisteg (from unicode steganography) lets you hide one string in another string by using [invisible unicode characters](https://invisible-characters.com/), specifically it uses `U+E0100 VARIATION SELECTOR-17` thru `U+E0180 VARIATION SELECTOR-145`, which gives 128 characters. That means it can encode any ASCII string, and therefore any base64 string.

There are [16 unicode selectors](https://en.wikipedia.org/wiki/Variation_Selectors_(Unicode_block)) used to modify the preceding character, most famously to give you emojis of different skin colours ✊🏾 ✊🏼 ✊. Then there is a big block of [supplemental variation selectors](https://en.wikipedia.org/wiki/Variation_Selectors_Supplement). I have no idea what they are used for. It's possible that you might see unexpected behaviour from this library if you use it to encode hidden messages into a string that is already using characters from that block as they are intended to be used, but I think it is probably unlikely.

## Installation

Probably just copy the 30 lines of Python code from the unisteg.py file to your own project to be honest. Not everything needs to be a library. If you want, you can install it from this repo using pip. It's not on pypi.

Here's the full source code for easy reference or copy-pasta.

```python
import base64

FIRST_INVISIBLE_CHAR = 917760

def encode(s):
    """Encodes an input string to a hidden one"""
    encoded = []
    for char in s:
        if ord(char) > 127:
            raise Exception(f"Non ascii character {char}. Maybe base64 encode your string first")
        encoded.append(chr(ord(char) + FIRST_INVISIBLE_CHAR))
    return ''.join(encoded)

def decode(s):
    """Decodes any of our 'special' characters to ascii"""
    plain = []
    for char in s:
        try:
            plain.append(chr(ord(char) - FIRST_INVISIBLE_CHAR))
        except:
            pass
    return ''.join(plain)

def add(m, s=""):
    """Adds a message to a string"""
    b64 = base64.b64encode(m.encode("utf8")).decode("utf8")
    hidden = encode(b64)
    return s + hidden

def get(s):
    """Gets a message from a string"""
    hidden = decode(s)
    decoded = base64.b64decode(hidden).decode("utf8")
    return decoded
```

## Usage

The library has two levels of functions - a lower-level `encode` and `decode` pair that will take a plaintext string and translate it to invisible characters. These require that your input string only uses the ASCII character set from `ord(0)` to `ord(127)`.

For most use, you should use `add` and `get` rather. This will take an input secret, encode it as base64, then encode _that_ to the invisible character set. It will combine the resulting string with your clear text string and give you something that to the naked eye looks just like your clear text string, but which also contains the invisible secret.

Example:

```python
import unisteg

secret = "this is a s3cret message. ssh"
plaintext = "Hey you, nothing to see here."
to_share = unisteg.add(secret, plaintext)

print(plaintext)
print(to_share)
print("length of plaintext", len(plaintext))
print("length of to_share", len(to_share))
```

This will output

```
Hey you, nothing to see here.
Hey you, nothing to see here.󠅤󠅇󠅨󠅰󠅣󠅹󠅂󠅰󠅣
length of plaintext 29
length of to_share 69
```

So the 'secret' message is included in the `to_share` string, but it still looks exactly like the `plaintext` one (unless you start printing out the length of the string, or the `ord` codes of each character in it. Then the game is up.)

To get your message back again, just add

```python
retrieved = unisteg.get(to_share)
print(retrieved)
```

which will print

```
this is a s3cret message. ssh
```

Magic.

## Why? 

I loved the idea of steganography 10 years ago when [I was first introduced to it](https://dwyer.co.za/static/steganography.pdf). This is a fun way to send hidden messages. 

Why I actually created this now is because I was building a Python Telegram bot with a custom keyboard. In Telegram, you can make keyboards with [arbitrary keys](https://core.telegram.org/bots/api#keyboardbutton) that have arbitrary text. I wanted some basic CRUD functionality where I show the user items from their shopping list like "milk", "eggs", etc, and when the user presses on that item it marks it as done. Unfortuantely, there's no way to include any other data in the custom keyboard, like the database ID of that item, so I needed a way to include extra information in the user interface without cluttering up each key. 

This was not a pretty way to do it, but it works.

