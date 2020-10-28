<?php
    header("Content-type: text/html;charset=\"utf-8\"");
    $error = ""; $mensajeExito = "";

    if ($_POST) {
        if ($_POST['email'] && filter_var($_POST["email"], FILTER_VALIDATE_EMAIL) === false) {
            $error .= "E-mail no válido.<br>";   
        }
        if ($error != "") {
            $error = '<div class="alert alert-danger" role="alert"><p><b>Se generó un error:</b></p>' . $error . '</div>';
        } else {
            $nombre = $_POST['nombre'];
            $mail = $_POST['email'];
            $asunto = $_POST['asunto'];
            $mensajeC = $_POST['mensaje'];
            
            $header = 'From: ' . $mail . " \r\n";
            $header .= "X-Mailer: PHP/" . phpversion() . " \r\n";
            $header .= "Mime-Version: 1.0 \r\n";
            $header .= "Content-Type: text/plain";

            $mensaje = "Este mensaje fue enviado por " . $nombre . ",\r\n";
            $mensaje .= "Su e-mail es: " . $mail . " \r\n";
            $mensaje .= "Asunto: " . $asunto . " \r\n";
            $mensaje .= "Mensaje: " . $mensajeC . " \r\n";
            $mensaje .= "Enviado el " . date('d/m/Y', time());

            $para = 'tu-nombre@tu-dominio.com';
            $asunto = 'Mensaje de mi sitio web';

            if (mail($para, $asunto, utf8_decode($mensaje), $header)) {
                $mensajeExito = '<div class="alert alert-success" role="alert">Mensaje enviado con éxito :)</div>';    
            } else {
                $error = '<div class="alert alert-danger" role="alert"><p><strong>Mensaje sin enviar :(</div>';  
            } 
        }  
    }
?>


<!DOCTYPE html>
<html lang="es">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="css/bootstrap.css">
        
  </head>
  <body>
 
  <!-- menú de navegación -->
  <nav class="navbar navbar-inverse bg-inverse navbar-toggleable-sm sticky-top">
    <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
    </button>
    <a class="navbar-brand" href="index.html">
    <img src="images/bootstrap-solid.svg" width="30" height="30" class="d-inline-block align-top" alt="Logo Bootstrap">
    Bootstrap
    </a>
    <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
    <div class="navbar-nav mr-auto ml-auto text-center">
      <a class="nav-item nav-link " href="#">Inicio</a>
      <a class="nav-item nav-link active" href="#">Nosotros</a>
      <a class="nav-item nav-link" href="#">Servicios</a>
      <a class="nav-item nav-link" href="#">Contacto</a>
    </div>
    <div class="d-flex flex-row justify-content-center">
      <a href="#" class="btn btn-outline-primary mr-2">F</a>
      <a href="#" class="btn btn-outline-danger">Y</a>
    </div>
    </div>
  </nav>
  <!-- fin menú de navegación -->
  
  <!-- Formulario 1 -->
  
  <section class="container mt-5 pt-5">
    <h3 class="text-uppercase text-center">Formulario de contacto</h3>
    <p class="lead text-center">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus hic sint non rem quibusdam. Dicta facilis dignissimos deserunt, mollitia dolores.</p>

    <div class="container">
      <div><? echo $error.$mensajeExito; ?></div>
      <form method="post">
        <div class="form-group row">
            <label for="nombre" class="col-sm-2 form-control-label">Nombre</label>
            <div class="col-sm-10">
              <input class="form-control" id="nombre" placeholder="Escribe tu nombre" type="text" name="nombre">
            </div>
        </div>
        <div class="form-group row">
          <label for="email" class="col-sm-2 form-control-label">Email</label>
          <div class="col-sm-10">
            <input class="form-control" id="email" placeholder="Escribe tu e-mail" type="email" name="email">
          </div>
        </div>
        <div class="form-group row">
          <label for="asunto" class="col-sm-2 form-control-label">Asunto</label>
          <div class="col-sm-10">
            <input class="form-control" id="asunto" placeholder="Asunto del correo" type="text" name="asunto">
          </div>
        </div>
        <div class="form-group row">
          <label for="mensaje" class="col-sm-2 form-control-label">Mensaje</label>
          <div class="col-sm-10">
            <textarea class="form-control" id="mensaje" rows="3" placeholder="¿Qué quieres preguntar?" name="mensaje"></textarea>
          </div>
        </div>
        <div class="form-group">
          <button type="submit" class="btn btn-warning offset-2">Enviar</button>
        </div>
      </form>
    </div>

  </section>

  <!-- fin Formulario 1 -->

  <div class="container-fluid bg-inverse text-white pt-4 pb-2 mt-5">
    <div class="text-center">
      <p class="lead">No olvides suscribirte a mi canal de Youtube :) <a class="text-white" href="https://www.youtube.com/bluuweb"><button class="btn btn-danger">Bluuweb!</button></a></p>
    </div>
  </div>
    
      
    
    <!-- jQuery first, then Tether, then Bootstrap JS. -->
    <script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>
    <script src="js/bootstrap.min.js"></script>



  </body>
</html>