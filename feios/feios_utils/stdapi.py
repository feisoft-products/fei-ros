"""The next generation FEIOS API.
The old feios_utils.funcs will be deprecated soon in (at most) 0.5.0 and will be deleted in (at most) 0.8.0.
The new API is faster but uses (relatively) more RAM.
"""
# Imports.
from . import msg
import os
import getpass
import pathlib
import hashlib
# Constants.
version = (0,6,0)
versuffix = "b1"
__null__ = None
indev_name = "0.6.0-pre"

# Functions.
def out(t :str):
    "Printing within line."
    print(t,end="")
    return

def outl(t :str):
    "Printing and start another line."
    print(t)
    return

def run_expr(expr :str):
    "Run an expression using eval()."
    eval(expr)

def clear():
    _cls_cmd = 'cls' if os.name=='nt' else 'clear'
    os.system(_cls_cmd)
    return None

def _out(line :str):
    if len(line) == 3:
        print("",end="")
        return 0
    else:
        if line[3] == " ":
            print(line[4:],end="")
            return 0
        else:
            print(msg.ERR_SPACES)
            return 2

def _outl(line :str):
    if len(line) == 4:
        print("")
        return 0
    else:
        if line[4] == " ":
            print(line[5:])
            return 0
        else:
            print(msg.ERR_SPACES)
            return 2

def _exit(line :str):
    if len(line) == 4:
        exit()
    else:
        exit(line[4:])

def _help():
    with open(r".\feios_utils\help\init.txt") as f:
        a = f.read()
        print(a)

def _version():
    print(f"FEI OS Version {version[0]}.{version[1]}.{version[2]} {versuffix}")
    print("This program and its library is licensed under GPLv3.0+.")
    print(f"Inner development name {indev_name}.")

def _login():
    passwd = getpass.getpass("Password: ")
    passwd = bytes(passwd,encoding="utf-8")
    dig = hashlib.sha256()
    dig.update(passwd)
    _hash = dig.hexdigest()
    if _hash != "2285d2badca55370a0d794a9df898c29922d21504c5c2c7fcb984c75328ad424":
        return False
    return True

def _logout():
    exit()


def _get_file(pof):
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    rawpth = os.path.dirname(os.path.realpath(__file__))
    tmp = pathlib.Path(rawpth)
    tmp2 = tmp.joinpath(".disk")
    finding = str(tmp2)
    realstr = finding + pof
    return realstr

def get_file(pof):
    pth = _get_file(pof)
    return pth

def _get_ext(pte: str):
    pth = _get_file(pte)
    if pth.endswith(".fsc") or pth.endswith(".ext") or pth.endswith(".py"):
        pass
    else:
        return -1
    fc = open(pth,'r').read()
    exec(fc)
    return 0

def _cat(cmd :str):
    cmd = cmd.strip()
    if cmd == 'cat':
        print("Usage:  cat [file | --]")
        print("Like `cat` on POSIX systems,this `cat` can either read contents from a file or read from STDIN.")
        print("If you use `--`,that means you force to read from STDIN.")
        print("If no arguments given,print the help and read from STDIN.")
        s = input()
        print(s)
    elif cmd == 'cat --':
        s = input()
        print(s)
    else:
        realpth = _get_file(cmd[4:])
        f = open(realpth,'r')
        content = f.read()
        print(content)

def _deep_load_ext(extpth,mode):
    if mode == 'python':
        import os
        ret = os.system(f"python {extpth}")
        return ret
    return 3

def load_ext(extpth,mode):
    """Load extensions."""
    ret = _deep_load_ext(extpth,mode)
    return ret

def runbatch(pof):
    """Read a batch script and execute it."""
    try:
        f = open(pof,'r')
    except FileNotFoundError:
        print(msg.ERR_NO_FILE)
        return 2
    except UnicodeDecodeError as e:
        print(msg.ERR_ENCODING(e))
    except OSError:
        print(msg.FATAL_OS)
        return 255
    except Exception:
        print(msg.FATAL_UNKNOWN)
        return 255
    content = f.readlines()
    ret = run(content)
    return ret


def run(l :list[str]):
    "Run a list of str."
    for line in l:
        if line.startswith('#'):
            continue
        elif line.startswith("run"):
            _a = runbatch(line[4:])
            continue
        elif line.startswith("cat"):
            _cat(line)
        elif line.startswith("outl"):
            _a = _outl(line)
            continue
        elif line.startswith("out"):
            _a = _out(line)
            continue
        elif line.startswith("exit"):
            _exit()
        else:
            print(msg.ERR_NO_COMMAND)
    return

def load_cmd(cmd :str):
    """Load only one cmd."""
    if cmd.startswith("#"):
        return
    elif cmd.startswith("run"):
        _a = runbatch(cmd[4:])
        return
    elif cmd.startswith("cat"):
        _cat(cmd)
    elif cmd.startswith("outl"):
        _a = _outl(cmd)
        return
    elif cmd.startswith("out"):
        _a = _out(cmd)
        return
    elif cmd == 'ver' or cmd == 'version':
        _version()
    elif cmd.startswith("exit"):
        _exit(cmd)
    elif cmd.startswith("logout"):
        _logout()
    elif cmd.startswith("help"):
        _help()
    else:
        print(msg.ERR_NO_COMMAND)
    return