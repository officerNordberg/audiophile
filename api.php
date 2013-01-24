<?php
if (!$_GET) echo getServers();
if ($_GET['control']) 
{
	file_put_contents("ctl", "{$_GET['control']}\n");

	if ($_GET['control'] == "n") file_put_contents("msg", "Skipped");
}


function getServers() {
	$return = "";

	$servers = file_get_contents("servers");
	unlink("servers");

	$array = explode("\n", $servers);
	foreach ($array as $server) {
           $entry = explode("|", $server);	
	   $name = $entry[0];
	   $address = $entry[1];
           $href = "$.get('api.php',{control:'connect',address:'$address'});"; 
	   $return .= "<h1><a onclick=$href >$name</a></h1>";
        }
	return $return;
}

function getSong() {
	$return = "";
	if (!file_exists("curSong")) 
	{
		$return = "
	<img src=imgs/pandora.png class=albumart alt=\"Pandora logo\" />
	<h1>Hello There</h1>
	<h2>Pianobar is starting up...</h2>";
		die($return);
	}

	if (file_exists("msg"))
	{
		$msg = file_get_contents("msg");
		unlink("msg");
		die("<h1 class=msg>$msg</h1>");
	
	}

	$songInfo = file_get_contents("curSong");
	$arraySong = explode("|", $songInfo);
	$title = $arraySong[0];
	$artist = $arraySong[1];
	$album = $arraySong[2];
	$coverart = $arraySong[3];
	if (!$coverart) $coverart = "imgs/pandora.png";
	$love = $arraySong[4];
	
	if ($love==1) $return .= "<img src=imgs/love.png class=love width=20 />";
	$return .= "
	<img src=$coverart class=albumart alt=\"Artwork for $album\" />
	<h1>$title</h1>
	<h2>$artist</h2>
	<h2 class=album>$album</h2>";
	return $return;
}
?>
