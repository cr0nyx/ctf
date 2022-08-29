<?php
libxml_disable_entity_loader (false);
$xmlfile = file_get_contents('php://input');
$dom = new DOMDocument();
libxml_use_internal_errors(true);
$dom->loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD | LIBXML_NONET);
$info = simplexml_import_dom($dom);
if (!$info) {
    foreach (libxml_get_errors() as $error){
        echo $error->message;
    }
}
$name = $info->name;
$password = $info->password;

echo "Scusa come?";
?>
