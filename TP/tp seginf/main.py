import argparse
from url import app

def main():
    parser = argparse.ArgumentParser(description="Soy la descripción cuando mandan --help")
    # sanitizar argument
    parser.add_argument("--tecnologia", type=str, help="Tu tecnologia")
    
    args = parser.parse_args()

    if args.tecnologia == 'url':
        app.run()


if __name__ == "__main__":
    main()
