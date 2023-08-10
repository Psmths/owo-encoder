# OwO Encoder and Decoder

Very simple encoding scheme that will encode data as a series of OwOs or UwUs. The encoder is a simple state machine. The decoder follows a similar state machine, and will convert OwO encrypted strings to plaintext. 

Example encoding:

```
import owoencode
test_string = "Hello World!"
print(owoencode.encode(test_string))
```

Example of output:

```
OwouwuOWoOwOOWoUwuOWoUwuOWoUWUoWoowoOwOOWOOWoUWUOWOoWoOWoUwuOWoOwooWoowO
```

Example decoding:

```
import owodecode
encoded_string = "OwouwuOWoOwOOWoUwuOWoUwuOWoUWUoWoowoOwOOWOOWoUWUOWOoWoOWoUwuOWoOwooWoowO"
print(owodecode.decode(encoded_string))
```

Example of output:

```
Hello World!
```
