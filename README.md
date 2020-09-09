# Enigma-Machine

![The Enigma Machine](https://thumbs-prod.si-cdn.com/1R5BVwjtdeEalhj9HBOhH4bDgCo=/800x600/filters:no_upscale()/https://public-media.si-cdn.com/filer/f5/95/f59548db-c8c7-47a0-8404-9e44cd4b8db6/enigma.jpg)

The [Enigma machine](https://en.wikipedia.org/wiki/Enigma_machine) is an encryption device that was invented by a German engineer, Arthur Scherbius, in WWI. Since radio signals are easily intercepted by enemies, the Enigma machine was used extensively by Nazi Germany to send encrypted messages to troops within the German military.


## The Mechanism

The machine has six components:
1. a keyboard
2. a set of lamps for each letter of the alphabet (like a backlit keyboard that you can't press)
3. a set of plugs with both male ends (separate from the machine)
4. a set of plug holes for each letter of the alphabet (called a plugboard)
5. five unique rotors with numbers on the outer ring (separate from the machine)
6. three slots to insert rotors

Using the machine was simple. Suppose that you are a German officer and you want to send the words **"Hey mate send some Sauerbraten"** to your friend in Berlin. Then you would find a piece of paper, called the Wehrmacht key, which has the settings for the enigma machine for each day of the month. Here's what it would look like:

![The Wehrmacht key](http://users.telenet.be/d.rijmenants/pics/hires-wehrmachtkey-stab.jpg)

So if today is the 17th of September, we would find the number 17 in the first column. Then we look across that row and find **IV**, **I**, and **II**. These correspond to three of the five rotors and you would place them into their slots in the machine in that order. Then in the next column, we read 12, 8, and 21. These numbers correspond to the numbers on the rings of the rotors. You will turn the rotors until the numbers on the rings matches the numbers on the paper. Next, we read the next column. The pairs of letters are for the plugs. When we read **ME**, we take a plug and put one end into the **M** slot in the machine and put the other into the **E** slot in the machine. We do that for every pair of letters in the column. Now that we've set up the machine, we can start encrypting our message. To do this, we can simply start typing on the machine. With each letter we type, one of the lamps with a letter will light up and we can write that down. You cannot type a space nor any other non-alphabetic characters on this machine so the message to encrypt would actually be **"HEYMATESENDSOMESAUERBRATEN"**. If the settings were inputted correctly, we should get **"ELMRECOFQWZMCOGXTMFMOBFQBF"**. That will be our encrypted message. You can now send the encrypted message to your friend using radio.

Now suppose that you're the friend in Berlin and you receive the message **"ELMRECOFQWZMCOGXTMFMOBFQBF"** on radio. You will set up the machine in exactly the same way. Then instead of typing the message, you instead just type the encrypted message and read the output on the lamps. You will get **"HEYMATESENDSOMESAUERBRATEN"**.

You might wonder how Germans received the Wehrmacht key in the first place. They simply sent soldiers to deliver them by hand at the start of each month. If the soldier never returned or the receiving end never sent a message, then they can assume that the soldier was intercepted by the enemy and will create a new key and send that instead.

## Using the Program

Using the program is just as simple as using the machine. You will read off of the Wehrmacht key, and type in the settings for the machine when prompted. Then you can simply encrypt or decrypt messages.
