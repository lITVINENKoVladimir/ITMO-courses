import psycopg2
import abc

class DB:
    __instance = None
   
    @staticmethod
    def get_instance(dbname="поликлиника", user="postgres", password="123123", host="localhost", port="5432"):
        if DB.__instance is None:
            DB.__instance = DB(dbname, user, password, host, port)
        return DB.__instance

    def __init__(self, dbname, user, password, host, port):
        if DB.__instance is not None:
            raise Exception("This class is a singleton. Use the get_instance() method.")
        try:
            self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
            self.cur = self.conn.cursor()  # Assign cur here, outside the try block
            print("Connection to the database established successfully.")
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")
            self.conn = None  # Indicate connection failure
            self.cur = None

    def execute(self, query, params=None):
        if not self.conn:
            return None #Handle connection error

        try:
            if params:
                self.cur.execute(query, params)
            else:
                self.cur.execute(query)
            self.conn.commit()
            return self.cur.fetchall()
        except psycopg2.Error as e:
            print(f"Error executing the query: {e}")
            return None

    def close(self):
        if self.conn:
            self.cur.close()
            self.conn.close()
            print("Database connection closed.")

class CarFactory:
    @staticmethod
    def create_car(brand, model, **kwargs):
        if brand.lower() == "lada":
            return Lada(model, **kwargs)
        elif brand.lower() == "mercedes":
            return Mercedes(model, **kwargs)
        elif brand.lower() == "toyota":
            return Toyota(model, **kwargs)
        else:
            return None


class AbstractCar(abc.ABC):
    @abc.abstractmethod
    def __init__(self, model, **kwargs):
        self.model = model
        pass

    @abc.abstractmethod
    def sold(self):
        pass

    @abc.abstractmethod
    def discount(self):
        pass


class Car(AbstractCar):
    def __init__(self, model, brand, **kwargs):
        super().__init__(model, **kwargs)
        self.brand = brand

    def sold(self):
        print(f"Автомобиль {self.brand} {self.model} продан")

    def discount(self):
        print(f"На автомобиль {self.brand} {self.model} скидка 5%")

    def __repr__(self):
        return f"{self.brand} {self.model}"



class Lada(Car):
    def __init__(self, model, **kwargs):
        super().__init__(model, "Lada", **kwargs)


class Mercedes(Car):
    def __init__(self, model, **kwargs):
        super().__init__(model, "Mercedes", **kwargs)


class Toyota(Car):
    def __init__(self, model, **kwargs):
        super().__init__(model, "Toyota", **kwargs)


# Пример использования:
db = DB.get_instance()  # Получение единственного экземпляра DB

lada = CarFactory.create_car("lada", "Granta")
mercedes = CarFactory.create_car("mercedes", "S-Class")
toyota = CarFactory.create_car("toyota", "Camry")

print(lada)
lada.sold()
lada.discount()

print(mercedes)
mercedes.sold()
mercedes.discount()

print(toyota)
toyota.sold()
toyota.discount()


db.execute("SELECT version()") #Пример выполнения запроса
db.close()