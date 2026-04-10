import os
import urllib.request
import sys

def download_m3u():
    # Get the URL from environment variable (GitHub secret)
    url = os.getenv('EVENTOS_VIV_URL')
    
    if not url:
        print("Error: EVENTOS_VIV_URL environment variable not set")
        sys.exit(1)
    
    try:
        print(f"Downloading m3u from: {url}")
        
        # Download the file
        urllib.request.urlretrieve(url, 'eventos.m3u')
        
        print("✓ Successfully downloaded m3u playlist")
        print("✓ File saved as: eventos.m3u")
        
        # Verify file was created
        if os.path.exists('eventos.m3u'):
            file_size = os.path.getsize('eventos.m3u')
            print(f"✓ File size: {file_size} bytes")
            return True
        else:
            print("Error: File was not created")
            return False
            
    except urllib.error.URLError as e:
        print(f"Error downloading file: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    download_m3u()