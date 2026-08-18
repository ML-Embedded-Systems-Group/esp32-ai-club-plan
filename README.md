# ESP32 AI Club Plan

This repository contains the Week 1 tasks for the ESP32 AI Club.

The club project studies machine learning on the ESP32-S3. Members read a trusted resource, solve a small problem, reproduce the result in code, and write a short report.

## Week 1 Goals

By the end of Week 1, each member must:

1. Explain the assigned idea in their own words.
2. Show the assigned maths step by step.
3. Write and run the assigned reproduction script.
4. Record the script output in a Markdown report.
5. Ask their pair to review the report.

Do not copy text or code from an AI tool. Use the resources as study material.

## Task Files

| File | Track | Topic | Main result |
|---|---|---|---|
| 01_R1.md | ML research | Probability | `P(B1) = 0.6`, `P(A1 given B1) = 0.333` |
| 02_R2.md | ML research | Gradient descent | Recover `y = 3x + 5` |
| 03_R3.md | ML research | Logistic regression | Classify all 6 points |
| 04_R4.md | ML research | Sigmoid neurons | `sigma(0.2) = 0.550` |
| 05_R5.md | ML research | Backpropagation | Learn the AND rule |
| 06_H1.md | ML and embedded | Floating point | `3.5 = 0x40600000` |
| 07_H2.md | ML and embedded | Latency | Reproduce the listed ratios |
| 08_H3.md | ML and embedded | Endianness | Show `78 56 34 12` |
| 09_H4.md | ML and embedded | Bandwidth | Reproduce `12.8` and `25.6 GB/s` |
| 10_H5.md | ML and embedded | Softmax | Reproduce `0.090`, `0.245`, `0.665` |
| 11_E1.md | Embedded | Repository setup | Run tests and fetch a model |
| 12_E2.md | Embedded | Pipeline trace | Follow one token to text |

## Common Report Rules

Use the report name listed in your task file. Write the report by hand in your own words.

R and H reports must contain at least 350 words. E reports must contain at least 300 words.

Each report must contain the resource summary, the maths or code evidence, the output, and the unanswered questions.

Use code blocks for commands and script output. Label each output with the command that produced it.

## Common Work Order

1. Read the assigned resource.
2. Write a short summary without copying the source.
3. Solve the maths by hand.
4. Write the reproduction script.
5. Run the script and record its output.
6. Write the report.
7. Complete the evidence checklist.
8. Ask your pair to review the report.

## Project Resources

- Project repository: https://github.com/slvDev/esp32-ai
- Published results: https://github.com/slvDev/esp32-ai/blob/main/RESULTS.md
- TinyStories paper: https://arxiv.org/abs/2305.07759
- Gemma 3n PLE: https://ai.google.dev/gemma/docs/gemma-3n

## Timeline

- Week 1: Complete the assigned fundamentals or repository task.
- Weeks 2-4: Reproduce the project on the host.
- Weeks 5-6: Verify results on the ESP32-S3 N16R8.
- Weeks 7-8: Build and test a practical use case.
