import argparse
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / 'packages.json'


def load_packages():
    if DATA_FILE.exists():
        with DATA_FILE.open('r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_packages(packages):
    with DATA_FILE.open('w', encoding='utf-8') as f:
        json.dump(packages, f, ensure_ascii=False, indent=2)


def init_db(args):
    if DATA_FILE.exists():
        print('Veri dosyası zaten mevcut.')
    else:
        save_packages([])
        print('Veri dosyası oluşturuldu.')


def add_package(args):
    packages = load_packages()
    if args.name in packages:
        print(f"'{args.name}' zaten ekli.")
        return
    packages.append(args.name)
    save_packages(packages)
    print(f"'{args.name}' eklendi.")


def remove_package(args):
    packages = load_packages()
    if args.name not in packages:
        print(f"'{args.name}' bulunamadı.")
        return
    packages.remove(args.name)
    save_packages(packages)
    print(f"'{args.name}' silindi.")


def list_packages(args):
    packages = load_packages()
    if not packages:
        print('Kayıtlı paket yok.')
    else:
        for pkg in packages:
            print(f'- {pkg}')


def main():
    parser = argparse.ArgumentParser(description='Basit pa manager')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('init', help='Veri dosyasını oluştur')

    add_parser = subparsers.add_parser('add', help='Paket ekle')
    add_parser.add_argument('name')

    remove_parser = subparsers.add_parser('remove', help='Paket sil')
    remove_parser.add_argument('name')

    subparsers.add_parser('list', help='Paketleri listele')

    args = parser.parse_args()

    if args.command == 'init':
        init_db(args)
    elif args.command == 'add':
        add_package(args)
    elif args.command == 'remove':
        remove_package(args)
    elif args.command == 'list':
        list_packages(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
