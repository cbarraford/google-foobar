def toString(version):
    version = [str(x) for x in version]
    return '.'.join(version)

def answer(versions):
    versions = [[int(y) for y in x.split(".")] for x in versions]
    versions = sorted(versions)
    return [toString(x) for x in versions]


print answer(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
print answer(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
