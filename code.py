def read_file(file):
  import time
  with open(file, 'r') as f:
    content = f.read()
    print(f"Reading file: {file}")
    time.sleep(5)
    print("Read complete")
  
