<html lang="en">
<head>
    <title>Form Validation</title>
</head>
<body bgcolor="grey">

<?php

    $name = "";
    $email = "";
    $phone = "";
    $address = "";
    $re="^[A-Z0-9a-z]+[!@#$%^&*()_] $^";
    $pattern = "^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$^";

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
    extract($_POST);
    $valid = true;

    if (empty($name)) {
        echo "<script>alert('Please enter name.')</script>";
        $valid = false;
    }

    if (empty($email)) {
        echo "<script>alert('Please enter email.')</script>";
        $valid = false;
    }

    if (!preg_match ($pattern, $email) ){  
        echo "<script>alert('Please enter a valid email.')</script>";
        $valid = false;
    }

    if (empty($phone)) {
        echo "<script>alert('Please enter phone.')</script>";
        $valid = false;
      }
      else{      
         if (strlen ($phone) != 10) {  
         echo "<script>alert('Mobile no must contain 10 digits.')</script>";
      }
    }
   
    if (empty($gender)) {
        echo "<script>alert('Gender is required')</script>";
        $valid = false;
    }

    if (empty($address)) {
        echo "<script>alert('Please provide your Communication Address')</script>";
        $valid = false;
    }
     if (strlen($pass)!=8){
       echo"<script>alert("Password must contain at leat 8 characters!!')</script>
       }
     else if(!preg_match ($re, $pass) ){
       echo "<script>alert(Password mismatch.Renter password!!')</script>
       $valid=false;
     }
    }
    if($valid){
        $name = "";
        $email = "";
        $phone = "";
        $address = "";
        echo "<script>alert('Submission successful!')</script>";  
    }
    }
?>

    <form method="post" action="#">
    <table align="center">
    <tr>
        <td colspan="2"><h1 align="center">Registration Form</h1></td>
    </tr>
    <tr>
        <td>Name:</td>
        <td><input type="text" name="name" value="<?php echo $name; ?>"></td>
    </tr>
    <tr>
       <td>email-Id: </td>
       <td><input type="text" name="email" value="<?php echo $email; ?>"></td>
    </tr>
    <tr>
       <td>Phone Number : </td>
       <td><input type="number" name="phone" value="<?php echo $phone; ?>"></td>
    </tr>
    <tr>
       <td>Gender : </td>
       <td><input type="radio" name="gender" value="male"> Male  
       <input type="radio" name="gender" value="female"> Female  
       <input type="radio" name="gender" value="other"> Other </td>
    </tr>
    <tr>
       <td>Address : </td>
       <td><textarea name="address" value="<?php echo $address;?>"></textarea></td>
    </tr>
 <tr>
      <td>Password:</td>
      <td><input type="password" name="pass"></td>
   </tr>
  <tr>
     <td>Confirm Password: </td>
     <td><input type="password" name="pass1"</td>
  </tr>
    <tr align="center">
       <td colspan="2"><input type="submit" style="width:100%"></td>
    <tr>
    </form>

</body>
</html>