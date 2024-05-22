<?php

define("SERVEUR","localhost");
define("USER","user");
define("MDP","user");
define("BD","Exoplanets");


function connexionBd($Serveur="localhost",$User="user",$Mdp="user",$Bd="Exoplanets"){
  // gestion de la connexion
      try
      {
          $connexion= new PDO('mysql:host='.$Serveur.';dbname='.$Bd, $User, $Mdp);
          $connexion->exec("SET CHARACTER SET utf8"); //Gestion des accents
          return $connexion;
      }
  
  //gestion des erreurs
      catch(Exception $e)
      {
          echo 'Erreur : '.$e->getMessage().'<br />';
          echo 'N° : '.$e->getCode();
      }
  }

?>
