<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Sligen Online Demo</title>
    <style>
    body {
        font-size: 1.5em;
    }
    </style>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1>SliGen</h1>
        <hr>
        <h4>Generate slide and pitch like a boss! </h4>
        <?php
            error_reporting(0);
            if($_POST['generate']) {
                $pwd = dirname(__FILE__);
                system("cd {$pwd} && make 2>&1 >/dev/null");
                echo '<p class="text-success">Enjoy your slide!</p>';
            }
        ?>
        <form action="." method="POST">
            <input type="hidden" name="generate" value="1">
            <a href="main/output.html" class="btn btn-lg btn-success" target="_blank">
                <span class="glyphicon glyphicon-film"></span> Preview
            </a>
            <button type="submit" class="btn btn-lg btn-primary">
                <span class="glyphicon glyphicon-random"></span> Generate
            </button>
            <a href="https://github.com/Inndy/sligen" class="btn btn-lg btn-info">
                <span class="glyphicon glyphicon-download-alt"></span> GitHub
            </a>
        </form>
    </div>
</body>
</html>
