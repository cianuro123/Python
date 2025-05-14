import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import signal


class RestartServerHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        self.process = None
        self.start_process()

    def start_process(self):
        print("🚀 Iniciando servidor...")
        # shell=False y lista de argumentos evita problemas en Windows

        self.process = subprocess.Popen(
            self.command, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        global proceso
        proceso = self.process

    def restart_process(self):
        print("🔄 Archivo modificado. Reiniciando servidor...")
        if self.process:
            try:
                # Enviar CTRL_BREAK para cerrar proceso en Windows correctamente
                os.kill(self.process.pid, signal.CTRL_BREAK_EVENT)
                self.process.wait(timeout=3)
            except Exception as e:
                print(f"⚠️ Error al intentar cerrar el servidor: {e}")
        self.start_process()

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            self.restart_process()

    def on_created(self, event):
        if event.src_path.endswith(".py"):
            self.restart_process()


if __name__ == "__main__":
    # Cambiá `main:app` si tu archivo principal tiene otro nombre
    uvicorn_command = ["python", "-m", "uvicorn",
                       "main:app", "--host", "127.0.0.1", "--port", "8000"]

    event_handler = RestartServerHandler(uvicorn_command)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()

    print("👀 Observando cambios en archivos Python...")

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()
        observer.join()
