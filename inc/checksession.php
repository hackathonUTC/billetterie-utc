<?php
	// Page d'accueil : /index.php 
	header("Content-Type: text/html; charset=UTF-8"); 
	$root = realpath($_SERVER["DOCUMENT_ROOT"]);
    require_once $root.'/config.inc.php';

 	session_start();
	if( !isset($_SESSION['login']) || $_SESSION['login'] == '' ) {
    	
    	$currentAddr = "http://".$_SERVER["HTTP_HOST"].$_SERVER["REQUEST_URI"];
    	if ($currentAddr != $_CONFIG['service']."/")
    		header('Location: '.$_CONFIG['service']);
    }
?>