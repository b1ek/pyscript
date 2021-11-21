import os
import time

SORTINGDIR = r"C:\Users\blek\Desktop"
PRINT_FAILED = True
FILESFILTER = {
    # Images
    ".bmp": "Images",
    ".png": "Images",
    ".gif": "Images\\Gifs",
    ".ico": "Images\\Icons",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".webp": "Images",

    # Text files
    ".txt": "Texts",

    # Documents
    ".pdf": "Documents",
    ".md": "Documents",
    ".rtf": "Documents",
    ".xls": "Documents",
    ".xlsx": "Documents",
    ".csv": "Documents",
    ".ppt": "Documents\\Presentations",
    ".pptx": "Documents\\Presentations",
    ".py": "Documents\\Python programs",
    ".cpp": "Documents\\C++ programs",
    ".hpp": "Documents\\C++ programs",
    ".c": "Documents\\C programs",
    ".h": "Documents\\C programs",
    ".cs": "Documents\\C# programs",
    ".java": "Documents\\Java programs",
    ".js": "Documents\\.JS programs",
    ".ts": "Documents\\.TS programs",
    ".chm": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".htm": "Documents",
    ".html": "Documents",
    ".xml": "Documents\\Data files",
    ".json": "Documents\\Data files",
    ".yaml": "Documents\\Data files",
    ".db": "Documents\\Data files",
    ".sqlite3": "Documents\\Data files",
    ".css": "Documents",

    # Archive files
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".rar4": "Archives",
    ".cab": "Archives",
    ".jar": "Archives\\Java Archive",
    ".tar": "Archives",
    ".gz": "Archives",
    ".iso": "Archives\\CD Disk image",

    # Programs
    ".exe": "Executables",
    ".msi": "Executables\\MS Install",
    ".cmd": "Executables\\Cmd script",
    ".bat": "Executables\\Cmd script",
    ".sh":  "Executables\\Shell script",
    ".swf":  "Executables\\Shockwave Flash",
    ".gadget":  "Executables\\Win7 gadgets",
    ".o": "Executables\\Object file",
    ".com": "Executables\\MS-DOS .COM Executables",
    
    # System files
    ".dll": "System files",
    ".lib": "System files",
    ".pdb": "System files",
    ".scr": "System files",

    # Videos
    ".mp4": "Movies",
    ".m4v": "Movies",
    ".mov": "Movies",
    ".mkv": "Movies",
    ".avi": "Movies",
    ".webm": "Movies",
    
    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".ogg": "Audio",

    # 3D object
    ".obj": "3D",
    ".blend": "3D",

    # Other
    ".lnk": ".Programs",
    ".url": ".Programs",
}
IGNOREFILEPREFIX = "." # .file.txt - no sorting
                       #  file.txt - sorting allowed

def main() -> int:
    sortdir = SORTINGDIR
    moved = 0
    timestart = time.time()
    f = open(SORTINGDIR + f"\\{IGNOREFILEPREFIX}backup.md", "w+")
    st = ""
    st = "".join([ " - " + ff + "\n" for ff in os.listdir(SORTINGDIR) ])
    f.write("## DIRECTORY IMAGE BACKUP<br/>\n### Made by blek!<br/>\n---------------------------\nCurrent files/dirs:\n" + st)
    f.close()

    for file in os.listdir(SORTINGDIR):
        if (file.startswith(".")== False) and os.path.isdir(file) == False:
            try:
                spl = file.split(".")
                ext = "." + spl[len(spl)-1].lower()
                isin = False
                try:
                    FILESFILTER[ext]
                    isin = True
                except Exception: 0
                if isin:
                    path: str = os.path.join(sortdir, FILESFILTER[ext], file)
                    pathd: str = os.path.join(sortdir, FILESFILTER[ext])
                    file: str = os.path.join(sortdir, file)
                    
                    if os.path.exists(pathd):
                        os.rename(file, path)
                    else:
                        os.mkdir(pathd)
                        os.rename(file, path)
                    print("Moved " + file + " to " + path)
                    moved += 1
            except Exception as e:
                if PRINT_FAILED:
                    try:
                        print("\nFailed to move \"" + file + "\": " + ''.join(e.args))
                    except Exception:0
                        #print("\nFailed to move \"" + file + "\":\n" + "No error description")
    finishtime = time.time()
    print(f"Moved {moved} files in {float(int((finishtime - timestart) * 100)) / 100} seconds.")
if __name__ == "__main__":
    exit(main())