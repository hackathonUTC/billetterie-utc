<?php
	// Page d'accueil : /index.php 
	header("Content-Type: text/html; charset=UTF-8"); 
	$root = realpath($_SERVER["DOCUMENT_ROOT"]);
	require_once $root.'/config.inc.php';
	require_once $root.'/inc/dbconnect.php';

	$email = isset($_POST['email']) ? $_POST['email'] : '';
	$password = isset($_POST['password']) ? $_POST['password'] : '';
	
	if ($email == "" or $password == "")
		header('Location: '.$_CONFIG['home']."admin/");
	
	$sth = $connexion->prepare('SELECT count(*) as `rslt`, `name`, `idAsso`   FROM `compte_assos` WHERE `email` = :email and `password` = SHA1(:password) and `verified` = 1');
	
	$sth->bindParam(':email', $email);
	$sth->bindParam(':password', $password);

	$sth->execute(); 
	$row = $sth->fetch();
	
	if ($row["rslt"] == 1){
		session_start();
		$_SESSION['asso'] = $row["name"];
		$_SESSION['idAsso'] = $row["idAsso"];
		$_SESSION['email'] = $email;
		header('Location: '.$_CONFIG['home']."admin/admin.php");
	}
	else
		header('Location: '.$_CONFIG['home']."admin/");

?>