Hello, I made this cool string encoder in Python, which is like a translator to an unknown language. 
let's just say I want to keep my passwords in a note. but as you know, whoever that uses your computer can easily read your notes. I mean you can just hide it somewhere and keep it hidden, but that's too lame. which is why I made this Custom string encoder.
now, the reason it has "Custom" in it's name is because you can actually change the encoder settings.

CONFIGURATION:

Basically, lets just say you want to encode the character 'a' then this code will turn it into whatever the settings tells it to. for example, 'Hi' will be turned turn into 'Ab'.
now, before using, you probably want to configure the encoder to make it more secure. if so, you must prepare an IDE for easier usage since it'll tell you if an error occured. (if not, you can skip to the usage part)
or, you can go to the non-IDE route by renaming the Python file to Custom string Encoder.txt then open it.

![top of the code](https://github.com/armygogames/Custom-string-Encoder.py/assets/141536305/26398455-dd00-474d-b1c7-7cb736818fa5)

now, you can insert anything in format of "a":"b" you can change those character to anything you'd like maybe symbols or anything I haven't added. (or delete everything and configure it yourself)

SUPER IMPORTANT! you must add , in the end of "a":"b" ("a":"b","c":"d","e":"f",on and on)

THIS IS ALSO SUPER IMPORTANT! you CAN'T add the symbol "!" to the encoder since it's used in the code to add salts. if added, will break the code.

now, rename the file back to Custom string Encoder.py then open it if you aren't using an IDE

USAGE:

after you open the code, you will be greeted by an input to put between yes or no, if you want the code to generate a random salt for you, you can type Y. if not, type N

![Input Salting Mode](https://github.com/armygogames/Custom-string-Encoder.py/assets/141536305/c3aba9d3-3abd-455c-b0d0-300d7bfb5921)

In this case, I'll type N for no, and manually add amount of salts myself.
after that, type Encode (or E to shorten the process) if you want to Encode or type Decode (or D to shorten the process too) if you want to Decode followed by a space and type in any word you want to Encode or Decode.
in this case, I want to Encode 'Hello World' so, i'll type Encode Hello World
after that, you need to input the amount of salt, in the string. (it'll instantly show the decoded version with a random salt of your input if you are not in random salt mode)

![result](https://github.com/armygogames/Custom-string-Encoder.py/assets/141536305/387f07dc-aac9-4d16-a657-906fbd885906)

So, I added 2 salt in my string. so Originally, the string 'Hello World' only has 11 character but, we're adding salt in it, we need somthing to remind our encoder that our string has 2 salts whioch is by having !(amount of salt)! in our string.
now we have (original character amount) + 3 (reminder) + 2 since I added 2 salts, it will have 16 (11+3+2) character, which made it look like an even longer string. even though it's not. and the best part of adding salt is, you can add as much salt in you string as you want.
if you typed Y to random salt mode, it'll add random salt amount ranging from 1 to 25 characters. so, your string may look even longer than you originally input.
And the best part is, if you decode that string, the salt will instantly be gone and you'll recieve your original string you've encoded.

![Final Result](https://github.com/armygogames/Custom-string-Encoder.py/assets/141536305/e2bd1e7f-af00-4386-8456-ce949f639338)

as you can see we got the same input as we typed in which is Hello World.

That's it for the code, Have fun using it

Thanks.
