<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Sligen Online Demo</title>
</head>
<body>
    <h1>Generate slide and pitch like a boss!</h1>
    <hr>
    <p><a href="main/output.html" target="_blank">Preview</a></p>
    <?php
        error_reporting(0);
        if($_POST['generate']) {
            $pwd = dirname(__FILE__);
            system("cd {$pwd} && make 2>&1 >/dev/null");
            echo '<p>Enjoy your slide!</p>';
        }
    ?>
    <form action="." method="POST">
        <input type="hidden" name="generate" value="1">
        <input type="submit" value="re-generate">
    </form>
    <p>Source code is available <a href="https://github.com/Inndy/sligen">here</a>.</p>
</body>
</html>
