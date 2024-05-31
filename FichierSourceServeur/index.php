<?php

include 'connexion.php';

$connexion=connexionBd();

//EXERCICE 1

//Création de la requete
$requete= "SELECT * FROM Planete";

//Envoi de la requete
$rep=$connexion->query($requete);

//recup des donnees
$listeContacts=$rep->fetchAll(PDO::FETCH_OBJ);


//EXERCICE 2

///Création de la requete
$requete= "SELECT * FROM Planete";

//Envoi de la requete
$rep=$connexion->query($requete);

//Recuperation du résultat
$listeLaRochelle=$rep->fetchALL(PDO::FETCH_ASSOC);

$nombre = 0;

if ($_SERVER["REQUEST_METHOD"] == "POST")
{
    if(isset($_POST['mon_bouton'])) {
        $nombre = count($listeLaRochelle);
    }else{
        $nombre = intval($_POST["nombre"]);
    }
}

?>
<!DOCTYPE html>
<html lang="fr">
    <head>

        <link rel="stylesheet" href="resetFinal.css">
        <link rel="stylesheet" href="stylesFinal.css">     
        <link rel="stylesheet" href="responsiveFinal.css">  
        <link rel="stylesheet" href="tableauFinal.css">
        <title>Exoplanètes</title>
        
        <meta charset="utf-8" />

    </head>

    <body>
        <main>
            <header>
                <h1>Exoplanètes</h1>
                <nav class="menu">
                    <ul>
                    <li><a href="predictions.php">Prédiction</a></li>
                    <li><a href="Statistics.html">Statistiques</a></li>
                    <li><a class="point_actif" href="index.php">Données</a></li>
                    </ul>
                </nav>
            </header>
            
            <article>
                <div class="table-title">
                    <h3>Base de donnée</h3>
                </div>

                <form method="POST" action="index.php">
                    <label for="nombre">Afficher les premières planètes :</label>
                    <p><input type="number" id="nombre" name="nombre"></p>
                    <button type="submit">Afficher</button>
                    <button type="submit" name="mon_bouton" value="clicked">Afficher tout</button>
                    <p>Nombre de planètes affichées : <?=$nombre?></p>
                </form>

                    <table class="table-fill">
                    <thead>
                        <tr>
                        <th class="text-left">Nom</th>
                        <th class="text-left">Distance</th>
                        <th class="text-left">Type</th>
                        <th class="text-left">Magnitude stellaire</th>
                        <th class="text-left">Année de découverte</th>
                        <th class="text-left">Masse</th>
                        <th class="text-left">Diametre</th>
                        <th class="text-left">Periode d'orbite</th>
                        </tr>
                    </thead>
                    <tbody class="table-hover">
                        <?php foreach(array_slice($listeLaRochelle, 0, $nombre) as $p) : ?>
                        <tr>
                            <td class="text-left"><?=$p["name"] ?> </td>
                            <td class="text-left"><?=$p["distance"]?> </td>
                            <td class="text-left"><?=$p["planet_type"]?> </td>
                            <td class="text-left"><?=$p["stellar_magnitude"]?> </td>
                            <td class="text-left"><?=$p["discovery_year"]?> </td>
                            <td class="text-left"><?=$p["mass_multiplier"]?> </td>
                            <td class="text-left"><?=$p["radius_multiplier"]?> </td>
                            <td class="text-left"><?=$p["orbital_period"]?> </td> 
                            <td></td>
                        </tr>
                        <?php endforeach; ?>

                    </tbody>
                </table>
            </article>
        </main>
    </body>
</html>
