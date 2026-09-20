## Topic
7. Interactive serial prompt (listed under Next in RESULTS.md).

## Problem (in this repo)
Right now, the `esp32-ai` project generates text based on a hardcoded prompt or a random seed that is baked into the flash memory. While this proves that the TinyLM model works on the ESP32-S3, it makes playing around with the model really hard. Every time I want to test a new prompt, I have to edit the code and rebuild the firmware. We don't have a simple, interactive way to just type in a prompt and see what the model says.

## What I would change
I propose building a simple, interactive chat prompt using the serial monitor (like a basic read-eval-print loop). After the model is loaded into the PSRAM, the ESP32 would wait for me to type a string and hit Enter on my computer. To make this work, we'd need a tiny piece of code on the device to convert my text into token IDs. The device would then load those tokens and start generating the story. When it finishes, it prints the answer back to the serial monitor and waits for the next prompt.

## How I would know it worked
I would know this worked by simply typing a custom prompt into the Arduino or ESP-IDF serial console and watching the greedy text output. If the model prints back a story that makes sense based on what I typed—without the board crashing—then the experiment is a success. I'd also measure the "time to first token" to see if converting my text into tokens on the device adds too much lag compared to using a hardcoded prompt.

## Memory / size risk
The biggest risk here is running out of SRAM. As the project's `param_budget` explains, things are already really tight: we have a 559K dense core taking up SRAM, while the large 25M table lives in PSRAM/flash. To take my text from the serial monitor, the board needs a temporary string buffer in SRAM. We also have to store the tokenizer vocabulary (a dictionary of words to token IDs) in the flash memory. If the tokenizer code isn't super efficient, it could easily chew up our remaining SRAM and cause the inference engine to crash.

## Sources
- [RESULTS.md](https://github.com/slvDev/esp32-ai/blob/main/RESULTS.md) - This lists the interactive serial prompt as a "Next" step for the project.
- The project README memory tiers - This taught me that SRAM is extremely limited (only for the core) and PSRAM is for the model parameters, which is why I know we have to be careful about where the tokenizer lives.
- [ESP-IDF UART Documentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/uart.html) - This shows how to read text from the serial port without freezing the board.
