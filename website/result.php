<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
    <link rel="stylesheet" href="table.css">
    <title>Menu</title>
</head>
<body>
    <?php
        require_once "database.php";
        $sql = "SELECT * FROM questionnaire WHERE user_id = (SELECT MAX(user_id) FROM questionnaire)";
        $result = mysqli_query($conn, $sql);
        
    ?>
    <div class="container">
        <table class="table table-bordered" id="test">
            <thead>
                <tr>
                    <th scope="col">Monday</th>
                    <th scope="col">Tuesday</th>
                    <th scope="col">Wednesday</th>
                    <th scope="col">Thursday</th>
                    <th scope="col">Friday</th>
                    <th scope="col">Saturday</th>
                    <th scope="col">Sunday</th>
                </tr>
            </thead>
    <tbody>
    <?php
        if ($result->num_rows > 0) {
        // output data of each row
            while($row = $result->fetch_assoc()) {
                echo "<tr>";
                $days = array("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday");
                foreach ($days as $day) {
                    $data = json_decode($row[$day], true);
                    if (is_array($data)) {
                        echo "<td>";
                        foreach ($data as $meal => $details) {
                            echo $meal . ": " . $details . "<br><br>";
                        }
                        echo "</td>";
                    } else {
                        echo "<td>" . $data . "</td>";
                    }
                }                
            echo "</tr>";  
        }
    }else{
        echo "0 results";
    }
    $conn->close();
    ?>
        </tbody>
  </table>
</div>
</body>
</html>