<html>
<head><title>Data Retrieving </title>
<style>
  {
    padding:1em
   }
</style>
</head>
</html>
  


<?php
  $con=Mysqli_Connect("localhost","root","","Soorya");
   if(!$con)
{
  echo "Connection error!";
}
  else
{
   $query="select * from sootb1"; 
   $values=mysqli_query($con,$query);
   echo'<table border="1">
   <th>Name</th>
   <th>Email</th>
   <th>Mobno</th> 
   <th>User name</th>
   <th>Password</th>';
if(mysqli_num_rows($values)) 
   {
    while($row=mysqli_fetch_assoc($values)){
  echo'<tr>';
    echo'<td>';
    echo $row["Name"];
    echo'</td>';
    echo'<td>';
    echo $row["Email"];
    echo'</td>';
    echo'<td>';
    echo $row["Mobno"];
    echo'</td>';
    echo'<td>';
    echo $row["Username"];
    echo'</td>';
    echo'<td>';
    echo $row["Password"];
    echo'</td>';
  echo'</tr>';
    }
}
else 
 {
   echo "Error".$query.mysqli_error($con);
 }

}
?>

    



