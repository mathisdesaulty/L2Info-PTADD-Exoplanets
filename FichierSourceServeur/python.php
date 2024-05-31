<?php
function appelerScriptPython($valeurs) {
    // Convertir les valeurs en une chaîne d'arguments
    $args = implode(' ', $valeurs);

    // Préparer la commande pour appeler le script Python
    $commande = escapeshellcmd("python3 pythonFinal/TestPrediction.py $args");

    // Exécuter la commande et capturer la sortie
    $resultat = shell_exec($commande);
    
    // Retourner le résultat
    return trim($resultat);
}