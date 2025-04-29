import os

image_dir = './data/celeba/img_align_celeba'
with open('./data/celeba/list_eval_partition.txt') as f:
    lines = f.readlines()

missing = []
for line in lines:
    fname = line.split()[0]
    if not os.path.exists(os.path.join(image_dir, fname)):
        missing.append(fname)

print(f"Total missing files: {len(missing)}")
for m in missing[:10]:
    print("❌", m)
