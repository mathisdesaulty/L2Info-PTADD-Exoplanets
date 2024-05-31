<?php 

include 'python.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Récupérer les valeurs du formulaire
    if ($_POST["masse"] != NULL) {
        $masse = floatval($_POST["masse"]);
        // echo "masse" . $masse;
    
        if ($_POST["rayon"]!=NULL) {
            $rayon = floatval($_POST["rayon"]);
            // echo "rayon" .$rayon;
    
                if($_POST["period_orbit"]!=NULL){
                    $periodO = floatval($_POST["period_orbit"]);
                    // echo "period" .$periodO;
                    $val = [$masse, $rayon, $periodO];
                    try {
                        $somme = appelerScriptPython($val);
                    } catch (Exception $e) {
                        echo "Erreur : " . $e->getMessage() . "\n";
                    }
                    // echo "somme" . $somme;
                }
            }
        }
    
    
    
}

if (!isset($somme)) {
    $somme = "";
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="resetFinal.css">
    <link rel="stylesheet" href="stylesFinal.css">
    <link rel="stylesheet" href="responsiveFinal.css">
    <title>Exoplanètes</title>
</head>
<body>
    <main>
        <header>
            <h1>Exoplanètes</h1>
            <nav class="menu">
                <ul>
                  <li><a class="point_actif" href="predictions.php">Prédiction</a></li>
                  <li><a href="Statistics.html">Statistiques</a></li>
                  <li><a href="index.php">Données</a></li>
                </ul>
            </nav>
        </header>
        
        <section class="contenus">
            <article class="contenu">
                <h2>Exoplanète Simulator</h2>
                <p>Créer ta planète à prévoir</p>
                <form action="predictions.php" method="post">
                <p><label for="masse"></label><input type="text" name="masse" id="masse" placeholder="Masse (masse terrestre)" /></p>                                
                <p><label for="rayon"></label><input type="text" name="rayon" id="rayon" placeholder="Rayon (km)" /></p>
                <p><label for="period_orbit"></label><input type="text" name="period_orbit" id="period_orbit" placeholder="Periode Orbite (année)" /></p>
                <p><input type="submit" value="Crée ta planète" name="send"/></p>
            </form>
            </article>

            <article class="contenu">
                <h2>Résultat</h2>
                <p>Résultat de la prédiciton</p>
                <h1 class="resultat"><?=$somme?></h1>
            </article>
        </section>
    </main>
</body>
</html>
