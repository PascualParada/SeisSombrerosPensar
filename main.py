"""
Sistema Multiagente con Google ADK
Punto de entrada principal
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from interface.chat_interface import main as chat_main
from utils.helpers import setup_logging
from config.settings import settings
import google.generativeai as genai # Added import

def main():
    """Función principal del sistema"""
    # Configurar logging
    setup_logging()
    
    # Verificar configuración
    if not settings.GOOGLE_API_KEY:
        print("Error: GOOGLE_API_KEY no configurada")
        print("Por favor, configura tu API key de Google en el archivo .env")
        sys.exit(1)

    # Configure the generative AI library
    try:
        genai.configure(api_key=settings.GOOGLE_API_KEY)
        print("Google Generative AI SDK configurado exitosamente.")
    except Exception as e:
        print(f"Error configurando Google Generative AI SDK: {e}")
        sys.exit(1)
    
    print("Iniciando Sistema Multiagente con Google ADK...")
    print(f"Proyecto: {settings.PROJECT_ID}")
    print("Ejecuta: streamlit run main.py")
    
    # Ejecutar interfaz de chat
    chat_main()

if __name__ == "__main__":
    main()