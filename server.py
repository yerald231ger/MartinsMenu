import http.server
import socketserver
import qrcode
import socket
import webbrowser
from threading import Thread

def get_ip():
    return "192.168.100.187"  # Your local IP

def create_qr_code(url):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save("qr_code.png")
    print(f"\nQR Code has been generated as 'qr_code.png'")
    print(f"Scan it with your phone's camera to access the menu!")

def run_server():
    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"\nServer running at http://{get_ip()}:{PORT}")
        print("Press Ctrl+C to stop the server")
        httpd.serve_forever()

if __name__ == "__main__":
    ip = get_ip()
    url = f"http://{ip}:8000"
    
    print("\nGenerating QR code...")
    create_qr_code(url)
    
    print("\nStarting server...")
    server_thread = Thread(target=run_server)
    server_thread.start()
    
    # Open the browser
    webbrowser.open(url)
