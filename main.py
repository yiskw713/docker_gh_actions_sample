import os


def main() -> None:
    repository = os.getenv("REPOSITORY")
    print(f"Hello world from github actions in {repository}!")


if __name__ == "__main__":
    main()
