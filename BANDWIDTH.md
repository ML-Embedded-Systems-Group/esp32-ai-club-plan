# H4: ML + Embedded — Week 1: Memory Bandwidth
## 1. What Is Memory Bandwidth?

Memory bandwidth describes how much data a memory interface can transfer in a given amount of time. A useful way to estimate the theoretical peak is to combine the amount of data transferred on each transfer with the number of transfers that can occur each second.
The two important interface quantities here are bus width and transfer rate. A wider bus carries more bits on every transfer. For example, a 64-bit bus carries 8 bytes per transfer. A higher transfer rate means that more of those transfers happen every second.
DDR means double data rate. In this exercise, data is transferred on both clock edges, so an 80 MHz clock gives an effective transfer rate of 160 MT/s. MT/s means million transfers per second; it is not the same unit as MHz. MHz describes clock cycles per second, while MT/s describes data transfers per second.
The theoretical bandwidth is therefore:
Bandwidth = bus width in bytes × transfers per second
For DDR:
Bandwidth = (bus width in bits / 8) × clock frequency × 2
This is a peak interface calculation. It does not guarantee that software will actually achieve that throughput. Memory access patterns, protocol overhead, contention, cache behavior and latency can reduce usable bandwidth. Bandwidth and latency are also different: bandwidth describes how much data can be moved over time, while latency describes how long it takes for an access to begin producing useful data.
For ML, memory bandwidth matters because a workload may spend a significant amount of time moving inputs, weights and outputs rather than doing arithmetic. NVIDIA describes workloads as memory-bound when memory access time is the limiting factor. In an embedded system, the same idea applies: a model can have enough compute capacity but still fail to reach its target throughput if the external memory interface cannot feed the computation fast enough.

## 2. Phase 2 Mathematics

### Problem 1 — DDR3-1600
1. Bus width = 64 bits
2. Convert to bytes:
   64 bits / 8 = 8 bytes/transfer
3. DDR transfers per clock = 2
4. DDR3-1600 effective transfer rate = 1600 MT/s
   This corresponds to a 800 MHz I/O clock with two transfers per clock.
5. Bandwidth:
   8 bytes/transfer × 1,600,000,000 transfers/s
   = 12,800,000,000 bytes/s
6. Convert to GB/s using decimal GB:
   12,800,000,000 / 1,000,000,000
   = 12.8 GB/s
Result: 12.8 GB/s

### Problem 2 — DDR4-3200
1. Bus width = 64 bits
2. Convert to bytes:
   64 / 8 = 8 bytes/transfer
3. Effective transfer rate = 3200 MT/s
4. Bandwidth:
   8 bytes/transfer × 3,200,000,000 transfers/s
   = 25,600,000,000 bytes/s
5. Convert to GB/s:
   25,600,000,000 / 1,000,000,000
   = 25.6 GB/s
Result: 25.6 GB/s

### Problem 3 — Club Chip PSRAM
Given: 8-bit bus, 80 MHz clock, DDR.
1. Bus width = 8 bits
2. Bus width in bytes:
   8 / 8 = 1 byte/transfer
3. Clock frequency = 80 MHz = 80,000,000 Hz
4. Transfers per clock = 2
5. Effective transfer rate:
   80,000,000 × 2 = 160,000,000 transfers/s
   = 160 MT/s
6. Bandwidth:
   1 byte/transfer × 160,000,000 transfers/s
   = 160,000,000 bytes/s
7. Convert to GB/s:
   160,000,000 / 1,000,000,000
   = 0.160 GB/s
Result: 0.160 GB/s (160 MB/s theoretical peak)

## 3. BANDWIDTH_REPRO.py Output
The following was captured by running the supplied script rather than manually typing the values:
Memory bandwidth table
Memory       Bus(B)  Transfer rate(MT/s)  Bandwidth(GB/s)
DDR3-1600      8          1600                12.800
DDR3-1866      8          1866                14.928
DDR4-2400      8          2400                19.200
DDR4-3200      8          3200                25.600

Verification
DDR3-1600: PASS
DDR4-3200: PASS
Club PSRAM workload
PSRAM theoretical bandwidth: 0.160 GB/s
Bytes per token: 7,450,000 B
Required bandwidth: 0.073606 GB/s
PSRAM bus can sustain the workload


## 4. Comparison and Verdict

The DDR3-1600 calculation gives 12.8 GB/s, matching the required reference value. DDR4-3200 gives 25.6 GB/s, also matching the required reference value.
The other table values are approximately 14.928 GB/s for DDR3-1866 and 19.200 GB/s for DDR4-2400. These use the same 64-bit bus assumption and the transfer rates implied by their names.
For the club PSRAM interface, the theoretical peak is 0.160 GB/s. The workload has 14.9 million values per token and each value occupies 0.5 bytes:
0.5 × 14,900,000 = 7,450,000 bytes/token
At 9.88 tokens/s:
7,450,000 × 9.88 = 73,606,000 bytes/s
Therefore the workload requires:
73,606,000 / 1,000,000,000 = 0.073606 GB/s
The theoretical PSRAM bandwidth is therefore higher than the calculated workload requirement:
0.160 / 0.073606 ≈ 2
So, under the assumptions in this exercise, the PSRAM bus can theoretically sustain the workload. This does not prove that the actual embedded application will achieve 9.88 tokens/s. Real performance can be lower because the theoretical bandwidth assumes ideal utilization and does not account for all overheads, access patterns, contention, cache behavior, computation time, or latency.

## 5. What I Did Not Understand
I initially treated MHz and MT/s as interchangeable because both appeared as speed numbers. After working through DDR, I understood that MHz refers to clock cycles while MT/s counts actual transfers. With two transfers on every clock, the DDR transfer rate can be twice the clock frequency.


