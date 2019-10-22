import webview

if __name__ == "__main__":
    window = webview.create_window("My Web Blog","index.html", width=1000, height=600)
    webview.start()
