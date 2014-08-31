if __name__ == "__main__":
    from app.app import app_factory

    new_app = app_factory("new_app")

    new_app.run(debug = True)
