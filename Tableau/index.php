<?php

include 'connexion.php';

$connexion=connexionBd();

//EXERCICE 1

//Création de la requete
$requete= "SELECT * FROM TABLE_NAME";

//Envoi de la requete
$rep=$connexion->query($requete);

//recup des donnees
$listeContacts=$rep->fetchAll(PDO::FETCH_OBJ);


//EXERCICE 2

///Création de la requete
$requete= "SELECT * FROM TABLE_NAME";

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
        <link rel="stylesheet" href="../css/styles.css">
        <link rel="stylesheet" href="tableau.css">
        <link rel="stylesheet" href="../css/reset.css">
        <link rel="stylesheet" href="../css/responsive.css">        
        <title>TD 3</title>
        
        <meta charset="utf-8" />

    </head>

    <body>
        <div class="table-title">
            <h3>Base de donnée</h3>
        </div>

        <form method="POST" action="index.php">
            <label for="nombre">Afficher les 'n' 1ere planetes :</label>
            <p><input type="number" id="nombre" name="nombre"></p>
            <button type="submit">Afficher</button>
            <button type="submit" name="mon_bouton" value="clicked">Afficher tout</button>
            <p>Nombre de planete afficher : <?=$nombre?></p>
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
    </body>
</html>
