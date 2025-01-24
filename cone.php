
<?php
// Datos de conexión a la base de datos
$servername = "localhost";
$username = "root"; // Nombre de usuario predeterminado en XAMPP
$password = ""; // Contraseña predeterminada en XAMPP
$dbname = "wonder 7";

// Crear la conexión a la base de datos
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar si hay errores de conexión
if ($conn->connect_error) {
    die("Error de conexión a la base de datos: " . $conn->connect_error);
}

// Obtener los datos enviados desde el formulario
$usuario = $_POST["usuario"];
$telefono = $_POST["telefono"];
$correo = $_POST["correo"];

// Preparar la consulta SQL para insertar los datos en la tabla
$sql = "INSERT INTO `wonder 7` (`usuario`, `telefono`, `correo`) VALUES ('$usuario', '$telefono', '$correo')";

// Ejecutar la consulta
if ($conn->query($sql) === TRUE) {
    echo "The data has been successfully saved to the database.";
} else {
    echo "Error al guardar los datos: " . $conn->error;
}

// Cerrar la conexión a la base de datos
$conn->close();
?>

