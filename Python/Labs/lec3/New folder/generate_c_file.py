import subprocess

print("this is python....");
subprocess.call(["gcc", "negm.c"])
subprocess.call("./a.out");
print("task is done.")