set PATH=c:\cygwin\bin;%PATH%

cd %~dp0

bash --login -c "cd /cygdrive/c/Users/cybozu/Desktop/fabric; fab updateAll"
pause
