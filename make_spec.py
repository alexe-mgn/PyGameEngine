import re
import os


def makespec(f, args):
    os.chdir("..")
    if os.path.isfile(f):
        spec = re.sub(r"(.+)\.\w{1,5}", r"\1.spec", f)
        if not os.path.isfile(spec):
            os.system(f"pyi-makespec {f} {args}")
            if os.path.exists("make_data.py"):
                md = "make_data.py"
            else:
                md = None
                for p, ds, fs in os.walk('.'):
                    for f in fs:
                        if f.lower() == 'make_data.py':
                            md = os.path.join(p, f)
                            break
                    if md is not None:
                        break
                if md is not None:
                    with open(spec, mode='r') as sp:
                        spec_code = sp.read()
                    with open(md, mode='r') as md:
                        with open(spec, mode='w') as sp:
                            sp.write(md.read() + '\n' + spec_code.
                                     replace("datas=[]", "datas=datas").
                                     replace("a.binaries,", "a.binaries + chipmunk_libs,")
                                     )
        else:
            raise FileExistsError(f"File {spec} already exists")
    else:
        raise FileNotFoundError(f"Couldn't find file {f}")


if __name__ == '__main__':
    makespec(input("File name:"), input("args: "))
