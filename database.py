import mysql.connector

def crear_base_si_no_existe():
    """
    Crea la base de datos 'academia' si no existe.
    """
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="TuContraseñaSegura"  # Cambia por la tuya
    )
    cursor = conn.cursor()
    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS academia CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
    )
    conn.commit()
    cursor.close()
    conn.close()

def crear_tablas():
    """
    Crea todas las tablas necesarias si no existen.
    """
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="tu_contraseña",  # Cambia por la tuya
        database="academia"
    )
    cursor = conn.cursor()

    # Tabla de Familias Profesionales
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fam_prof (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre_fam VARCHAR(100),
            desc_fam TEXT
        )
    ''')

    # Tabla de Cursos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cursos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            ref_curso VARCHAR(50),
            nombre_curso VARCHAR(100),
            fam_curso INT,
            desc_curso TEXT,
            fecha_curso DATE,
            niv_prof VARCHAR(100),
            FOREIGN KEY (fam_curso) REFERENCES fam_prof(id)
        )
    ''')

    # Tabla de Alumnos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alumnos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            apellidos VARCHAR(100),
            nombre VARCHAR(100),
            dni VARCHAR(20) UNIQUE,
            telf VARCHAR(20),
            mail VARCHAR(100),
            f_nacimiento DATE,
            niv_academico VARCHAR(100)
        )
    ''')

    # Tabla N:M Alumnos-Cursos (inscripciones)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alumno_curso (
            id INT AUTO_INCREMENT PRIMARY KEY,
            alumno_id INT,
            curso_id INT,
            FOREIGN KEY (alumno_id) REFERENCES alumnos(id),
            FOREIGN KEY (curso_id) REFERENCES cursos(id)
        )
    ''')

    # Tabla de cursos finalizados
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cursos_fin (
            id INT AUTO_INCREMENT PRIMARY KEY,
            alumno_id INT,
            curso_id INT,
            fecha_fin DATE,
            FOREIGN KEY (alumno_id) REFERENCES alumnos(id),
            FOREIGN KEY (curso_id) REFERENCES cursos(id)
        )
    ''')

    # Tabla de adjuntos (documentos/fotos)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS adjuntos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            alumno_id INT NOT NULL,
            archivo VARCHAR(255) NOT NULL,
            fecha_subida DATETIME DEFAULT CURRENT_TIMESTAMP,
            descripcion VARCHAR(255),
            FOREIGN KEY (alumno_id) REFERENCES alumnos(id) ON DELETE CASCADE
        )
    ''')

    conn.commit()
    cursor.close()
    conn.close()

def conectar():
    """
    Devuelve una conexión a la base de datos 'academia'.
    Utilízala en el resto de tus módulos para todas las operaciones CRUD.
    """
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="tu_contraseña",  # Cambia por la tuya
        database="academia"
    )

if __name__ == "__main__":
    crear_base_si_no_existe()
    crear_tablas()
    print("Base de datos y tablas creadas o verificadas correctamente.")
