TinyML Platforms Benchmarking: A Report

Problem / State of the Art

Running machine learning models used to mean relying on powerful servers or at least a smartphone, because training and inference both need a lot of memory and computing power. Over time, researchers found ways to shrink models through techniques like quantization and pruning, which made it possible to run inference on smaller mobile devices. TinyML pushes this idea even further by trying to run ML models directly on microcontrollers, tiny chips that consume less than a milliwatt of power and often run on a coin sized battery. Because this field is so new, a lot of different frameworks have popped up to help developers convert and deploy models on these constrained devices, including TensorFlow Lite Micro, STM32Cube.AI, Embedded Learning Library, ARM-NN, AIfES, MicroMLGen, and m2cgen. Each of these tools takes a different approach and supports different hardware, which makes it hard for someone to know which one actually fits their project best.

Goal

The paper sets out to compare two of the most widely used TinyML frameworks head to head: TensorFlow Lite Micro running on an Arduino Nano 33 BLE, and STM32Cube.AI running on an STM32 NucleoF401RE. The authors want to give developers a standardized way to judge which framework suits a particular application, instead of just going with whichever one is more popular or better documented.

Challenges

Since TinyML is such a young field, there isn't an agreed upon way to benchmark these frameworks yet. Benchmarks can either focus narrowly on low level operations like matrix multiplication, which ignores real world constraints such as memory bandwidth, or they can be so broad that the actual thing being measured gets buried inside a larger application. Another challenge is making sure a comparison is fair. Since the two frameworks run on completely different hardware, the authors had to keep everything else identical, meaning the same training data, the same model architecture, and the same evaluation parameters for both platforms, so that any difference in results could be attributed to the framework itself.

Key Mechanism

The team built two separate applications to test the frameworks. The first is a gesture recognition task where a convolutional neural network reads accelerometer data from an onboard IMU sensor and classifies hand drawn letters like O, H, G, and C. The second is a wake word spotting task, similar to how voice assistants listen for a trigger word, using a dataset of short speech samples for ten different command words. Both models were trained using Keras and TensorFlow Lite, then converted for each platform. To fit inside the tight memory of a microcontroller, the models were quantized from 32 bit floating point down to 8 bit integers, which shrinks the file size considerably while trying to keep accuracy intact.

Key Results

After quantization, the gesture recognition model dropped from 346KB to 275KB on TensorFlow Lite Micro and to 192KB on STM32Cube.AI, while keeping around 85 percent accuracy. For the wake word task, the model shrank from 650KB down to 288KB and 247KB respectively. When it came to actually running these models, STM32Cube.AI was clearly faster and lighter for gesture recognition, taking just 9 milliseconds for inference compared to 30 milliseconds on TensorFlow Lite Micro. For wake word spotting the gap narrowed a lot, with STM32Cube.AI at 211 milliseconds and TensorFlow Lite Micro close behind at 193 milliseconds, meaning TensorFlow Lite Micro was actually a touch faster there despite using more memory.

Strengths and Improvements

The comparison is well designed because the authors kept the model architecture and training data consistent across both platforms, which makes the results genuinely comparable rather than an apples to oranges situation. The paper is also useful as a quick reference thanks to its framework comparison table covering algorithms, compatible platforms, and licensing. That said, the study only tests two applications on two devices, so the conclusions may not hold up across other model types like decision trees or larger, more complex neural networks. It would also help to know more about power consumption, since that is one of the main selling points of TinyML in the first place, and the paper does not report it directly.

What I Learned or Liked

What stood out to me is how much of a trade off there is between openness and performance in this space. STM32Cube.AI performs better in these tests but only works on STM32 hardware, while TensorFlow Lite Micro is a bit slower yet works across many more devices and stays open source. That is a genuinely useful thing to know before picking a framework for a project. I also liked seeing quantization applied in a concrete way, since it made the abstract idea of shrinking a model into something I could actually see reflected in the KB numbers before and after.

Summary

This paper benchmarks two popular TinyML frameworks, TensorFlow Lite Micro and STM32Cube.AI, on gesture recognition and wake word spotting tasks. STM32Cube.AI came out ahead in memory usage and speed for gesture recognition, and stayed competitive for wake word spotting, but it only works with STM32 hardware. TensorFlow Lite Micro trailed slightly in performance but wins on flexibility and open source availability across many devices. The authors conclude that STM32Cube.AI suits memory limited and performance heavy applications, while TensorFlow Lite Micro remains the better choice when broad hardware support matters more.