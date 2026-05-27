from app import ShopApp
from cli import ConsoleUI


def main() -> None:
    try:
        # Создаем приложение с указанием файла для сохранения
        app = ShopApp(storage_file="shop_data.json")
        
        # Создаем интерфейс
        ui = ConsoleUI(app)
        
        # Запускаем основной цикл
        ui.run()
        
    except Exception as e:
        print(f"Критическая ошибка при запуске приложения: {e}")
        return


if __name__ == "__main__":
    main()