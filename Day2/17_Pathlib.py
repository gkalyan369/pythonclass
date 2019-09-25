from pathlib import Path
from pathlib import PurePath


p = Path('.')
# returns path with OS details
dirs = [x for x in p.iterdir() if x.is_dir()]
print(dirs)
# print(dirs[0].name)


p = Path('.')
# display files in the directory
daily_files = list(p.glob('data/*.csv'))

# recursive search in sub directories
# dayend_files = list(p.glob('**/*.csv'))
# dayend_files = list(p.rglob('*.csv'))
for x in daily_files:
    print(x)
print()


# Create & navigate through directories
drive = Path('C:/')
p = Path('.')
# The slash operator helps create child paths
full_path = drive / 'Users' / 'TrgDev' / 'PycharmProjects' / 'TrainingDemo' / 'data'
print(type(full_path))
print(full_path)    # observe the path representation in output (OS specific)


full_path = full_path / '*.csv'
print(full_path)    # full_path is still Path object
dayend_files = list(p.glob(full_path.name))     # get string out of Path object
for x in dayend_files:
    print(x.name)

# PurePath is a generic class
# Also look at concrete classes: Path, PureWindowsPath/PurePosixPath
full_path = PurePath(full_path)
# A tuple giving access to the path’s various components
print(full_path.parts)
print(full_path.drive)
print(full_path.root)

# An immutable sequence providing access to the logical ancestors of the path
# print(list(full_path.parents))
print(full_path.parents[0], '\t', full_path.parents[1])
print(full_path.parent)

# get file extension
print(full_path.suffix)
print(full_path.is_absolute())  # check whether its an absolute or relative path


'''
# try the following functions on your own
Path.cwd()
Path.chmod(mode)
Path.exists()
Path.glob(pattern)
Path.is_dir()
Path.is_file()
Path.iterdir()
Path.mkdir(mode=0o777, parents=False, exist_ok=False)
Path.open(mode='r', buffering=-1, encoding=None, errors=None, newline=None)
Path.rename(target)
Path.rglob(pattern)
Path.rmdir()
Path.unlink()
'''
