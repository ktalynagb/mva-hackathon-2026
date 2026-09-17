"""
Descarga selectiva del dataset SageBio/mva-hackathon-2026-data desde Hugging Face.
Uso:
    python scripts/download_data.py --file <nombre_archivo>
    python scripts/download_data.py --list          # listar archivos disponibles
    python scripts/download_data.py --all           # descargar todo (85 GB!)
"""
import argparse
from pathlib import Path
from huggingface_hub import HfApi, hf_hub_download, snapshot_download


REPO_ID = "SageBio/mva-hackathon-2026-data"
DATA_DIR = Path(__file__).parent.parent / "data" / "raw"


def list_files():
    api = HfApi()
    files = api.list_repo_files(REPO_ID, repo_type="dataset")
    print(f"\nArchivos disponibles en {REPO_ID}:")
    for f in files:
        print(f"  {f}")


def download_file(filename: str):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Descargando: {filename}")
    path = hf_hub_download(
        repo_id=REPO_ID,
        filename=filename,
        repo_type="dataset",
        local_dir=str(DATA_DIR),
    )
    print(f"Guardado en: {path}")


def download_all():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Descargando dataset completo (~85 GB) en {DATA_DIR} ...")
    snapshot_download(
        repo_id=REPO_ID,
        repo_type="dataset",
        local_dir=str(DATA_DIR),
    )
    print("Descarga completa.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Descarga datos del hackathon MVA")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--list", action="store_true", help="Listar archivos disponibles")
    group.add_argument("--file", metavar="FILENAME", help="Descargar un archivo específico")
    group.add_argument("--all", action="store_true", help="Descargar todo el dataset (85 GB)")
    args = parser.parse_args()

    if args.list:
        list_files()
    elif args.file:
        download_file(args.file)
    elif args.all:
        confirm = input("Esto descargará ~85 GB. ¿Confirmar? (s/N): ")
        if confirm.lower() == "s":
            download_all()
        else:
            print("Cancelado.")
