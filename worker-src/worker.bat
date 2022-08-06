@ECHO OFF
IF [%1] == [] GOTO ERROR
IF /I [%1] == [-h] GOTO ERROR
CALL :CHECKIP _result %1
IF %_result% == False GOTO ERROR
DIR /b ray.exe /s 2> nul > %temp%\raypathfindtmp
SET /p exe_path=<%temp%\raypathfindtmp
DEL %temp%\raypathfindtmp
SET init_script=%exe_path:ray.exe=activate.bat% 
CALL %init_script%
%exe_path% start --num-cpus 1 --address=%1:6379
:LOOP
ECHO.
ECHO.
ECHO =====================
ECHO ^| The worker program^|
ECHO =====================
ECHO Input options:
ECHO "stop" : to disconnect from server and quit the program
ECHO "status" : to list tasks and resources connect to server
SET /P PARAM="> "
IF /I [%PARAM%] == [stop] GOTO DONE
IF /I [%PARAM%] == [status] %exe_path% status
GOTO LOOP
:CHECKIP
SETLOCAL
SET _var=%1
SET _ip=%~2
SET _prefixlenght=%_ip:*/=%
CALL SET _ip=%%_ip:/%_prefixlenght%=%%
FOR /F "usebackq tokens=*" %%g in (`POWERSHELL -c "$ipaddrobj = [ipaddress]::Any ; if (!([ipaddress]::TryParse('%_ip%', [ref]$ipaddrobj))){if (!([ipaddress]::TryParse('%_ip%'.split(':')[0], [ref]$ipaddrobj))){return $false}} ; return $true"`) do (set _ipvalid=%%g)
ENDLOCAL & set %_var%=%_ipvalid%
GOTO :EOF
:ERROR
ECHO usage: worker.bat [-h] head
ECHO.
ECHO Start worker process and connect to task server to share the
ECHO computation power of this device.
ECHO.
ECHO positional arguments:
ECHO   head        IP address of task server.
ECHO.
ECHO optional arguments:
ECHO  -h, --help  show this help message and exit
EXIT /B 1
:DONE
%exe_path% stop
EXIT /B 1