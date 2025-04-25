from app import create_app

app = create_app()

if __name__ == '__main__':
    # Set debug to False for production and listen on all network interfaces
    app.run(debug=False, host='0.0.0.0', port=5000)

