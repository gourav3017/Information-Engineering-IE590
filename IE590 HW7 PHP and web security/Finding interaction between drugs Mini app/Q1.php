<html>
<head>
<style>
body {
  margin: 0;
  min-width: 250px;
  background-color: #FFD700;
}
</style>
</head>
<body>
<?php



$drug1=$_GET["drugone"];
$drug2=$_GET["drugtwo"];

//echo "Comparing ".$drug1;
echo "</br>";
//echo "with ".$drug2;
//$one= "<a href='https://rxnav.nlm.nih.gov/REST/rxcui?name=".$drug1."'>Test GET 1</a>";
$one= 'https://rxnav.nlm.nih.gov/REST/rxcui?name='.$drug1; //create link for drug 1
$two= "https://rxnav.nlm.nih.gov/REST/rxcui?name={$drug2}"; //create link for drug 2
//echo $one;
//echo $two;
//echo "</br>";
//$str = file_get_contents($one);
//$b =$one;


$xml= simplexml_load_file($one) or die("Error: Cannot create object"); //parse xml file
//print_r($xml);
$rxc= $xml->idGroup-> rxnormId;  // parse and get rxnormId for drug 1
//echo $rxc;
if(empty($rxc)){
	echo '<h3>please enter valid drug</h3>';
}else{
echo "</br>";
//echo "https://rxnav.nlm.nih.gov/REST/interaction/interaction.json?rxcui={$rxc}";
echo '<h2>Rxcui code for '.$drug1.' is: '.$rxc.'</h2>';
$rxcuione="https://rxnav.nlm.nih.gov/REST/interaction/interaction.json?rxcui={$rxc}";

$xmltwo= simplexml_load_file($two) or die("Error: Cannot create object"); //parse xml file
//print_r($xml);
$rxctwo= $xmltwo->idGroup-> rxnormId;  // parse and get rxnormId for drug 2

if(empty($rxctwo)){
	echo '<h3>please enter valid drug</h3>';
}else{
$someJSON = file_get_contents($rxcuione);
echo '<h2>Rxcui code for '.$drug2.' is: '.$rxctwo.'</h2>';
  // Convert JSON string to Array
$someArray = json_decode($someJSON,true);

foreach ($someArray['interactionTypeGroup'][0]['interactionType'][0]['interactionPair'] as $character) {
	if($character['interactionConcept'][1]['minConceptItem']['rxcui']==$rxctwo){
	echo '<h2> Affect when '.$drug1.' used with '.$drug2.':<i>'.$character['description'] .'</i></h2>'. '<br>';
	}
}
//echo $someArray['interactionTypeGroup'][0]['interactionType'][0]['interactionPair']['interactionConcept'];
}
}
?>

</body>
</html>
 