<p align="center">
  <a href="https://github.com/sixhobbits/unisteg">
    <img alt="Unisteg" title="Unisteg" src="./unisteg.png" width="100" style="color: black">
  </a>
</p>


<p align="center">
  <i>Hide text in text with invisible unicode characters</i><br/> 
  <a href="https://github.com/sixhobbits/unisteg">unisteg</a>
</p>

<h1 align="center">
Unisteg
</h1>

<br/>

Unisteg (from unicode steganography) lets you hide one string in another string by using [invisible unicode characters](https://invisible-characters.com/), specifically it uses `U+E0100 VARIATION SELECTOR-17` thru `U+E0180 VARIATION SELECTOR-145`, which gives 128 characters. That means it can encode any ASCII string, and therefore any base64 string.

There are [16 unicode selectors](https://en.wikipedia.org/wiki/Variation_Selectors_(Unicode_block)) used to modify the preceding character, most famously to give you emojis of different skin colours ✊🏾 ✊🏼 ✊.




