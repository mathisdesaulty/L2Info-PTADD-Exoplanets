<?php
function appelerScriptPython($valeurs) {
    // Convertir les valeurs en une chaîne d'arguments
    $args = implode(' ', $valeurs);

    // Préparer la commande pour appeler le script Python
    $commande = escapeshellcmd("python3 python//pythontestsOutilsAnalyse.py $args");

    // Exécuter la commande et capturer la sortie
    $resultat = shell_exec($commande);
    
    // Retourner le résultat
    return trim($resultat);
}
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>