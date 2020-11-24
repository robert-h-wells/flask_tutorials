"""Application entry point."""
from flask_wtforms_tutorial import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)