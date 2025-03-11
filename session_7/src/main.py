import time

class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.start_time = time.time() 
        print(f"Opening file {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()  
        self.elapsed_time = (self.end_time - self.start_time) * 10000
        print(f"Closing file {self.filename}")
        if self.file:
            self.file.close()
        print(f"File operation completed in {self.elapsed_time:.4f} microseconds.")
        return False

if __name__ == "__main__":
    with FileOpener("example.txt", "w") as f:
        f.write("Hello, Context Managers!\n" *10000)

    



    