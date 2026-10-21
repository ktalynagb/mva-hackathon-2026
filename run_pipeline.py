"""Punto de entrada unico del analisis (tarea D2).

Corre en orden los pasos reproducibles del proyecto y para en el primero que falle.

Uso:
    python run_pipeline.py                     # todos los pasos
    python run_pipeline.py --listar            # ver los pasos sin correrlos
    python run_pipeline.py --solo farmacos,figuras
    python run_pipeline.py --desde farmacos
    python run_pipeline.py --thermompnn DIR    # agrega el calculo de estabilidad (B3) con la salida de ThermoMPNN

Requisitos: entorno de requirements.txt y conexion a internet (gnomAD, Ensembl, UniProt,
AlphaFold, DGIdb, Open Targets, openFDA, EMA). El paso "diagnostico" necesita el VCF del
paciente en data/raw/ (ver README, "Como reproducir").
"""
import argparse
import subprocess
import sys
import time
from pathlib import Path

RAIZ = Path(__file__).resolve().parent

# (id, descripcion, script, necesita_vcf)
PASOS = [
    ("genes", "Unir los grupos de genes del equipo en config/genes_candidatos.txt", "scripts/unir_grupos_genes.py", False),
    ("diagnostico", "Diagnóstico diferencial en el panel, con consecuencia en MANE (A3, A8)", "scripts/diagnostico_diferencial.py", True),
    ("dominante", "Modelo dominante en 92 genes de PanelApp: segundo diagnóstico (A10)", "scripts/modelo_dominante.py", True),
    ("genes_equipo", "Modelo dominante en los 10 genes propuestos por el equipo (C8)", "scripts/analisis_genes_equipo.py", True),
    ("alelo2", "Evidencia estructural de p.Asn1002Lys: AlphaFold, ClinVar, conservación (B3)", "scripts/evidencia_alelo2.py", False),
    ("farmacos", "Lista larga de fármacos con aprobación FDA/EMA (C3)", "scripts/lista_larga_farmacos.py", False),
    ("farmacogenetica", "Fenotipos de metabolizador para ciclofosfamida y sirolimus (C7)", "scripts/farmacogenetica.py", True),
    ("figuras", "Figuras 1 y 2 del informe (A5, B5)", "scripts/figuras_informe.py", False),
]


def main():
    ap = argparse.ArgumentParser(description="Pipeline MVA Hackathon 2026 · Track 2")
    ap.add_argument("--listar", action="store_true", help="mostrar los pasos y salir")
    ap.add_argument("--solo", help="pasos a correr, separados por coma")
    ap.add_argument("--desde", help="correr desde este paso en adelante")
    ap.add_argument("--thermompnn", metavar="DIR", help="carpeta con la salida de ThermoMPNN para el paso de estabilidad")
    args = ap.parse_args()

    pasos = [(i, d, [s], v) for i, d, s, v in PASOS]
    if args.thermompnn:
        tras_alelo2 = [p[0] for p in pasos].index("alelo2") + 1
        pasos.insert(tras_alelo2, ("estabilidad", "ΔΔG de p.Asn1002Lys con ThermoMPNN (B3)",
                                   ["scripts/estabilidad_alelo2.py", "--dir", args.thermompnn], False))
    ids = [p[0] for p in pasos]

    if args.listar:
        for i, d, s, v in pasos:
            print(f"  {i:12} {d}{'  [necesita el VCF]' if v else ''}")
        return 0

    if args.solo:
        pedidos = [x.strip() for x in args.solo.split(",")]
        desconocidos = set(pedidos) - set(ids)
        if desconocidos:
            sys.exit(f"Pasos desconocidos: {', '.join(sorted(desconocidos))}. Opciones: {', '.join(ids)}")
        pasos = [p for p in pasos if p[0] in pedidos]
    elif args.desde:
        if args.desde not in ids:
            sys.exit(f"Paso desconocido: {args.desde}. Opciones: {', '.join(ids)}")
        pasos = pasos[ids.index(args.desde):]

    if any(v for *_, v in pasos) and not list((RAIZ / "data" / "raw").glob("*.vcf.gz")):
        sys.exit("Falta el VCF en data/raw/. Descárgalo con scripts/download_data.py (README, 'Cómo reproducir'), "
                 "o salta ese paso con --solo.")

    resumen = []
    for i, d, comando, _ in pasos:
        print(f"\n=== [{i}] {d}", flush=True)
        t0 = time.time()
        r = subprocess.run([sys.executable, *comando], cwd=RAIZ)
        resumen.append((i, r.returncode, time.time() - t0))
        if r.returncode != 0:
            break

    print("\nResumen")
    for i, codigo, seg in resumen:
        print(f"  {i:12} {'OK' if codigo == 0 else f'FALLÓ ({codigo})':10} {seg:6.0f} s")
    return 0 if all(c == 0 for _, c, _ in resumen) and len(resumen) == len(pasos) else 1


if __name__ == "__main__":
    sys.exit(main())
