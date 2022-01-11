start "Split data" python master_proc.py
timeout 15
@echo off
for /f %%A in ('dir data ^| find "File(s)"') do set cnt=%%A
echo File count = %cnt%
FOR /L %%A IN (1,1,%cnt%) DO (
   IF %%A == 1 (
   	start "nick%%A" python new_api_tool_v2.py data/nick%%A.txt output%%A.txt 103.90.229.13:9028 phamductrungit510 6f50fd91f
   )
   IF %%A == 2 (
   	start "nick%%A" python new_api_tool_v2.py data/nick%%A.txt output%%A.txt 103.90.229.16:9028 phamductrungit510 6f50fd91f
   )
   IF %%A == 3 (
   	start "nick%%A" python new_api_tool_v2.py data/nick%%A.txt output%%A.txt 103.90.230.29:9028 phamductrungit510 6f50fd91f
   )
   IF %%A == 4 (
   	start "nick%%A" python new_api_tool_v2.py data/nick%%A.txt output%%A.txt 103.90.229.153:9028 phamductrungit510 6f50fd91f
   )
   IF %%A == 5 (
   	start "nick%%A" python new_api_tool_v2.py data/nick%%A.txt output%%A.txt 103.90.229.119:9028 phamductrungit510 6f50fd91f
   )
   IF %%A == 6 (
   	start "nick%%A" python new_api_tool_v2.py data/nick%%A.txt output%%A.txt 103.90.229.123:9028 phamductrungit510 6f50fd91f
   )
   IF %%A == 7 (
   	start "nick%%A" python new_api_tool_v2.py data/nick%%A.txt output%%A.txt 103.90.229.128:9028 phamductrungit510 6f50fd91f
   )
   IF %%A == 8 (
   	start "nick%%A" python new_api_tool_v2.py data/nick%%A.txt output%%A.txt 103.90.229.173:9028 phamductrungit510 6f50fd91f
   )
   IF %%A == 9 (
   	start "nick%%A" python new_api_tool_v2.py data/nick%%A.txt output%%A.txt 103.90.229.175:9028 phamductrungit510 6f50fd91f
   )
   IF %%A == 10 (
   	start "nick%%A" python new_api_tool_v2.py data/nick%%A.txt output%%A.txt 103.90.228.245:9028 phamductrungit510 6f50fd91f
   )
   IF %%A == 11 (
   	start "nick%%A" python new_api_tool_v2.py data/nick%%A.txt output%%A.txt 103.90.231.73:9008 phamductrungit510 6f50fd91f
   )
   IF %%A == 12 (
   	start "nick%%A" python new_api_tool_v2.py data/nick%%A.txt output%%A.txt 103.90.231.74:9008 phamductrungit510 6f50fd91f
   )
   IF %%A == 13 (
   	start "nick%%A" python new_api_tool_v2.py data/nick%%A.txt output%%A.txt 103.90.231.75:9008 phamductrungit510 6f50fd91f
   )
   IF %%A == 14 (
   	start "nick%%A" python new_api_tool_v2.py data/nick%%A.txt output%%A.txt 103.90.231.76:9008 phamductrungit510 6f50fd91f
   )
   IF %%A == 15 (
   	start "nick%%A" python new_api_tool_v2.py data/nick%%A.txt output%%A.txt 103.90.231.84:9045 phamductrungit510 6f50fd91f
   )
   IF %%A == 16 (
   	start "nick%%A" python new_api_tool_v2.py data/nick%%A.txt output%%A.txt 103.90.230.175:9045 phamductrungit510 6f50fd91f
   )
   IF %%A == 17 (
   	start "nick%%A" python new_api_tool_v2.py data/nick%%A.txt output%%A.txt 103.90.230.176:9045 phamductrungit510 6f50fd91f
   )
   IF %%A == 18 (
   	start "nick%%A" python new_api_tool_v2.py data/nick%%A.txt output%%A.txt 103.90.230.177:9045 phamductrungit510 6f50fd91f
   )
   IF %%A == 19 (
   	start "nick%%A" python new_api_tool_v2.py data/nick%%A.txt output%%A.txt 103.90.228.163:8889 phamductrungit510 6f50fd91f
   )
   IF %%A == 20 (
   	start "nick%%A" python new_api_tool_v2.py data/nick%%A.txt output%%A.txt 103.90.228.175:8889 phamductrungit510 6f50fd91f
   )
   IF %%A == 21 (
   	start "nick%%A" python new_api_tool_v2.py data/nick%%A.txt output%%A.txt 103.90.228.188:8889 phamductrungit510 6f50fd91f
   )
)

timeout 2000
start "summarize data" python sumarize_output.py %cnt%
pause