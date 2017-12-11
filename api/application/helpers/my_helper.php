<?php 
if(!function_exists('echoJson'))
{
	function echoJson($array)
	{
		echo json_encode($array, JSON_FORCE_OBJECT);
	}
}
?>