import argparse
from pathlib import Path
import threading
from impacket import smbserver


def create_samba_server(directory):
    server = smbserver.SimpleSMBServer(listenPort=5000)
    server.setSMB2Support(True)
    server.addShare("code", str(directory))
    server.start()


def start_share(directory):
    samba_thread = threading.Thread(target=create_samba_server, args=(directory,))
    samba_thread.start()
    print("test")


def main():
    parser = argparse.ArgumentParser(
        description="Share a directory for pair programming"
    )
    parser.add_argument(
        "dir", metavar="directory", type=str, help="the directory to share"
    )
    args = parser.parse_args()
    directory = Path(args.dir).resolve()
    if not directory.is_dir():
        raise ValueError(f"The given path is not a directory '{directory}'")
    start_share(directory)


if __name__ == "__main__":
    main()
