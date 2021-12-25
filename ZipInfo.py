import sys
import io
import zipfile


total_count = 0
total_size = 0

data = sys.stdin.read()
data = bytes.fromhex(data)

with io.BytesIO(data) as f:
    zf = zipfile.ZipFile(f)
    info_list = zf.infolist()

for v in info_list:
    if not v.is_dir():
        total_count += 1
        total_size += v.file_size


print(total_count, total_size)