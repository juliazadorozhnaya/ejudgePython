import sys
import zlib

def read_varint(stream):
    value = 0
    while True:
        byte = ord(stream.read(1))
        value = (value << 7) | (byte & 0x7f)
        if (byte & 0x80) == 0:
            break
    return value

def read_git_object(stream):
    header = stream.read(4)
    if len(header) != 4:
        return "unknown:"

    if header[:2] == b'PK':
        version = int.from_bytes(stream.read(4), byteorder='big')
        obj_count = int.from_bytes(stream.read(4), byteorder='big')
        return f"pack: {version} {obj_count}"

    if header == b'\xfftOc':
        stream.read(8)  # Skip next 8 bytes
        size = read_varint(stream)
        return f"index: {size}"

    # Decompress and process a Git object
    decompressed = zlib.decompress(stream.read())
    space = decompressed.find(b' ')
    null = decompressed.find(b'\x00', space)
    obj_type = decompressed[:space].decode('ascii')
    size = int(decompressed[space:null].decode('ascii'))

    if obj_type == 'blob':
        return f"blob: {size}"
    elif obj_type == 'tree':
        tree_data = decompressed[null + 1:]
        entries = []
        while tree_data:
            mode_end = tree_data.find(b' ')
            mode = tree_data[:mode_end].decode('ascii')
            tree_data = tree_data[mode_end + 1:]
            sha1_end = tree_data.find(b'\x00')
            sha1 = tree_data[:sha1_end].hex()
            tree_data = tree_data[sha1_end + 21:]
            name_end = tree_data.find(b'\n')
            name = tree_data[:name_end].decode('utf-8')
            tree_data = tree_data[name_end + 1:]
            entries.append(f"{sha1} {mode} {name}")
        return "tree:\n  " + "\n  ".join(entries)
    elif obj_type == 'tag':
        return f"tag: {decompressed[null + 1:]}".split('\n')[0]
    elif obj_type == 'commit':
        return f"commit: {decompressed[null + 1:]}".split('\n')[0]
    else:
        return f"unknown object: {obj_type} {size}"

# Считывание файла из стандартного ввода
if len(sys.argv) != 2:
    print("Usage: python git_object_reader.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]
with open(file_path, 'rb') as file:
    result = read_git_object(file)
    print(result)
