<?php
session_start();
if (!isset($_SESSION["user"])) {
   header("Location: login.php");
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css">
    <title>User Dashboard</title>
</head>
<body>
    <div class="container position-relative">
    <?php

        if (isset($_POST["submit"])) {
            $sex = $_POST["sex"];
            $age = $_POST["age"];
            $activityLevel = $_POST["activity_level"];
            $weight = $_POST["weight"];
            $goal = $_POST["goal"];

            $errors = array();

            if (empty($sex) OR empty($age) OR empty($activityLevel) OR empty($weight) OR empty($goal)) {
                array_push($errors,"All fields are required");
            }
            require_once "database.php";
            $id = $_SESSION["user"];
            
            $sql = "SELECT * FROM questionnaire WHERE user_id = '$id'";
            $result = mysqli_query($conn, $sql);
            $rowCount = mysqli_num_rows($result);
            if ($rowCount>0) {
                array_push($errors,"Questionnaire data already exists for this user");
            }
            if (count($errors)>0) {
                foreach ($errors as  $error) {
                    echo "<div class='alert alert-danger'>$error</div>";
                }
            } else {
                $sql = "INSERT INTO questionnaire (user_id, sex, age, activity_level, weight, goal) VALUES (?, ?, ?, ?, ?, ?)";
                $stmt = mysqli_stmt_init($conn);
                $prepareStmt = mysqli_stmt_prepare($stmt,$sql);
                if ($prepareStmt) {
                    mysqli_stmt_bind_param($stmt,"isisis",$id, $sex, $age, $activityLevel, $weight, $goal);
                    mysqli_stmt_execute($stmt);
                    echo "<div class='alert alert-success'>Your ansers were successfully added.</div>";
                } else {
                    die("Something went wrong");
                }
            }
        }
    ?>
        <h1>Ēdienkartes aptauja</h1> <br>

        <form action="index.php" method="post">

            <div class="form-group form-check form-check-inline">
                <input type="radio" name="sex" value="male" class="form-check-input"> Vīrietis
            </div>

            <div class="form-group form-check form-check-inline">
                <input type="radio" name="sex" value="female" class="form-check-input"> Sieviete
            </div>

            <div class="form-group">
                <input type="number" name="age" placeholder="Vecums" class="form-control">
            </div>

            <div class="form-group">
                <select name="activity_level" class="form-select">
                    <option value="0">Aktivitātes līmenis</option>
                    <option value="1">Zems</option>
                    <option value="2">Vidējais (1-2 treniņi nedeļā)</option>
                    <option value="3">Aktīvs dzīvesveids (3+ treniņi nedeļā)</option>
                </select>
            </div>
            
            <div class="form-group"><input type="number" name="weight" placeholder="Svars" class="form-control"></div>

            <div class="form-group">
                <select name="goal" class="form-select">
                    <option>Edienkārtes mērķis</option>
                    <option value="1">Mazināt ēdināšanas izmaksas</option>
                    <option value="2">Mazināt ēdiena pagatavošanas laiku</option>
                    <option value="3">Saglabāt esošo svaru</option>
                    <option value="pielikt_svarā">Pielikt svarā</option>
                </select>
            </div>
            
            <div class="form-btn">
                <input type="submit" value="Send" class="btn btn-primary" name="submit">
            </div> <br>
        </form>

        <a href="logout.php" class="btn btn-warning position-absolute bottom-1 start-50 translate-middle-x">Logout</a>
    </div>
</body>
</html>