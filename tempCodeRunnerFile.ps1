# Latido de corazón en consola
$heart1 = @'
  **     **
 ****** ******
***************
***************
 *************
  ***********
   *********
     *****
      ***
       *
'@

$heart2 = @'
  **     **
  **** ****
 ***********
 ***********
  *********
   *******
    *****
     ***
      *
'@

# Limpiar consola
Clear-Host

# Animación de latido
for ($i = 0; $i -lt 10; $i++) {
    Clear-Host
    Write-Host $heart1 -ForegroundColor Red
    Start-Sleep -Milliseconds 400
    Clear-Host
    Write-Host $heart2 -ForegroundColor DarkRed
    Start-Sleep -Milliseconds 200
}

Write-Host "`n¡Tu consola tiene corazón! ❤️" -ForegroundColor Magenta