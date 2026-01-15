# log_parser.py
# Script simple para analizar logs de autenticación

def parse_log(file_path):
    failed_attempts = 0

    try:
        with open(file_path, "r") as log:
            for line in log:
                if "Failed password" in line:
                    failed_attempts += 1

        print(f"Intentos de acceso fallidos detectados: {failed_attempts}")

    except FileNotFoundError:
        print("Archivo de log no encontrado.")

if __name__ == "__main__":
    log_file = "/var/log/auth.log"
    parse_log(log_file)
