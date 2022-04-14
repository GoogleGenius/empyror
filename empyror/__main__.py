import os

from empyror import build_bot


if __name__ == "__main__":
    if os.name != "nt":
        import uvloop

        uvloop.install()

    build_bot().run()
