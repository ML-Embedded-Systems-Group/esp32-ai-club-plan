def bandwidth_gbps(bus_bits, clock_mhz, ddr=True):
    transfers_per_sec = clock_mhz * 1e6 * (2 if ddr else 1)
    return (bus_bits / 8) * transfers_per_sec / 1e9

memories = [
    ("DDR3-1600", 64, 800),
    ("DDR3-1866", 64, 933),
    ("DDR4-2400", 64, 1200),
    ("DDR4-3200", 64, 1600),
]

print("Memory bandwidth table")
print("Memory       Bus(B)  Transfer rate(MT/s)  Bandwidth(GB/s)")
for name, bits, clock in memories:
    bw = bandwidth_gbps(bits, clock)
    print(f"{name:<11} {bits//8:<7} {clock*2:<21} {bw:.3f}")

print("\nVerification")
for name, expected in [("DDR3-1600", 12.8), ("DDR4-3200", 25.6)]:
    bits, clock = next((b, c) for n, b, c in memories if n == name)
    actual = bandwidth_gbps(bits, clock)
    print(f"{name}: {'PASS' if abs(actual - expected) < 1e-9 else 'FAIL'}")

bus_bytes = 8 / 8
psram_clock = 80e6
psram_transfers = psram_clock * 2
psram_bw = bus_bytes * psram_transfers
values_per_token = 14.9e6
bytes_per_value = 0.5
tokens_per_sec = 9.88
bytes_per_token = bytes_per_value * values_per_token
required_bw = bytes_per_token * tokens_per_sec

print("\nClub PSRAM workload")
print(f"PSRAM theoretical bandwidth: {psram_bw / 1e9:.3f} GB/s")
print(f"Bytes per token: {bytes_per_token:,.0f} B")
print(f"Required bandwidth: {required_bw / 1e9:.6f} GB/s")
print("PSRAM bus can sustain the workload" if required_bw <= psram_bw
      else "PSRAM bus cannot sustain the workload")
