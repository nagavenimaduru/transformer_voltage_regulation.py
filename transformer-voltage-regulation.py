print("==========================================")
print("  TRANSFORMER VOLTAGE REGULATION CALCULATOR")
print("==========================================")

no_load_voltage = float(input("Enter no-load voltage (V): "))
full_load_voltage = float(input("Enter full-load voltage (V): "))

if no_load_voltage <= 0 or full_load_voltage <= 0:
    print("\nPlease enter positive voltage values.")
elif no_load_voltage < full_load_voltage:
    print("\nNo-load voltage should normally be greater than or equal to full-load voltage.")
else:
    voltage_regulation = (
        (no_load_voltage - full_load_voltage)
        / full_load_voltage
    ) * 100

    voltage_drop = no_load_voltage - full_load_voltage

    print("\n------------- RESULTS -------------")
    print(f"No-load Voltage       : {no_load_voltage:.2f} V")
    print(f"Full-load Voltage     : {full_load_voltage:.2f} V")
    print(f"Voltage Drop          : {voltage_drop:.2f} V")
    print(f"Voltage Regulation    : {voltage_regulation:.2f}%")
    print("-----------------------------------")
