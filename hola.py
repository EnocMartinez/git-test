#!/usr/bin/env python3
import rich

rich.print("[green]Hello!")
animals = ["cat", "dog", "rabbit"]
for animal in animals:
    rich.print(f"[cyan]{animal}")

for i in range(3):
    rich.print(f"[blue] {i}")

