from bot import main


def run_main():
    try:
        main()
    except Exception as ex:
        print("Exception:", ex)


if __name__ == "__main__":
    run_main()
