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
$requete= "SELECT name FROM TABLE_NAME";
echo $requete;

//Envoi de la requete
$rep=$connexion->query($requete);

//Recuperation du résultat
$listeLaRochelle=$rep->fetchALL(PDO::FETCH_ASSOC);




?>


<!DOCTYPE html>
<html lang="fr">
    <head>
        <link rel="stylesheet" href="../css/styles.css">
        <link rel="stylesheet" href="../css/reset.css">
        <link rel="stylesheet" href="../css/responsive.css">        
        <title>TD 3</title>
        
        <meta charset="utf-8" />

    </head>

    <body>

            <?php foreach($listeLaRochelle as $unContact) : ?>    
            <tr>
                <td><?=($unContact["name"]) ?> </td>
            </tr>
            <?php endforeach; ?>


    </body>
</html>
