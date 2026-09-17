"""
Autenticación en Hugging Face.
Ejecutar con el venv activo:
    .venv\Scripts\activate
    python scripts/hf_login.py
"""
from huggingface_hub import login, whoami

print("=== Login en Hugging Face ===")
print("Pega tu token de acceso (Settings > Access Tokens en hf.co):")
login()

try:
    info = whoami()
    print(f"\nAutenticado como: {info['name']} ({info['email']})")
    print("Token guardado en el cache local de HuggingFace.")
except Exception as e:
    print(f"Error al verificar: {e}")
