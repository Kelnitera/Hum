import os

def null_file(root):
  total = 0
  for i in os.listdir(root):
    filepath = os.path.join(root, i)
    if os.path.getsize(filepath) == 0:
      total += 1; os.remove(filepath)
  result = f"{total} File in 0 Bytes"
  return total

def corrupted_image(root):
  total = 0
  for i in os.listdir(root):
    filepath = os.path.join(root, i)
  try:
    file_object = open(filepath, "rb")
    data_object = tf.compat.as_bytes("JFIF") in file_object.peek(10)
  finally:
    file_object.close()
  if not data_object:
    total += 1
    os.remove(filepath)
  result = f"Total Corrupted : {total}"
  return total
