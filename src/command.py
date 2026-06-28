from node import node
from typing import Callable
import platform
import socket
import psutil

def init(node : node): ...

def help(node : node): 
    print("""[help] Help command panel
    [arguments] category
        Remember "Every arguments start with - example:  -<argName>".
        output 
        origin
        type
        name
        file
        ignore
        author
        delete
        lenguage

    [commands] category
        help - none.
        sysinfo - none.
        tasks - none.
        task - Taskname.
        end - Taskname.
""")    
    
def sysinfo(node : node):
    print("[sysinfo] Sysinfo command panel")
    print("    [system]", platform.system())
    print("    [release]", platform.release())
    print("    [version]", platform.version())
    print("    [machine]", platform.machine())
    print("    [processor]", platform.processor())
    print("    [architecture]", platform.architecture())
    print("    [hostname]", platform.node())
    print("    [platform]", platform.platform())
    print("    [ip]", socket.gethostbyname(socket.gethostname()))

def end(node : node):

    print("[Warning] Be careful what you're closing; you might be closing a process that's fundamental.")
    ask = input("[Asking] You wanna continue with the end. Y|N? ")

    if ask.lower() != "y":
        return
    
    taskName = node.arguments["name"] if "name" in node.arguments else "[None]"

    for proc in psutil.process_iter():
        if proc.name() == taskName:
            proc.kill()

def task(node : node):
    taskName = node.arguments["name"] if "name" in node.arguments else "[None]"

    for proc in psutil.process_iter():
        if proc.name() == taskName:
            print(f"[process] {proc.name()}")
            print(f"    [pid] {proc.pid}")
            print(f"    [name] {proc.name()}")
            print(f"    [status] {proc.status()}")
            print(f"    [ram] {proc.memory_info().rss}")
            print(f"    [exe] {proc.exe()}")
            print(f"    [started] {proc.create_time()}")
            print(f"    [threads] {proc.threads()}")
    
def tasks(node : node):
    print("[tasks] process running")
    for proc in psutil.process_iter():
        try:
            print(f"    [process] {proc.name()}")
            print(f"        [pid] {proc.pid}")
            print(f"        [name] {proc.name()}")
            print(f"        [status] {proc.status()}")
            print(f"        [exe] {proc.exe()}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

commandList: dict[str, Callable] = {
    
    # DON'T REQUIRE ARGS.

    "init" : {
        "args" : False,
        "func": init
    },

    "help" : {
        "args" : False,
        "func" : help
    },

    "tasks" : {
        "args" : False,
        "func" : tasks
    },


    "sysinfo" : {
        "args" : False,
        "func" : sysinfo
    },

    # REQUIRE ARGS.

    "task" : {
        "args" : {'taskName'},
        "func" : task
    },

    "end" : {
        "args" : {'taskName'},
        "func" : end
    },
}


