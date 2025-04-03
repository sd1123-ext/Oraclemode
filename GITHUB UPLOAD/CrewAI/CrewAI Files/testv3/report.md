**Anomaly Overview**  
The observed anomaly is that the LT101 (level transmitter) has a reading of 99%. This reading signifies that there is a potential issue with the stripper column, which could lead to operational risks and safety hazards.

**Possible Causes for LT101 Reading 99%**  
| Possible Causes                                                                                                     | Reasoning                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| 1. High Liquid Level in Stripper Column                                                                            | The level transmitter (LT101) reading 99% indicates that the stripper column is nearly full, triggering the high-high (HH) alarm at 95%.                             |
| 2. Valve Malfunction (V107, V108, V200, V201, V202, V203, V300, V301, V302, and V318)                               | If any of these valves are stuck closed or malfunctioning, it could cause an overflow or restricted flow, leading to a high level reading.                                            |
| 3. Flowrate Imbalance Due to Open Bypass Valves (V110, V112, V113a, V113b, V116, V117a, V117b, V121, V402, V403) | Too many valves open could impede or redirect flow to the stripper column, causing unexpected buildup in the column and leading to high level readings.                  |
| 4. Malfunctioning Pump (J100)                                                                                     | An improperly functioning pump may cause inconsistencies in fluid movement, resulting in backflow or stagnant liquid in the stripper column, contributing to high level readings. |
| 5. Pressure Transmitter Error (PT102, PT103, PT104, PDT105)                                                       | Inaccurate pressure transmitters leading to misreadings can affect flow rates, thus contributing to the high LT101 reading due to miscalculated pressure.        |
| 6. Measured Flowrate Exceeding Maximum Capacity (FT103 or FT104)                                                 | Flow rates exceeding operational limits can lead to backup levels in the stripper column resulting in a high reading on LT101.                   |
| 7. Incorrect Calibration of LT101                                                                                  | If LT101 is not properly calibrated, it may provide false readings, misleading personnel about the actual liquid level, and reflecting it higher than reality.          |

**Explanation of the Chosen Cause**  
The most likely cause for the LT101 reading of 99% is the **High Liquid Level in the Stripper Column**. This is evidenced by the activation of the high-high alarm at 95%, indicating a critical condition that warrants immediate attention. Other causes, while plausible, are less direct in their impact compared to the clear signal from the liquid level in the stripper column.

**Effects of the LT101 Reading 99%**  
The consequence of this high level reading can lead to potential overflow in the stripper column, posing risks such as:
- Equipment damage due to excessive pressure
- Compromised safety leading to hazardous situations
- Production losses if operations must be halted to address the situation

**Identifying the Cause**  
The root cause of the issue has been linked primarily to the liquid level exceeding normal operational limits in the stripper column, which is evident from the continuous high reading on LT101.

**Solution to Rectify the LT101 Reading**  
To effectively address the anomaly of LT101 reading 99%, the following solutions are recommended:  

1. **Immediate Actions:**
   - **Adjust Flow Rates:** Verify flow rates through FT103 and FT104. If they exceed 12000 kg/hr, adjustments to throttle incoming flow should be made to mitigate column flooding.
   - **Inspect Stripper Column:** Confirm the liquid level visually and downscale operations if liquid levels exceed appropriate thresholds. Engage emergency protocols for fluid displacement if necessary.

2. **Assess Valves:**
   - **Functionality Check:** Inspect valves (V107, V108, V200, etc.) for blockages or malfunctions. Open shut valves and clear obstructions to restore normal flow.
   - **Bypass Valve Control:** Review the operational status of bypass valves, making necessary adjustments to restrict flow deviations.

3. **Pump Analysis:**
   - **Pump Inspection:** Conduct a thorough check on pump J100 for operational issues that may hinder liquid movement. Repair or replace as needed.

4. **Transmitters and Calibration Review:**
   - **Accuracy Checks on Pressure Transmitters:** Review PT102, PT103, PT104 for accuracy. Recalibrate faulty units and ensure operational integrity.
   - **LT101 Calibration Verification:** Confirm LT101's calibration accuracy against known standards and adjust accordingly if discrepancies are found.

5. **Monitoring and Documentation:**
   - Continuously track LT101 readings post-implementation of corrective actions to ensure stability. Document actions taken and findings for future reference.

6. **Long-term Consideration:**
   - **Routine Maintenance:** Develop a maintenance schedule for the stripper column and components to preemptively catch issues.
   - **Training Staff:** Equip operational staff with the knowledge needed to recognize high-level alarms and effective remediation protocols, promoting a safe operational environment.

By effectively implementing these corrective measures, the high LT101 reading problem can be resolved, returning the process to normal, safe operating conditions.