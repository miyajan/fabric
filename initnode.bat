set PATH=c:\cygwin\bin;%PATH%

cd %~dp0

bash --login -c "cd /cygdrive/c/Users/cybozu/Desktop/selenium; fab -f initnode.py initnode"
