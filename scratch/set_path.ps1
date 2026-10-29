$current = [Environment]::GetEnvironmentVariable("Path", "User")
$pyPath = "C:\Users\ykdub\AppData\Local\Programs\Python\Python39"
$pyScripts = "C:\Users\ykdub\AppData\Local\Programs\Python\Python39\Scripts"

if ($current -notmatch [regex]::Escape($pyPath)) {
    $newPath = "$pyPath;$pyScripts;$current"
    [Environment]::SetEnvironmentVariable("Path", $newPath, "User")
    Write-Output "SUCCESS: Added Python 3.9 and Scripts to User PATH"
} else {
    Write-Output "INFO: Already in User PATH"
}
