# Python-TikTok-TTS

This is a small python script can generate the TTS voices from TikTok using [Weilbyte's TikTok API](https://tiktok-tts.weilbyte.dev/).

## How to use

You can either use it as a command-line program, or integrate it as a module in other Python scripts.

### Command line arguments

- `-t / --text` - The text to speak
- `-v / --voice` - The voice code to use, see [Voices](#voices)
- `-o / --output` - If specified, saves the file to the specified path instead of speaking it
- `--volume` - If specified, sets the volume of the TTS (only if not saving to a file)

### Demo script

Saving to a file:
```python
import tiktok_tts

available = tiktok_tts.check_availability()
if not available[0]:
    print(f"Error: Service unavailable! (status: {available[1]}, reason: {available[2]})")

audio = download_audio("How to get free robux for free!", "en_us_001")
if type(audio) != BytesIO:
    # Script already prints error info
    exit(1)

save_audio(audio, "output.mp3")
```

Speaking at half volume:
```python
import tiktok_tts

available = tiktok_tts.check_availability()
if not available[0]:
    print(f"Error: Service unavailable! (status: {available[1]}, reason: {available[2]})")

audio = download_audio("How to get voice chat in Roblox!", "en_us_001")
if type(audio) != BytesIO:
    # Script already prints error info
    exit(1)

play_audio(audio, volume=0.5)
```

## Voices
These are all of the voices currently supported by [Weilbyte's TikTok API](https://tiktok-tts.weilbyte.dev/).
```
---English US---
en_us_001..........................Female
en_us_006..........................Male 1
en_us_007..........................Male 2
en_us_009..........................Male 3
en_us_010..........................Male 4
---English UK---
en_uk_001..........................Male 1
en_uk_003..........................Male 2
---English AU---
en_au_001..........................Female
en_au_002..........................Male
---French---
fr_001.............................Male 1
fr_002.............................Male 2
---German---
de_001.............................Female
de_002.............................Male
---Spanish---
es_002.............................Male
---Spanish MX---
es_mx_002..........................Male 1
es_male_m3.........................Male 2
es_female_f6.......................Female 1
es_female_fp1......................Female 2
es_mx_female_supermom..............Female 3
---Portuguese BR---
br_003.............................Female 2
br_004.............................Female 3
br_005.............................Male
---Indonesian---
id_001.............................Female
---Japanese---
jp_001.............................Female 1
jp_003.............................Female 2
jp_005.............................Female 3
jp_006.............................Male
---Korean---
kr_002.............................Male 1
kr_004.............................Male 2
kr_003.............................Female
---Characters---
en_us_ghostface....................Ghostface (Scream)
en_us_chewbacca....................Chewbacca (Star Wars)
en_us_c3po.........................C3PO (Star Wars)
en_us_stitch.......................Stitch (Lilo & Stitch)
en_us_stormtrooper.................Stormtrooper (Star Wars)
en_us_rocket.......................Rocket (Guardians of the Galaxy)
---Singing---
en_female_f08_salut_damour.........Alto
en_male_m03_lobby..................Tenor
en_male_m03_sunshine_soon..........Sunshine Soon
en_female_f08_warmy_breeze.........Warmy Breeze
en_female_ht_f08_glorious..........Glorious
en_male_sing_funny_it_goes_up......It Goes Up
en_male_m2_xhxs_m03_silly..........Chipmunk
en_female_ht_f08_wonderful_world...Dramatic
```