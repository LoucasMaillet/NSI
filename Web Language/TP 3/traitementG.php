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
    $n_GET=$_GET["nom_get"];
    $p_GET=$_GET["prenom_get"];
    $a_GET=$_GET["age_get"];
    
    echo '<h2>Bonjour</h2><p>'.$p_GET.' '.$n_GET.', tu as '.$a_GET.' ans</p>'?>
    
</body>
</html>