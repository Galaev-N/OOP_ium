"""Точка входа для ЛР-7."""

try:
    from .app import ShopApp
    from .cli import ConsoleUI
except ImportError:
    from app import ShopApp
    from cli import ConsoleUI


def main() -> None:
    """Запускает консольное приложение."""
    app = ShopApp(storage_file="shop_data.json")
    ui = ConsoleUI(app)
    ui.run()


if __name__ == "__main__":
    main()
