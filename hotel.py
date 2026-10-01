
import mysql.connector
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="hotel"
)

def crear():
    firstName = input("Nombre: ")
    lastName = input("Apellido: ")
    numberOfGuests = input("Numero de huespedes: ")
    roomType = input("Tipo Standard, Deluxe, Suite: ")

    if conexion.is_connected():
        cursor = conexion.cursor()
        query = "INSERT INTO reservas (firstName, lastName, numberOfGuests, roomType) VALUES (%s,%s,%s,%s)"
        cursor.execute(query, (firstName, lastName, numberOfGuests, roomType))
        conexion.commit()
        print("SUS DATOS SE ALMACENAN CORRECTAMENTE: ")


def mostrar():
    if conexion.is_connected():
        cursor = conexion.cursor()
        query = ("SELECT * FROM reservas")
        cursor.execute(query)
        for f in cursor.fetchall():
            print(f)

def actualizar():
    id_reserva = input("ID para actualizar: ")
    firstName = input("Nuevo nombre: ")
    lastName = input("Nuevo apellido: ")
    numberOfGuests = input("Nuevo numero de huespedes: ")
    roomType = input("Nuevo tipo Standard, Deluxe, Suite: ")

    cursor = conexion.cursor()
    query = "UPDATE reservas SET firstName=%s, lastName=%s, numberOfGuests=%s, roomType=%s WHERE id=%s"
    cursor.execute(query, (firstName, lastName, numberOfGuests, roomType, id_reserva))
    conexion.commit()
    print("DATOS ACTUALIZADOS CORRECTAMENTE: ")

def eliminar():
    id_eliminar = int(input("ID para borrar: "))
    cursor = conexion.cursor()
    query = "DELETE FROM reservas WHERE id=%s"
    cursor.execute(query, (id_eliminar,))
    conexion.commit()
    print("DATO ELIMINADO CORRECTAMENTE: ")


def menu():
    lista = ["1.INGRESE CLIENTE", "2.CONSULTAR", "3.ACTUALIZAR", "4.BORRAR"]
    for item in lista:
        print(item)
    desis = int(input("INGRESE LA OPCION: "))

    match desis:
        case 1:
            crear()
        case 2:
            mostrar()
        case 3:
            actualizar()
        case 4:
            eliminar()
        case _:
            print("INGRESE UN DATO VALIDO")

menu()