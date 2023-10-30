import math

## max System voltage 17
## maximum load 10A


max_system_voltage = 20
max_load = 15
max_fsv_voltage = 0.320
max_system_voltage = int(input(f"System Voltage [{max_system_voltage}]: ") or max_system_voltage)
max_load = float(input(f"Load [{max_load}]: ") or max_load)
max_fsv_voltage = float(input(f"Full scale value [{max_fsv_voltage}]: ") or max_fsv_voltage)

print(f"system voltage: {max_system_voltage}, load: {max_load}, full scale voltage: {max_fsv_voltage}")

r_shunt = math.ceil((max_fsv_voltage / max_load)*1000)/1000
## r_shunt = (max_fsv_voltage / max_load)

fs_shunt_current = max_fsv_voltage / r_shunt 

max_power = max_load * max_fsv_voltage

print(f"\n======================================\n")
print(f"r_shunt: {r_shunt}Ω, max current: {math.ceil(fs_shunt_current)}A, power: {max_power}W")

min_current_lsb = max_load / 2**15
max_current_lsb = max_load / 2**12

print (f"min current_lsb: {math.ceil(min_current_lsb*10**6)}µA, max current_lsb: {math.ceil(max_current_lsb*10**6)}µA")

current_lsb = math.ceil(min_current_lsb*10000)/10000

print(f"current_lsb: {current_lsb*10**6}µA")

calibration = math.trunc(0.04096/(current_lsb * r_shunt))
print(f"Calibration: {calibration} → {hex(calibration)}")
print(f"\n======================================\n")

print(f"\n========        Example       ========\n\n")

## Shunt Voltage
bus_voltage_plus = float(input(f"Bus Voltage +ve [{max_system_voltage}]: ") or max_system_voltage)
load_current = float(input(f"Load current [{max_load}]: ") or max_load)

r_shunt_vd = load_current * r_shunt

print(f"Shunt resistor voltage drop: {r_shunt_vd} V")
bus_voltage_neg = bus_voltage_plus - r_shunt_vd

print(f"Bus Voltage -ve {bus_voltage_neg}")

bus_v_reg = int(bus_voltage_neg * 100)<<3

print(f"Bus Voltage Register {hex(bus_v_reg)}")
## Bus Voltge
## Current
## Power

