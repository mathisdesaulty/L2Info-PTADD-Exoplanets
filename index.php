<?php 

include 'python.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Récupérer les valeurs du formulaire
    $masse = intval($_POST["masse"]);
    $rayon = intval($_POST["rayon"]);
    $rayonO = intval($_POST["rayon_orbit"]);
    $periodO = intval($_POST["period_orbit"]);
}

$val = [$masse, $rayon, $rayonO, $periodO];
try {
    $somme = appelerScriptPython($val);
} catch (Exception $e) {
    echo "Erreur : " . $e->getMessage() . "\n";
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="eset.css">
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="responsive.css">
    <title>Exoplanètes</title>

</head>
<body>
    <main>
        <header>
            <h1>ExoPlanetes</h1>
        </header>

            <h2>Exoplanètes Simulator</h2>
            <p>Créer une planète pour la prévoir ensuite</p>
            <form action="index.php" method="post">
                <p><label for="masse"></label><input type="text" name="masse" id="masse" placeholder="Masse" /></p>                                
                <p><label for="rayon"></label><input type="text" name="rayon" id="rayon" placeholder="Rayon" /></p>
                <p><label for="rayon_orbit"></label><input type="text" name="rayon_orbit" id="rayon_orbit" placeholder="Rayon orbit" /></p>
                <p><label for="period_orbit"></label><input type="text" name="period_orbit" id="period_orbit" placeholder="Period orbit" /></p>
                <p><input type="submit" value="Crée ta planète" name="send"/></p>
            </form>

            <p>Resultat : <?=$somme?></p>
    </main>
</body>
</html>
