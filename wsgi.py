
import os

from app import app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="10.0.2.15", 
               port=port)
