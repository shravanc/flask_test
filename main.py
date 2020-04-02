from app import create_app

if __name__ == "__main__":
  application = create_app('development.cfg')
  application.run(debug=True, host="0.0.0.0", port="5000")

