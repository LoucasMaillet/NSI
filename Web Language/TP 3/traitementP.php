<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml" lang="fr">

<head>
    <title>Traitement</title>
    <meta http-equiv="content-type" content="text/html;charset=utf-8" />
    <link rel="stylesheet" href="style.css">
    <script src="script.js"></script>
</head>


<body>
    <?php
    $n_POST=$_POST["nom_post"];
    $p_POST=$_POST["prenom_post"];
    $a_POST=$_POST["age_post"];
    
    echo '<h2>Bonjour</h2><p>'.$p_POST.' '.$n_POST.', tu as '.$a_POST.' ans</p>'?>
    
</body>
</html>