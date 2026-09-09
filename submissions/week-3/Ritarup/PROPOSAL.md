## Topic
Topic 7: Interactive serial prompt

## Problem (in this repo)
Right now, the ESP32-S3 runs the model and streams the generated output text, but the user cannot type their own prompt into the device. The input prompt is fixed at compile time. For example, the TinyStories module uses the prompt **"Once upon a time"** to generate a story. As a result, it generates a similar story every time.
If users could provide a custom prompt, the model could generate different stories based on their input each time. The device currently cannot be used as a real conversational tool because it only runs one preset sequence every time it boots.


## What I would change
I would add a serial input loop on the ESP32-S3. The device would wait on
the USB serial port for the user to type a short prompt (up to 8 tokens,
matching the current seq_len). Once the user presses enter, the device
tokenizes the input, runs the forward pass, and streams the output back over
serial. This is one small change to the firmware, no change to the model
weights or architecture.

## How I would know it worked
I would type 5 different short prompts over serial and check that the device
responds with text each time without crashing or freezing. The metric is
simple: does it respond correctly to all 5 prompts. I would also measure
the time from pressing enter to first output token in milliseconds.

## Memory / size risk
The serial input buffer needs to hold up to 8 token ids — that is 8 integers,
which is under 32 bytes. This fits easily in SRAM. No extra flash is needed
because the model weights do not change. The tokenizer must also run on
device, which needs a small lookup table in flash, but the current vocab is
only 32 tokens so this is tiny. There is no risk to the 559K dense core
budget or the 25M flash table.

## Sources
- RESULTS.md in slvDev/esp32-ai — lists interactive serial prompt under Next
- src/model.py in slvDev/esp32-ai — shows seq_len = 8, confirming input size limit
- Job 1 idx.npy — shape (1, 8) confirms the model takes up to 8 token ids as input