# One Line of Wonder — make.fun entry.
import os

def main():
    os.makedirs('/output', exist_ok=True)
    line = "The pencil sharpened down to the eraser still draws the tree, only smaller each time."
    with open('/output/entry.txt', 'wb') as f:
        f.write(line.encode('utf-8'))

if __name__ == "__main__":
    main()
